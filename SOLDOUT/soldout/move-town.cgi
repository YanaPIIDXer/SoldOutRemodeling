#! /usr/local/bin/perl
# $Id: move-town.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';

OutError('�g�p�s�ł�') if !$MOVETOWN_ENABLE || !$TOWN_CODE;
my $townmaster=ReadTown($TOWN_CODE,'getown');
OutError('�g�p�s�ł�') if !$townmaster;

GetQuery();
DataRead();
CheckUserPass(1);

if(!$GUEST_USER && $Q{towncode} ne '')
{
	if($Q{pass} ne '')
	{
		OutError('�p�X���[�h������������܂���') if $Q{pass} ne $MASTER_PASSWORD && !CheckPassword($Q{pass},$DT->{pass});
		#�ړ]����
		$disp.=MoveShop($DT,$Q{towncode});
	}
	else
	{
		#�ړ]�p����HTML�\��
		$disp.=GetMoveShopForm($Q{towncode});
	}
}
else
{
	$disp.=GetTownListHTML();
}
OutHTML('�ړ]�葱��',$disp);

exit;

sub GetMoveShopForm
{
	my($towncode)=@_;
	
	my($town)=ReadTown($towncode);
	return '<b>�ړ]�\�ȊX��������܂���</b>' if !$town;
	
	my $disp="";
	
	my $dist=GetTownDistance($townmaster->{position},$town->{position});
	my $movetime=GetMoveTownTime($DT,$townmaster,$town);
	
	$disp.=$TB;
	$disp.="$TR$TD�ړ]��$TD$town->{name}$TRE";
	$disp.="$TR$TD�R�����g$TD$town->{comment}$TRE";
	$disp.="$TR$TD���ݒn����̋���$TD".($dist*80)."m$TRE";
	$disp.="$TR$TD�ړ]��܂ł̈ړ�����$TD".GetTime2HMS($movetime).' ���\�莞�Ԃł��B�ړ]��ɂ���ĕϓ����܂��B'.$TRE;
	$disp.=$TBE;
	
	sub GetMarkDeny
	{
		return $_[0] ? " <font color=red><b>�������𖞂����Ă��܂���</b></font>" : "";
	}
	my @flag=();
	push(@flag,"���� \\$town->{allowmoney} �ȏ�".GetMarkDeny($town->{allowmoney}>$DT->{money}+$DT->{moneystock})) if $town->{allowmoney} ne '';
	push(@flag,"���� \\$town->{denymoney} �ȉ�".GetMarkDeny($town->{denymoney}<$DT->{money}+$DT->{moneystock}))  if $town->{denymoney} ne '';
	push(@flag,"�M���h ".join("/",map{GetTagImgGuild($_,1,1)}split(/\W/,$town->{allowguild})).($town->{onlyguild} ? '':' ����уM���h������')." �̂�".GetMarkDeny($DT->{guild} ne '' && !scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$town->{allowguild}))))) if $town->{allowguild} ne '';
	push(@flag,"�M���h ".join("/",map{GetTagImgGuild($_,1,1)}split(/\W/,$town->{denyguild})).($town->{onlyguild} ? ' ����уM���h������':'')." �ȊO".GetMarkDeny($DT->{guild} ne '' && scalar(grep($_ eq $DT->{guild},split(/[^\w]+/,$town->{denyguild}))))) if $town->{denyguild} ne '';
	push(@flag,"�g�b�v�l���� $town->{allowtopcount} ��ȏ�".GetMarkDeny($town->{allowtopcount}>$DT->{rankingcount})) if $town->{allowtopcount} ne '';
	push(@flag,"�g�b�v�l���� $town->{denytopcount} ��ȉ�".GetMarkDeny($town->{denytopcount}<$DT->{rankingcount}))  if $town->{denytopcount} ne '';
	push(@flag,"�J�Ɗ��� ".GetTime2HMS($town->{allowfoundation})." �ȏ�".GetMarkDeny($town->{allowfoundation}>$NOW_TIME-$DT->{foundation})) if $town->{allowfoundation} ne '';
	push(@flag,"�J�Ɗ��� ".GetTime2HMS($town->{denyfoundation})." �ȉ�".GetMarkDeny($town->{denyfoundation}<$NOW_TIME-$DT->{foundation}))  if $town->{denyfoundation} ne '';
	push(@flag,"�M���h�����̂� ".GetMarkDeny($DT->{guild} eq '')) if $town->{onlyguild} ne '';
	push(@flag,"�M���h�������̂� ".GetMarkDeny($DT->{guild} ne '')) if $town->{noguild} ne '';
	push(@flag,"�E�� ".join("/",map{$JOBTYPE{$_}}split(/\W+/,$town->{allowjob})).($town->{onlyjob} ? '':' ����ѐE�ƕs��')." �̂�".GetMarkDeny($DT->{job} ne '' && !scalar(grep($_ eq $DT->{job},split(/\W+/,$town->{allowjob}))))) if $town->{allowjob} ne '';
	push(@flag,"�E�� ".join("/",map{$JOBTYPE{$_}}split(/\W+/,$town->{denyjob})).($town->{onlyjob} ? ' ����ѐE�ƕs��':'')." �ȊO".GetMarkDeny($DT->{job} ne '' && scalar(grep($_ eq $DT->{job},split(/\W+/,$town->{denyjob}))))) if $town->{denyjob} ne '';
	push(@flag,"�E�ƓX�܂̂� ".GetMarkDeny($DT->{job} eq '')) if $town->{onlyjob} ne '';
	push(@flag,"�E�ƕs��X�܂̂� ".GetMarkDeny($DT->{job} ne '')) if $town->{nojob} ne '';
	$disp.="<br>$TB$TR$TD�ړ]���� ���ړ]��̏������X�V���ꂽ�ꍇ�͕\\�������𖞂����Ă��ړ]�ł��Ȃ��ꍇ������܂�<ul><li>".join("<li>",@flag)."</ul>$TRE$TBE" if scalar(@flag);
	
	$disp.=<<"HTML";
		<form action="$MYNAME" $METHOD>
		$USERPASSFORM
		<input type=hidden name=towncode value="$towncode">
		�ړ]��ł̖��O(ID) <input type=text name=name value="$Q{nm}">(���p�p���̂�)<br>
		���݂̃p�X���[�h <input type=password name=pass value=""><br>
		<input type=submit value="�ړ]�葱���J�n">
		</form>
		<hr>
		�ړ]�ň����p����Ȃ��f�[�^�͉��L�̒ʂ�ł��B����ȊO�͂قڂ��̂܂܈����p����܂��B
		<ul>
		<li>�O���̏��ʏ��
		<li>�X�֔��̒��g�i�S�Ĕj���j
		<li>�ړ]��ɑ��݂��Ȃ����i�i�ꎞ�ۊǁj
		</ul>
		�ꎞ�ۊǂ̏��i�́A���̏��i�����݂���X�ֈړ]����ƕԊ҂���܂����A�ȉ��̏����Ŕj������܂��B
		<ul>
		<li>�ۊǂ���10��̈ړ]�̊Ԃɂ��̏��i�����݂���X�֍s���Ȃ������ꍇ
		</ul>
		�ȉ��̏ꍇ�͈ړ]�̍ۓX�܃f�[�^���ꕔ�����܂�
		<ul>
		<li>�V�X�e���������œX�܃f�[�^�Ɍ݊������Ȃ��ꍇ
		</ul>
		�ȉ��̏ꍇ�͈ړ]�ł��܂���
		<ul>
		<li>���ݏ������̃M���h���ړ]��ɂȂ��ꍇ(�މ��ړ]�����OK)
		<li>�ړ]�悪�����̏ꍇ
		<li>�ړ]��ɓ������O(ID)��X�ܖ�������ꍇ
		</ul>
