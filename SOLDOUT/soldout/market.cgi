#! /usr/local/bin/perl
# $Id: market.cgi 96 2004-03-12 12:25:28Z mu $
#use integer;
#use strict;
require './_base.cgi';

my $_town_def;
my %_query=();
my $_market_version=2004021800;
my $_max_cart=5;

_main();
exit 0;

sub _main
{
	my $html='';
	my $mytown_define=_get_mytown_define();
	OutError('���̋@�\�͎g�p�s�ɂȂ��Ă���܂�') if !$mytown_define;
	$_town_def=$mytown_define; # set package global
	
	GetQuery();			# get %Q;
	DataRead();			# get @DT
	_remote_login(\%main::Q) if $Q{entry_code}; # re-set $Q{nm} $Q{ss} session_alive_time
	CheckUserPass(1);	# get $DT or $GUEST_USER
	
	%_query=_clean_query();
	
	$html=$main::GUEST_USER ? _process_guest() : _process_user();
	
	if(!$main::GUEST_USER)
	{
		RequireFile('inc-html-ownerinfo.cgi');
		$main::disp.=$main::MARKET_INFO.'<hr>' if $main::MARKET_INFO;
	}
	OutHTML('�O�o',$main::disp.$html);
}

sub _clean_query
{
	my $val;
	my %q;
	$val=$main::Q{market_code}||'';	$val=~s/\W//g;		$q{market_code}=$val;
	$val=$main::Q{cart}||'';		$val=~s/[^\d\.]//g;	$q{cart}=$val;
	
	$val=$main::Q{itemno}||0;		$val=~s/\D//g;		$q{itemno}=$val+0;
	$val=$main::Q{itemval}||0;		$val=~s/\D//g;		$q{itemval}=$val+0;
	$val=$main::Q{money}||0;		$val=~s/\D//g;		$q{money}=$val+0;
	
	return %q;
}

sub _process_user
{
	if($main::Q{check_cart})
	{
		return _get_html_check_cart($main::Q{check_cart});
	}
	
	my $entry_code=main::GetUserDataEx($main::DT,'_so_market');
	if($entry_code)
	{
		my($market_code,$town_code,$user_id,$password,$stay_limit_time)=split /,/,$entry_code;
		if($stay_limit_time<$main::NOW_TIME)
		{
			Lock();
			DataRead();
			CheckUserPass();
			
			main::SetUserDataEx($main::DT,'_so_market',$stay_limit_time ? '' : "$market_code,$town_code,$user_id,$password,".($main::NOW_TIME+86400*3));
			
			DataWrite();
			DataCommitOrAbort();
			UnLock();
			
			return $stay_limit_time ? _get_html_limit_over() : _get_html_market_login();
		}
		elsif($main::Q{submit_return})
		{
			my($result,$message)=_logout_market_server($market_code);
			return $result ? _get_html_market_logout($message) : _get_html_market_login($message);
		}
		else
		{
			return _get_html_market_login();
		}
	}
	else
	{
		if($main::Q{submit_send})
		{
			my($result,$message)=_login_market_server($_query{market_code});
			return $result ? _get_html_market_login($message) :_get_html_market_list('user',$message);
		}
		elsif($main::Q{submit_stock})
		{
			return _get_html_market_list('user');
		}
		else
		{
			return _get_html_market_list('user');
		}
	}
}

sub _process_guest
{
	return _get_html_market_list('guest');
}

sub _get_mytown_define
{
	return 0 if !$main::MARKET_ENABLE || !$main::TOWN_CODE;
	return _get_town_define($main::TOWN_CODE,'getown');
}

sub _get_town_define
{
	my($town_code,$mode)=@_;
	my $town_def=ReadTown($town_code,$mode);
	return $town_def ? $town_def : 0;
}

