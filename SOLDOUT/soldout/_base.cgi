#���̃t�@�C���̃p�[�~�b�V������644(or604or600)�ł��B
# $Id: _base.cgi 106 2004-03-17 13:15:34Z mu $

BEGIN{$SIG{__WARN__}=$SIG{__DIE__}=sub{$incdir=$INCLUDE_DIR; $incdir||="./inc"; require "$incdir/inc-error.cgi"; die($_[0]);};}

SoldOutInit();

sub AUTOLOAD
{
	my($package,$functionname)=$AUTOLOAD=~/^(.*)::(.+)/;
	
	if($package ne 'main')
	{
		@_=caller;
		die(qq|not defined function [$package::$functionname $_[1] line $_[2]] |);
	}
	
	my $requirefile=GetPath("autoload");
	require $requirefile if -e $requirefile; # require autoload index
	
	$requirefile=$autoload{$functionname};
	$requirefile&&=$AUTOLOAD_DIR."/".$requirefile.".cgi";
	require $requirefile if -e $requirefile; # require autoload function
	
	if(!defined(&$functionname))
	{
		my @back=@_;
		RequireFile("inc-autoload.cgi");
		MakeIndexAutoLoad($functionname);
		@_=@back;
	
		if(!defined(&$functionname))
		{
			@_=caller;
			die(qq|not defined function [$functionname $_[1] line $_[2]] |);
			#OutError("not defined function",$functionname) if !defined(&$functionname);
		}
	}
	
	goto &$functionname;
}

sub SoldOutInit
{
	#��������
	srand();
	$disp="";         # �o�̓o�b�t�@������
	$NOW_TIME=time(); # ���ݎ���
	$LOCKED='';       # ���b�N��ԏ�����
	
	($MYDIR,$MYNAME)=($ENV{SCRIPT_NAME}=~/^.*\/([^\/]+)\/([^\/]+)$/); # ���t�@�C����/�f�B���N�g����
	($REFERER)=($ENV{HTTP_REFERER}=~/.+\/(.+)$/);                     # HTTP REFERER
	
	require './_config.cgi';
	
	#my($up1)=(`uptime`=~/(\d+\.\d+)/);
	#OverLoad($up1) if $up1>10;
	
	MenteDisplay() if -e "./lock" || -e "$DATA_DIR/lock"; # �����e���[�h
	
	Lock(),DataCommitOrAbort(1),UnLock() if -e GetPath($COMMIT_FILE);
	
	require(GetPath($ITEM_DIR,"item")) if !$NOITEM;
	require(GetPath($GUILD_FILE));
	
	CheckMobile();
	
	@DTindexnamelist=
		qw(
			id lastlogin name shopname pass money time rank showcasecount comment saleyesterday
			saletoday costyesterday rankingcount remoteaddr pointyesterday rankingyesterday
			paytoday payyesterday profitstock boxcount costtoday options taxyesterday moneystock
			taxtoday guild blocklogin nocheckip foundation
			job icon
		);
	
	@DTindexnamelist_num=
		qw(
			id lastlogin money time rank showcasecount saleyesterday
			saletoday costyesterday rankingcount pointyesterday rankingyesterday
			paytoday payyesterday profitstock boxcount costtoday options taxyesterday moneystock
			taxtoday foundation
		);
	
	push(@BACKUP_FILES,
		(
			$BBS_FILE,
			$CHAT_FILE,
			$GLOBAL_MSG_FILE,
			(map{$GLOBAL_MSG_FILE.'-'.$_}keys %GMSG_CATEGORY_NAME),
			$LOG_FILE.'-s0',
			$LOG_FILE.'-s1',
			$LOG_FILE.'-s2',
			$BOX_FILE,
			$PERIOD_FILE,
			$GUILDBAL_FILE,
			$DATA_FILE,
		)
	);
}

sub GetPath
{
	return $DATA_DIR."/".$_[0].$FILE_EXT if @_==1;
	return join("/",@_).$FILE_EXT;
}