HTML
	return $disp;
}

sub GetTownListHTML
{
	my @townlist=ReadTown();
	return '<b>�ړ]�\�ȊX��������܂���</b>' if !scalar(@townlist);
	
	my $ret="";
	$ret.='���ړ]�\�ȊX<hr>';
	$ret.=$TB;
	foreach(@townlist)
	{
		$ret.=$TR;
		$ret.=$TDNW.$_->{name};
		$ret.=$TD.$_->{comment};
		$ret.=$TDNW.GetTagA("�m�F","jump.cgi?town=$_->{code}",0,"_blank");
		$ret.=$TDNW.GetTagA("�ړ]�葱��","$MYNAME?$USERPASSURL&towncode=$_->{code}") if !$GUEST_USER;
		$ret.=$TRE;
	}
	$ret.=$TBE;
	
	return $ret;
}

sub MoveShop
{
	my($DT,$towncode)=@_;
	
	my($town)=ReadTown($towncode);
	return '<b>�ړ]�\�ȊX��������܂���</b>' if !$town;
	return '<b>�ړ]��ł̖��O���s���ł�(���p�p��12�����ȓ�)</b>' if $Q{name} eq '' || length $Q{name}>12 || $Q{name}=~/[^\w\-]/;
	
	$DT->{newname}=$Q{name};
	$DT->{newpass}=$Q{pass};
	$DT->{remoteaddr}=GetTrueIP();
	
	require "$ITEM_DIR/funcshopout.cgi" if $DEFINE_FUNCSHOPOUT;
	
	$DT->{_MoveTownTimeSrc}=GetMoveTownTime($DT,$townmaster,$town);
	
	MakeMoveDT($DT);
	my $data=GetDataTree($DT);
	my $subdata=ReadSubData($DT);
	#my $datahash=GetHash(time(),$data);
	my $towndata="code\t$TOWN_CODE\tname\t$townmaster->{name}";
	$towndata.="\tgroup\t$townmaster->{group}" if $townmaster->{group} ne '';
	my $trueip=GetTrueIP();
	my $result=PostHTTP($town->{recvshopurl},"$data\n$subdata->{stock}\n$towndata\n$trueip",$townmaster->{password},$TOWN_CODE);
	
	if($result eq 'OK')
	{
		Lock();
		DataRead();
		CheckUserPass();
		WriteLog(1,0,0,$DT->{shopname}."��".$town->{name}."�ֈړ]���܂���",1);
		CloseShop($DT->{id},$town->{name}."�ֈړ]");
		DataWrite();
		DataCommitOrAbort();
		UnLock();
		my $trash="";
		if($GET_DATA{trash})
		{
			@_=split(/\t/,$GET_DATA{trash});
			my($code,$name)=split(/!/,shift);
			my %trashitem=@_; my $val=0;
			foreach(values(%trashitem)){$val+=$_;}
			$trash=$name."�ŕۊǂ��Ă������i ".scalar(keys(%trashitem))." ��� ".$val." ���j������܂����B";
		}
		return	$town->{name}."�ֈړ]���܂����B<br>".
				GetTagA($town->{name}."�ֈړ�","jump.cgi?town=$town->{code}")."<br><br>".$trash;
	}
	elsif($result eq 'DENY')
	{
		return	"�ړ]�����ۂ���܂����B�ړ]��̏󋵂�ړ]�󂯓�������������m�F�������B<br>".
				"<b>$GET_DATA{msg}</b><br>".
				GetTagA($town->{name}."��K��Ă݂�","jump.cgi?town=$town->{code}","","_blank");
	}
	elsif($result eq 'ERROR')
	{
		return	"�ړ]��ɐڑ��o���܂���ł����B�ړ]��̏󋵂��m�F���A�K�v������Ίe�Ǘ��҂܂ł��A���������B<br>".
				GetTagA($town->{name}."���m�F","jump.cgi?town=$town->{code}","","_blank");
	}
	else
	{
		return "error code [ $result ]";
	}
}