sub _get_html_market_login
{
	my($message)=@_;
	my $entry_code=main::GetUserDataEx($main::DT,'_so_market');
	my($market_code,$town_code,$user_id,$password,$stay_limit_time)=split /,/,$entry_code;
	$stay_limit_time||=$main::NOW_TIME+86400*3;
	my $market=_read_market($market_code);
	return '<p>�\���ł��Ȃ��G���[���N���܂����B�g�b�v�����蒼���Ă݂Ă��������B' if !$market;
	
	$message.='<p>����'.$market->{name}.'�֑؍ݒ��ł��B</p>';
	$message.='<p>�؍݊����܂Ŏc��'.GetTime2HMS($stay_limit_time-$main::NOW_TIME).'</p>';
	
	my $go_form=qq|<form action="$market->{forward_url}" $main::METHOD>|;
	$go_form.=qq|<input type=hidden name="entry_code" value="$town_code,$user_id,$password">|;
	#$go_form.=qq|<input type=hidden name="cmd_main" value="go">|;
	$go_form.='<input type=submit value="'.$market->{name}.'�̗l�q�����ɍs��">';
	$go_form.='</form>';
	
	my $return_form=qq|<form action="$main::MYNAME" $main::METHOD>$main::USERPASSFORM|;
	#$return_form.=qq|<input type=hidden name="market_code" value="$market_code">|;
	$return_form.='<input type=submit name="submit_return" value="'.$market->{name}.'����A���Ă���">';
	$return_form.='<input type=checkbox name="compel" value="ok">���i�Ƃ������̂ĂĂł��A���Ă���(�����A��)';
	$return_form.='</form>';
	
	$message.='<hr>' if $message;
	
	return $message.$go_form.$return_form;
}

sub _get_html_market_logout
{
	my($message)=@_;
	
	$message.='<hr>' if $message;
	return $message.'<p>��������Ȃ����B</p><hr>';
}

sub _get_html_market_list
{
	my($mode,$head_msg)=@_;
	
	my @market_list=_read_market_list();
	return '<p>���݁A�O�o�ł������ȏꏊ��������܂���B</p>' if !scalar(@market_list);
	
	my $html=$head_msg||'';
	
	my $cart_in=0;
	my $cart='';
	
	my $disp_enter=$mode eq 'user';
	
	if($disp_enter)
	{
		$html.=qq|<form action="$main::MYNAME" $main::METHOD>$main::USERPASSFORM|;
		
		$cart=$_query{cart};
		my @cart_detail=split(/\./,$cart);
		@cart_detail=@cart_detail[0..$_max_cart*2-1] if scalar(@cart_detail)>$_max_cart*2;
		my %cart_detail=@cart_detail;
		
		my $come_item_no =$_query{itemno};
		my $come_item_val=$_query{itemval};
		if($come_item_no && scalar(keys(%cart_detail))<$_max_cart or !$come_item_val)
		{
			$cart_detail{$come_item_no}=$come_item_val;
		}
		
		$html.='�������o�����i<br>';
		$html.=$main::TB;
		$html.=$main::TR;
		$html.=$main::TD.'���i��';
		$html.=$main::TD.'����';
		$html.=$main::TD.'���݌�';
		$html.=$main::TRE;
		foreach my $item_no (sort{$a<=>$b}keys %cart_detail)
		{
			my $item=$main::ITEM[$item_no]||0;
			my $request=$cart_detail{$item_no};
			if(!$item || !$item->{code} || !$request)
			{
				delete $cart_detail{$item_no};
				next;
			}
			
			my $stock=LibDTItem($main::DT,$item_no);
			$stock=$stock ? $stock.$item->{scale} : '�Ȃ�';
			
			$html.=$main::TR;
			$html.=$main::TD.$item->{name};
			$html.=$main::TD.$request.$item->{scale};
			$html.=$main::TD.$stock;
			$html.=$main::TRE;
		}
		$html.=$main::TBE;
		
		my $itemlist=LibDTItemList($main::DT);
		
		my $select='';
		$select.='<option value="0" selected>���i�I��';
		foreach my $item_no (@$itemlist)
		{
			$select.=qq|<option value="$item_no">$main::ITEM[$item_no]->{name}($main::DT->{item}[$item_no-1])|;
		}
		$html.='���i<select name=itemno>'.$select.'</select>��';
		$html.='<input type=text name=itemval value="0">��';
		$html.='<input type=submit name="submit_stock" value="�����Ă�������������"><br>';
		$html.='����'.($_max_cart-scalar(keys(%cart_detail))).'��ގ����Ă����܂�';
		
		$cart=join '.',%cart_detail;
		$cart=~s/[^\d\.]//g;
		$cart_in=scalar(keys(%cart_detail));
		
		$html.=qq|<input type=hidden name=cart value="$cart">|;
		$html.='<br><br>';
	}
	
	$html.='���O�o��<br>';
	$html.=$main::TB;
	my $checked_market_code=$_query{market_code}||$market_list[0]||'';
	foreach my $market_code (@market_list)
	{
		my $market=_read_market($market_code);
		my $checked=$market_code eq $checked_market_code ? ' checked' : '';
		$html.=$main::TR;
		$html.=$main::TD.qq|<input type=radio name="market_code" value="$market_code"$checked>| if $disp_enter;
		$html.=$main::TD.$market->{name};
		$html.=$main::TD.$market->{comment};
		$html.=$main::TD.qq|<a target="_blank" href="jump.cgi?market=$market_code">|.'��</a>';
		$html.=$main::TRE;
	}
	$html.=$main::TBE;
	if($disp_enter)
	{
		my $money=$_query{money};
		$html.=$cart_in.'��ނ̏��i��';
		$html.='\<input type=text name="money" value="'.$money.'">������<input type=submit name="submit_send" value="�o������">';
		$html.='</form>';
	}
	$html.='<hr>';
	
	return $html;
}