#�g�ђ[���n���ǂ����̃`�F�b�N&�e�[�u����`
sub CheckMobile
{
	my $agent=$ENV{HTTP_USER_AGENT};

	if($agent=~/(DoCoMo|UP\.Browser|J-PHONE)/ || $ENV{HTTP_X_JPHONE_MSNAME} || $DEBUG_MOBILE)
	{
		#�g�ьn
		$MOBILE=1;
		$TB	="";
		$TB2="";
		$TBE="<BR>";
		$TR	="";
		$TRE="<BR>";
		$TD	="<BR>";
		$TDNW="<BR>";
		$TDE="";
		$LIST_PAGE_ROWS=$LIST_PAGE_ROWS_MOBILE;
		$METHOD=qq|method="GET"|;
	}
	else
	{
		#�p�\�R���n
		$MOBILE=0;
		$TB	="<TABLE>";
		$TB2 ="<TABLE>";
		$TBE="</TABLE>\n";
		$TR	="<TR>";
		$TRE="</TR>\n";
		$TD	="<TD>";
		$TDNW="<TD NOWRAP>";
		$TDE="</TD>\n";
		$LIST_PAGE_ROWS=$LIST_PAGE_ROWS_PC;
		$METHOD=qq|method="POST"|;
		
		# Netscape Navigator �ł� img �֘A�̃X�^�C���V�[�g�L�q���폜
		if($ENV{HTTP_USER_AGENT}=~/^Mozilla\/[234][.\d]* \[\w+\]/)
		{
			$HTML_HEAD=~s/\bIMG.*?\{.*?\}\s*\r?\n?//ig;
		}
	}
}

sub OutHeader
{
	$GZIP_ENABLE=0;
	print "Cache-Control: no-cache, no-store\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html; charset=Shift_JIS\n";
	
	print ("\n"),return if $ENV{REQUEST_METHOD} eq "HEAD" || !$GZIP_PATH || $ENV{HTTP_ACCEPT_ENCODING}!~/(x-gzip|gzip)/ || !open(GZIP,"| ".$GZIP_PATH);
	
	$|=1;
	print "Content-encoding: $1\n\n";
	$GZIP_ENABLE=1;
	select(GZIP);
}