sub MakeMoveDT
{
	my($DT)=@_;
	$DT->{itemcode}={};
	$DT->{expcode}={};
	$DT->{itemyesterdaycode}={};
	$DT->{itemtodaycode}={};
	my $val;
	foreach my $no (1..$MAX_ITEM)
	{
		my $code=$ITEM[$no]->{code};
		
		$val=$DT->{item}->[$no-1];
		$DT->{itemcode}->{$code}=$val if $val;
		
		$val=$DT->{exp}->{$no};
		$DT->{expcode}->{$code}=$val if $val;
		
		$val=$DT->{itemyesterday}->{$no};
		$DT->{itemyesterdaycode}->{$code}=$val if $val;
		
		$val=$DT->{itemtoday}->{$no};
		$DT->{itemtodaycode}->{$code}=$val if $val;
	}
	$DT->{showcasecode}=[];
	foreach my $idx (0..$DT->{showcasecount}-1)
	{
		my $itemno=$DT->{showcase}->[$idx];
		my $price=$DT->{price}->[$idx];
		$price=0 if !$itemno;
		$DT->{price}->[$idx]=$itemno ? $price : 0;
		$DT->{showcasecode}->[$idx]=$itemno ? $ITEM[$itemno]->{code} : "";
	}
	delete $DT->{showcase};
	#delete $DT->{price};
	delete $DT->{item};
	delete $DT->{exp};
	delete $DT->{itemyesterday};
	delete $DT->{itemtoday};
	
	foreach(grep /^_so_trtm_/,keys %{$DT->{user}})
	{
		delete $DT->{user}{$_};
	}
}