sub _get_html_limit_over
{
	return '�؍݊������߂����܂����̂ŃJ���_��Ŗ߂��Ă��܂����B�����čs�������i�₨���͂����߂��Ă��܂���B';
}

sub _read_market_list
{
	local *DIR;
	opendir(DIR,$main::MARKET_DIR);
	my @market_list=sort map{/^(\w+)$main::FILE_EXT$/} grep(/^\w+$main::FILE_EXT$/,readdir(DIR));
	closedir(DIR);
	
	return @market_list;
}

sub _read_market
{
	my($market_code)=@_;

	my @data=ReadConfig("$main::MARKET_DIR/$market_code$main::FILE_EXT");
	return 0 if scalar(@data)<2;
	
	my %hash=(
		code	=>	$market_code,
		@data
	);
	$hash{name}=main::EscapeHTML($hash{name});
	return \%hash;
}

sub _login_market_server
{
	my($market_code)=@_;
	
	my $market=_read_market($market_code);
	return 0 if !$market;
	
	my $query='';
	my $message='';
	my @result=();
	
	Lock();
	DataRead();
	CheckUserPass();
	
	my $money=$_query{money};
	my $cart=$_query{cart};
	
	my %items=((split /\./,$cart),0 x $_max_cart*2)[0..$_max_cart*2-1];
	delete $items{0};
	my $cartno=1;
	foreach my $itemno (keys %items)
	{
		my $stock=$main::DT->{item}[$itemno-1];
		
		if($itemno<0 || $itemno>$main::MAX_ITEM
		|| !$main::ITEM[$itemno]
		|| !exists $main::ITEM[$itemno]->{code}
		|| $stock<=0
		)
		{
			delete $items{$itemno};
			next;
		}
		$items{$itemno}=$stock if $stock<$items{$itemno};
		$main::DT->{item}[$itemno-1]-=$items{$itemno};
		
		$query.="item${cartno}=$itemno\n";
		$query.="item${cartno}_count=$items{$itemno}\n";
		$query.="item${cartno}_code=$main::ITEM[$itemno]->{code}\n";
		$query.="item${cartno}_name=$main::ITEM[$itemno]->{name}\n";
		$cartno++;
		
		push @result,$main::ITEM[$itemno]->{name}.'��'.$items{$itemno}.$main::ITEM[$itemno]->{scale}.'�����Ă����܂��B'
	}
	
	$money=$main::DT->{money} if $main::DT->{money}<$money;
	$main::DT->{money}-=$money;
	push @result,'\\'.$money.'�����Ă����܂��B' if $money;
	
	$query.="money=$money\n";
	$query.="town_code=$main::TOWN_CODE\n";
	$query.="user_id=$main::DT->{id}\n";
	$query.="user_name=$main::DT->{name}\n";
	$query.="user_shopname=$_town_def->{name}-$main::DT->{shopname}\n";
	$query.="market_version=$_market_version\n";
	$query.="env_HTTP_USER_AGENT=$ENV{HTTP_USER_AGENT}\n";
	$query.="env_HTTP_ACCEPT=$ENV{HTTP_ACCEPT}\n";
	$query.="env_REMOTE_ADDR=$ENV{REMOTE_ADDR}\n";
	#$query.="market_url=http://$ENV{SERVER_NAME}$ENV{SCRIPT_NAME}\n";
	$query.="market_url=http://$ENV{HTTP_HOST}$ENV{SCRIPT_NAME}\n";
	
	my $result=PostHTTP($market->{login_url},$query,$_town_def->{password},'REQUEST_LOGIN');
	
	if($result eq 'OK')
	{
		my $limit=$main::GET_DATA{stay_limit_time}+$main::GET_DATA{entry_time};
		main::SetUserDataEx($main::DT,'_so_market',"$market_code,$main::TOWN_CODE,$main::DT->{id},$main::GET_DATA{password},$limit");
		DataWrite();
		DataCommitOrAbort();
		$message='<ul><li>'.(join '</li><li>',@result).'</li></ul>' if @result;
	}
	else
	{
		my $err=$main::GET_DATA{error_msg};
		
		if($err eq 'deny_login')
		{
			$message='<p>���ݐi���֎~�������ł��B��O��������Ă��܂��܂����B���Ԃ�u���čēx�`�������W���Ă݂Ă��������B</p>';
		}
		elsif($err eq 'deny_version')
		{
			$message='<p>�O�o�葱���̕��@���ς�����悤�ł��B���̊X�̊Ǘ��l����ɂǂ��ɂ����Ă��炤�����Ȃ��ł��ˁB</p>';
		}
		elsif($err eq 'over_capacity')
		{
			$message='<p>'.$market->{name}.'�͐l�ň�t�ł����B���Ԃ�u���čēx�`�������W���Ă݂Ă��������B</p>';
		}
		elsif($err eq 'always_entry')
		{
			$message='<p>���Ȃ���(�Ȃ���)���ł�'.$market->{name}.'�֑؍ݒ��̂悤�ł��B��x(�����I��)�߂��Ă��Ă��������B</p>';
			main::SetUserDataEx($main::DT,'_so_market',"$market_code,$main::TOWN_CODE,$main::DT->{id},,".($main::NOW_TIME+86400));
			DataWrite();
			DataCommitOrAbort();
		}
		else
		{
			$message='<p>�G���[���N��������'.$market->{name}.'�֏o�������܂���ł����B���Ԃ�u���čēx�`�������W���Ă݂Ă��������B['.($err||'unknown_error').']</p>';
		}
	}
	UnLock();
	
	return (($result eq 'ERROR' ? 0 : 1),$message);
}