sub OutHTML
{
	my $title=shift;
	my $body=\shift;
	my $lastmodified=shift;
	
	print "Last-Modified: ".GetTime2HTTPDate($lastmodified)."\n" if $lastmodified;
	OutHeader();
	return if $ENV{REQUEST_METHOD} eq "HEAD";
	
	my $disp="";
	
	print '<HTML><HEAD>',"\n";
	print $HTML_HEAD if !$MOBILE;
	
	print '<TITLE>SOLD OUT ',$HTML_TITLE,':',$title,'</TITLE>',"\n",'</HEAD>',"\n";
	print $MOBILE ? '<BODY>' : ('<BODY BGCOLOR="',$HTML_BODY_BGCOLOR,'" TEXT="',$HTML_BODY_TEXT,'" LINK="',$HTML_BODY_LINK,'" VLINK="',$HTML_BODY_VLINK,'" ALINK="',$HTML_BODY_ALINK,'" BACKGROUND="',$HTML_BODY_BACKGROUND,'">'),"\n";
	
	my $backurl=GetBackUrl() if $USER and $NOMENU || $Q{bk};
	print($backurl,'<BR><BR>') if $backurl;
	
	if(!$NOMENU and !$MOBILE || $MYNAME eq 'menu.cgi')
	{
		print 'SOLD OUT ',$HTML_TITLE,' <A HREF="index.cgi">[�g�b�v]</A> ';
		print GetMenuTag('help','[�o�c����]','','[��]');
		print '<A HREF="',($MOBILE ? $HOME_PAGE_MOBILE : $HOME_PAGE),'" TARGET=_top>[�z�[��]</A> ';
		
		my $now=$DTlasttime+$TZ_JST-$DATE_REVISE_TIME;
		my $nextday=$now+$ONE_DAY_TIME-($now % $ONE_DAY_TIME);
		print '[���񌈎Z ',GetTime2FormatTime($nextday-$TZ_JST+$DATE_REVISE_TIME),' �܂ł���',GetTime2HMS(int(($nextday-$now)/60)*60+59),']<br>';
		
		print GetMenuTag('bbs',			"[$BBS_TITLE " .GetFileTime($BBS_FILE).']') if $USE_BBS  and !$GUEST_USER || !$DENY_GUEST_BBS;
		print GetMenuTag('chat',		"[$CHAT_TITLE ".GetFileTime($CHAT_FILE).']') if $USE_CHAT and !$GUEST_USER || !$DENY_GUEST_CHAT;
		if($USE_GLOBAL_MSG and !$GUEST_USER || !$DENY_GUEST_GLOBAL_MSG)
		{
			my $lasttime=0;
			foreach($GLOBAL_MSG_FILE,map{$GLOBAL_MSG_FILE.'-'.$_}keys %GMSG_CATEGORY_NAME)
			{
				my $time=(stat(GetPath($_)))[9];
				$lasttime=$time if $lasttime<$time
			}
			;
			print GetMenuTag('gmsg',		"[$GLOBAL_MSG_TITLE ".GetTime2FormatTime($lasttime,1).']');
		}
		print "<br>" if $BBSMENU_BR;
		
		print GetMenuTag('analyze',		'[�s�ꕪ��]','','[��]');
		print GetMenuTag('shop',		'[���X]','','[�X]');
		print GetMenuTag('shop',		'[����]','&t=2','[��]');
		print GetMenuTag('shop-master',	'[�s��]','','[�s]');
		print GetMenuTag('log',			'[�ŋ߂̏o����]','','[��]');
		print GetMenuTag('ranking',		'[�����L���O]','','[��]');
		print GetMenuTag('commentlist',	'[�R�����g�ꗗ]','','[��]');
		print GetMenuTag('guild',		'[�M���h]','','[�g]');
		print GetMenuTag('trade',		'[�f��]','','[�f]') if $TRADE_ENABLE;
		print GetMenuTag('move-town',	'[�߂��̊X]','','[�X]') if $MOVETOWN_ENABLE;
		print GetMenuTag('market',		'[�O�o]','','[�O]') if $MARKET_ENABLE;
		print GetMenuTag('custom',		"[$CUSTOM_TITLE]") if $USE_CUSTOM;
		
		print '<HR SIZE=1>';
		my $bar="";
		if(!$MOBILE)
		{
			print '<A HREF="port.cgi" target="_blank">[�O��]</A> ' if $USE_PORT;
			
			#@CUSTOM_MENU=('1url','1str','2url','2str'); # debug
			for(my $idx=0; $idx<@CUSTOM_MENU; $idx+=2)
			{
				print '<A HREF="',$CUSTOM_MENU[$idx],'" target="_blank">[',$CUSTOM_MENU[$idx+1],']</A> ';
			}
			if(@CUSTOM_MENU || $USE_PORT)
			{
				print '<small>(�ʃE�B���h�E)</small><br>';
				$bar='<HR SIZE=1>';
			}
		}
		if($USER && $USER ne 'soldoutadmin')
		{
			my $boxcount=$DT->{boxcount} ? '<FONT COLOR="#ff6666"><B>('.$DT->{boxcount}.')</B></FONT>' : '';
			print GetMenuTag('main',		'[�X����]','','[��]');
			print GetMenuTag('moneystock',	'[��������]','','[��]');
			print GetMenuTag('stock',		'[�q��]','','[�q]');
			print GetMenuTag('showcase',	'[��I]','','[�I]');
			print GetMenuTag('box',			'[�X�֔�'.$boxcount.']','','[�X'.$boxcount.']');
			print GetMenuTag('other',		'[�e��葱��]','','[��]');
			print GetTagA('[�M���h�{���n��<small>(�ʃE�C���h�E)</small>]',"jump.cgi?myguild=$DT->{name}",0,"_blank") if $JUMP_MY_GUILD && $DT->{guild};
			$bar='<HR SIZE=1>';
		}
		print $bar;
	}
	print CustomMenuBar() if defined &CustomMenuBar;
	
	print GetMenuTag('menu','[���j���[]'),'<br>' if $MOBILE && !$NOMENU && $MYNAME ne 'menu.cgi';
	
	print "\n",$$body,"\n";
	
	print('<BR><BR>',$backurl) if $backurl;
	
	# CPU���׌v�����\��
	@_=times(); $_[0]+=$_[1];
	print '<br><div align="right"><small>',(int($_[0]*1000)/1000),'CPUs</small></div>';
	
	print '</BODY></HTML>',"\n";
	
	close(GZIP),select(STDOUT),$GZIP_ENABLE=0 if $GZIP_ENABLE;
	
	# �����J�E���^����
	GetCounter();
}

sub GetFileTime
{
	return GetTime2FormatTime((stat(GetPath($_[0])))[9]+0,1);
}

sub GetMenuTag
{
	my($loc,$str,$foot,$str_short)=@_;
	$str=$str_short if $USER && $str_short && $DT->{options}&1;
	return qq|<A HREF="$loc.cgi?$USERPASSURL$foot">$str</A> | if $USERPASSURL || $foot;
	return qq|<A HREF="$loc.cgi">$str</A> |;
}

sub GetQuery
{
	my($q)=@_;
	
	if(!$q)
	{
		$ENV{REQUEST_METHOD} eq "POST" ? read(STDIN,$q,$ENV{CONTENT_LENGTH}) : ($q=$ENV{QUERY_STRING});
		$Q{INPUT_DATA}=join(':',$ENV{REQUEST_METHOD},$ENV{CONTENT_LENGTH},$q,$ENV{HTTP_COOKIE});
	}
	return if length($q)<=1;
	
	undef %Q;
	my $key;
	my $cmd=$MYNAME; $cmd=~s/.cgi$//i;
	foreach(split(/&/,$q))
	{
		($key,$_)=split(/=/);
		tr/\?+/  /;
		s/%([a-fA-F0-9][a-fA-F0-9])/pack('H2',$1)/eg;
		tr/"',\x00-\x1f/   /d; #"
		$_=0 if $QUERY_TYPE_TABLE{$key} eq "" && $QUERY_TYPE_TABLE{"$cmd:$key"} eq "" && /^\s*(nan|inf)/i;
		$Q{$key}=$_;
	}
	@Q{qw(nm pw ss)}=split(/!/,$Q{u},3) if exists $Q{u};
}

sub GetCookieSession
{
	my $cookieon=0;
	my($name,$sess)=($ENV{HTTP_COOKIE}=~/SESSION=([\w\-]*)!(\w*)/);
	$name="",$cookieon=1 if $name eq "-check-cookie-";
	return ($name,$sess,$cookieon);
}

sub SetCookieSession
{
	my($name,$sess)=@_;
	$name="-check-cookie-",$sess=time() if $name eq "";
	print "Set-Cookie: SESSION=$name!$sess;\n";
}