sub _logout_market_server
{
	my($market_code)=@_;
	
	my $market=_read_market($market_code);
	return 0 if !$market;
	
	my $query='';
	my $message='';
	
	Lock();
	DataRead();
	CheckUserPass();
	
	$query.="town_code=$main::TOWN_CODE\n";
	$query.="user_id=$main::DT->{id}\n";
	$query.="market_version=$_market_version\n";
	
	my $result=PostHTTP($market->{logout_url},$query,$_town_def->{password},'REQUEST_LOGOUT');
	
	if($result eq 'OK')
	{
		my @result=();
		foreach my $cartno (1..100)
		{
			last if !exists $main::GET_DATA{"cart$cartno"};
			my $itemno=$main::GET_DATA{"cart$cartno"};
			my $count=$main::GET_DATA{"cart${cartno}_count"};
			my $code=$main::GET_DATA{"cart${cartno}_code"};
			my $name=$main::GET_DATA{"cart${cartno}_name"};
			
			next if !$count;
			
			my $no_exists=0;
			
			if($itemno<0 || $itemno>$main::MAX_ITEM
			|| !$main::ITEM[$itemno]
			|| !exists $main::ITEM[$itemno]->{code}
			|| $main::ITEM[$itemno]->{code} ne $code
			)
			{
				$no_exists=1;
				foreach my $searchno (1..$main::MAX_ITEM)
				{
					if($main::ITEM[$searchno]->{code} eq $code)
					{
						$itemno=$searchno;
						$name=$main::ITEM[$itemno]->{name};
						$no_exists=0;
						last;
					}
				}
			}
			
			if($no_exists)
			{
				push @result,$name.'�͂��̊X�ɑ��݂��Ȃ����i�ł����̂Ŕj�����܂��B(����'.$count.')';
			}
			else
			{
				$main::DT->{item}[$itemno-1]+=$count;
				my $over=$main::DT->{item}[$itemno-1]-$main::ITEM[$itemno]->{limit};
				if($over>0)
				{
					push @result,$name.'�͂���ȏ�݌ɂł��܂���̂Ŕj�����܂��B(����'.$over.')';
					$main::DT->{item}[$itemno-1]-=$over;
				}
				else
				{
					$over=0;
				}
				push @result,$name.'�������A��܂����B(����'.($count-$over).')';
			}
		}
		if($main::GET_DATA{money})
		{
			LibDTEditMoney($main::DT,$main::GET_DATA{money});
			push @result,'\\'.$main::GET_DATA{money}.'�������A��܂����B';
		}
		
		my $used_time_static=$main::GET_DATA{use_time_static}||0;
		my $used_time_dynamic=$main::GET_DATA{use_time_dynamic}||0;
		my $used_time=$used_time_static+$used_time_dynamic;
		LibDTEditTime($main::DT,-$used_time);
		
		my $used_money_static=$main::GET_DATA{use_money_static}||0;
		my $used_money_dynamic=$main::GET_DATA{use_money_dynamic}||0;
		my $used_money=$used_money_static+$used_money_dynamic;
		$used_money=LibDTEditMoney($main::DT,-$used_money,{abs=>1});
		
		if($used_money or $used_time)
		{
			push @result,$market->{name}.'�ł̏���́A';
			push @result,$main::GET_DATA{use_money_info}.' '.($used_money_static ? '\\'.$used_money_static.'+' : '').'\\'.$used_money_dynamic if $used_money;
			push @result,$main::GET_DATA{use_time_info}.' '.($used_time_static ? main::GetTime2HMS($used_time_static).'+' : '').main::GetTime2HMS($used_time_dynamic) if $used_time;
			push @result,'�ł����B';
		}
		
		main::SetUserDataEx($main::DT,'_so_market','');
		DataWrite();
		DataCommitOrAbort();
		
		$message='<ul><li>'.(join '</li><li>',@result).'</li></ul>' if @result;
	}
	else
	{
		my $err=$main::GET_DATA{error_msg};
		
		if($main::Q{compel})
		{
			main::SetUserDataEx($main::DT,'_so_market','');
			DataWrite();
			DataCommitOrAbort();
			$message='<p>�����Ă��������̂����ׂĂ�j�����A�J���_��Ŗ߂��Ă��܂����B</p>';
			$result='OK';
		}
		else
		{
			if($err eq 'deny_logout')
			{
				$message='<p>����'.$market->{name}.'���猟��ŏo���Ȃ������ł��B���Ԃ�u���čēx�`�������W���Ă݂Ă��������B</p>';
			}
			elsif($err eq 'deny_version')
			{
				$message='<p>'.$market->{name}.'�Ƃ̎葱�����@���ς�����悤�ł��B���̊X�̊Ǘ��l����ɂǂ��ɂ����Ă��炤�����Ȃ��ł��ˁB</p>';
			}
			elsif($err eq 'now_logon')
			{
				$message='<p>�܂��A�鏀�����ł��Ă��Ȃ��悤�ł��B</p>';
			}
			elsif($err eq 'no_entry')
			{
				$message='<p>�Ȃ���'.$market->{name}.'�Ɏp�������܂���B���Ԃ�u���čēx�`�������W���邩�A�����I�ɖ߂��Ă��Ă��������B</p>';
			}
			else
			{
				$message='<p>��������'.$market->{name}.'�͑�ύ��G���Ă��܂��B���Ԃ�u���čēx�`�������W���Ă݂Ă��������B</p>';
			}
		}
	}
	UnLock();
	
	return (($result eq 'ERROR' ? 0 : 1),$message);
}