sub DataRead
{
	my $datafile=GetPath($DATA_FILE);
	
	open(IN,$datafile);
	read(IN,my $buf,-s $datafile);
	close(IN);
	my @DATA=split(/\n/,$buf);
	
	OutError("no data") if !@DATA;
	
	my $idx=0;
	my $maxdata=@DATA;
	
	$DTlasttime=$DATA[$idx++];
	($DTpeople,$DTnextid,$DTblockip,$DTTradeIn,$DTTradeOut)=split(/,/,$DATA[$idx++]);
	@DTwholestore=split(/,/,$DATA[$idx++],$MAX_ITEM);
	%DTevent=split(/,/,$DATA[$idx++]);
	foreach(keys(%DTevent)){require(GetPath($ITEM_DIR,"event",$_));}
	
	tie($DTtown,"AutoVar",[\$DTtown,$DATA[$idx++],"HASH",","]) if $DATA[$idx] ne '//';
	
	while($DATA[$idx++] ne '//'){}
	
	undef @DT;
	undef %id2idx;
	undef %name2idx;
	undef %name2pass;
	
	my @list;
	my $cnt=0;
	my $id;
	my $name;
	
	while($idx<$maxdata)
	{
		my %DT;
		$DT[$cnt]=\%DT;
		
		@DT{@DTindexnamelist}=split(/,/,$DATA[$idx++]);
		$DT{point}=GetDTPoint(\%DT);
		$DT{status}=1;
		
		$id=$DT{id};
		$name=$DT{name};
		
		$id2idx{$id}=$name2idx{$name}=$cnt;
		$name2pass{$name}=$DT{pass};
		
		$DTnextid=$id+1 if $DTnextid<=$id;
		
		if($MAX_ITEM)
		{
			@list=split(/:/,$DATA[$idx],7);
			@DT{qw(showcase price)}=map{[split(/,/,$_)]}@list[0,1];
			tie $DT{item},"AutoVar",[\$DT{item},$list[2],"ARRAY",","];
			@DT{qw(itemyesterday itemtoday exp)}=map{{split(/,/,$_)}}@list[3,4,5];
			$list[6] ? tie($DT{user},"AutoVar",[\$DT{user},$list[6],"HASH",'[\t,]']) : ($DT{user}={});
			
			#$DT->{item}       =[split(/,/,$list[2],$MAX_ITEM)];
			#tie $DT{itemyesterday},"AutoVar",[\$DT{itemyesterday},$list[3],"HASH",","];
			#tie $DT{itemtoday},"AutoVar",[\$DT{itemtoday},$list[4],"HASH",","];
			#$DT->{user        =$list[6];
			#GetUserData($DT) if $USER_DATA_OLD_MODE;
		}
		$idx++;
		$cnt++;
	}
	
	$DTusercount=$cnt;
}

sub GetDTPoint
{
	my($DT)=@_;
	return int(
		$DT->{rank}*
		(
			($DT->{profitstock}*2+$DT->{saletoday}-$DT->{taxtoday}+$DT->{saleyesterday}-$DT->{taxyesterday})/400000+1
		)
	);
}

sub CheckUserPass
{
	my($guestok)=@_;
	
	my $username=$Q{nm};
	my $password=$Q{pw};
	my $session=$Q{ss};
	my($Cname,$Csess,$cookieon)=GetCookieSession();
	#$disp.="($ENV{HTTP_COOKIE},$Cname,$Csess)"; #debug
	if($username eq '' && $Cname ne '')
		{$username=$Cname;$session=$Csess;}
	else
		{$Cname=$Csess="";}
	
	if($guestok && $username eq '' && $password eq '')
	{
		$DT={};
		$DT->{id}=-1;
		$DTid=$DTidx=0;
		$GUEST_USER=1;
		$USER=$USERPASSURL=$USERPASSFORM="";
		return;
	}
	
	OutError("bad request") if $username eq '';
	OutError("no user",$username) if !exists $name2pass{$username} && $username ne 'soldoutadmin';
	
	my $fn=$SESSION_DIR."/".$username.".cgi";
	
	if($session ne '')
	{
		SetCookieSession(),OutError("timeout") if (stat($fn))[9]<$NOW_TIME-$SESSION_TIMEOUT_TIME || !open(SESS,$fn);
		$_=<SESS>;
		close(SESS);
		chop;
		SetCookieSession(),OutError("timeout") if $_ ne $session;
		utime($NOW_TIME,$NOW_TIME,$fn);
		SetCookieSession($username,$session) if $Cname ne '';
		$MASTER_USER=1 if $username eq 'soldoutadmin';
	}
	else
	{
		if($password ne '')
		{
			$session=CheckLogin($username,$password,$fn);
			if($cookieon)
			{
				SetCookieSession($username,$session);
				$Cname=$username;
				$Csess=$session;
			}
		}
		else
		{
			OutError("no user",$username);
		}
	}
	
	$USER=$username;
	$USERSESSION=$session;
	$USERPASSURL=$USERPASSFORM="";
	if($Cname eq "")
	{
		$USERPASSURL ="u=$username!!$session";
		$USERPASSFORM="<INPUT TYPE=HIDDEN NAME=u VALUE=\"$username!!$session\">\n";
	}
	$COOKIESESSION=$Cname ne "";
	$DTidx=$name2idx{$USER};
	$DT=$DT[$DTidx];
	$DTid=$DT->{id};
	
	$DT->{lastlogin}=$NOW_TIME if !$MASTER_USER && $LOCKED;
	
	require "$ITEM_DIR/funcinit.cgi" if $DEFINE_FUNCINIT;
}