sub _remote_login
{
	my($query)=@_;
	
	my $entry_code=$query->{entry_code};
	my($town_code,$user_id,$password)=split / /,$entry_code; # ','->' ' X(
	
	return 0 if $main::TOWN_CODE ne $town_code;
	return 0 if !exists $main::id2idx{$user_id};
	
	my $dt=$main::DT[$main::id2idx{$user_id}];
	my $market_entry_info=LibDTUser($dt,'_so_market');
	my($m_market_code,$m_town_code,$m_user_id,$m_password,$m_stay_limit_time)=split /,/,$market_entry_info;
	
	return 0 if $password ne $m_password;
	
	local *SESS;
	my $fn=$main::SESSION_DIR."/".$dt->{name}.".cgi";
	return 0 if !open SESS,$fn;
	my $session=<SESS>;
	chop $session;
	close SESS;
	utime $main::NOW_TIME,$main::NOW_TIME,$fn; # refreshed session time
	
	$query->{nm}=$dt->{name};
	$query->{ss}=$session;
}

sub _get_html_check_cart
{
	my($cart)=@_;
	my $html='';
	#$cart=~s/[^\w,:]//g;
	$cart=~s/%(..)/pack("H2",$1)/ge;
	my %list=split /,/,$cart;
	
	return '�����A�鏤�i�������悤�ł�' if !scalar keys %list;
	
	$html.='<p>�O�o�悩��̏��i�����A��ۂ��m�F��</p>';
	
	$html.=$main::TB;
	$html.=$main::TR;
	$html.=$main::TD.'���i��';
	$html.=$main::TD.'���݌�';
	$html.=$main::TD.'�����A�萔��';
	$html.=$main::TD.'�����A���';
	$html.=$main::TRE;
	foreach my $code (keys %list)
	{
		#$html.=$code;
		my($count,$name)=split /:/,$list{$code},2;
		next if $count=~/\D/ or length $name>64;
		
		$name=EscapeHTML($name);
		my $no=LibItemCode2No($code);
		if($no)
		{
			my $stock=LibDTItem($DT,$no);
			my $over=($stock+$count)-LibItem($no,'limit');
			$over=$over>0 ? '�݌ɃI�[�o�[ +'.$over : '��';
			$html.=$main::TR;
			$html.=$main::TD.$name;
			$html.=$main::TD.$stock.'/'.LibItem($no,'limit');
			$html.=$main::TD.$count;
			$html.=$main::TD.$over;
			$html.=$main::TRE;
		}
		else
		{
			$html.=$main::TR;
			$html.=$main::TD.$name;
			$html.=$main::TD;
			$html.=$main::TD.$count;
			$html.=$main::TD.'�����A��s��';
			$html.=$main::TRE;
		}
	}
	$html.=$main::TBE;
	
	$html.="<hr>\n"._get_html_market_login();
	return $html;
}