sub GetCounter
{
	my $fn =GetPath($COUNTER_FILE."-l");
	my $fn2=GetPath($COUNTER_FILE."-h");

	open(COUNTER,">>$fn");
	print COUNTER "1";
	
	my $lsize=-s $fn;
	if($lsize>=1000)
	{
		$lsize=0;
		open(COUNTER,">$fn");
		#close(COUNTER);
		
		open(COUNTER,">>$fn2");
		print COUNTER "1";
		#close(COUNTER);
	}
	my $hsize=-s $fn2;

	close(COUNTER);
	return $hsize*1000+$lsize;
}

sub Get02D
{
	return $_[0]<10 ? '0'.$_[0] : $_[0];
}

sub GetTime2HMS
{
	my($tm,$mode)=@_;
	
	my $s=$tm%60;
	return Get02D($s).'�b' if $tm<60;
	
	my $m=($tm-$s)%3600;
	return ($m/60).'��' if $tm<3600;
	
	my $h=($tm-$s-$m)/3600;
	return $h.'����'.($m && !$mode ? Get02D($m/60).'��':'') if $h<24*3;
	
	return int($h/24).'��';
}

sub GetTime2FormatTime
{
	return '--/--' if !$_[0];
	my($sec,$min,$hour,$mday,$mon,$year)=gmtime($_[0]+$TZ_JST);
	$mon++;
	return sprintf("%02d/%02d %02d:%02d",$mon,$mday,$hour,$min) if !$_[1];
	return sprintf("%02d:%02d",$hour,$min) if $_[0]>$NOW_TIME-12*3600 or int(($_[0]+$TZ_JST)/86400)==int(($NOW_TIME+$TZ_JST)/86400);
	return sprintf("%02d/%02d",$mon,$mday);
}

sub GetTime2HTTPDate
{
	my($sec,$min,$hour,$mday,$mon,$year,$wday)=gmtime(shift);
	return sprintf "%s, %02d %s %04d %02d:%02d:%02d GMT",
			(qw(Sun Mon Tue Wed Thu Fri Sat))[$wday],
			$mday,
			(qw(Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec))[$mon],
			$year+1900,
			$hour,
			$min,
			$sec
	;
}

sub GetTagA
{
	#my($str,$href,$nolink,$target)=@_;
	
	return $_[0]." " if $_[2];
	return qq|<a href="$_[1]">$_[0]</a> | if $_[3] eq '';
	return qq|<a target="$_[3]" href="$_[1]">$_[0]</a> |;
}

sub Turn
{
	$DTlasttime=(stat(GetPath($LASTTIME_FILE)))[9];
	return if !$DTlasttime;
	TurnProc() if $NOW_TIME-$DTlasttime>$UPDATE_TIME;
}

sub RequireFile
{
	#my($file)=@_;
	my $customfile="$CUSTOM_DIR/$_[0]";
	
	require (-e $customfile ? $customfile : "$INCLUDE_DIR/$_[0]");
}

require "$ITEM_DIR/funcbase.cgi" if $DEFINE_FUNCBASE;

package AutoVar;

sub Get
{
	my $tied=tied ${$_[0]};
	my $data=$tied ? $tied->[1] : ${$_[0]};
	my $ref=ref $data;
	return $data if !$ref;
	return join $_[1]||",",($ref eq 'ARRAY' ? @$data : %$data);
}

sub TIESCALAR { bless $_[1],$_[0];}

sub FETCH
{
	return $_[0]->[1] if ref $_[0]->[1];
	my @array=split /$_[0]->[3]/,$_[0]->[1];
	my $array=$_[0]->[2] eq 'ARRAY' ? [@array] : {@array};
	$_[0]->[1]=$array;
	untie ${$_[0]->[0]};
	return $array;
}

sub STORE
{
	$_[0]->[1]=$_[1];
	$_[0]->[2]=(ref $_[1])||'ARRAY';
	$_[0]->[3]||=',';
	untie ${$_[0]->[0]} if $_[0]->[2];
	return;
}
1;
