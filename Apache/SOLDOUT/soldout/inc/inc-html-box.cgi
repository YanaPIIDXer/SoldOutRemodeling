# $Id: inc-html-box.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

my $expiretime=$NOW_TIME-$BOX_STOCK_TIME; #$BOX_STOCK_TIME�o�߂Ŋ����؂ꈵ��
my $usertaxrate=GetUserTaxRate($DT);
my $sitetaxrate=GetTradeTaxRate();

$disp.="���X�֔�<HR>";

$disp.="�ǂ񂾂炷���ɕԓ������܂��傤�B�ԓ����Ȃ��Ƒ���ɖ��f��������܂��B<HR>";

$disp.="<DIV ALIGN=right><a href=\"box-edit.cgi?$USERPASSURL&reset=0\"><SMALL>��M�����Z�b�g</SMALL></a></DIV>" if $DT->{boxcount}<0;
$disp.="<a href=\"box-edit.cgi?$USERPASSURL&cmd=newmail\">[���b�Z�[�W���M]</a><BR>";
$disp.="<a href=\"box-edit.cgi?$USERPASSURL&cmd=newmoney\">[����]</a><BR>";
$disp.="<a href=\"box-edit.cgi?$USERPASSURL&cmd=newitem\">[���i���t]</a><BR>";

my @BOX=(@INBOX,@OUTBOX,@RETBOX);
chop @BOX;

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{lpg},int($LIST_PAGE_ROWS/2),scalar(@BOX));

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","lpg",$pagemax,$page);
$disp.=$pagecontrol;

$disp.="<BR>";
#$disp.=$TB if !$MOBILE;
$disp.="<HR SIZE=\"1\">";

foreach my $cnt ($pagestart..$pageend)
{
	my $box=$BOX[$cnt];
	my($no,$from,$to,$flag,$modtime,$cmd,$time,$price,$data,$msg)=split(/,/,$box);
	$main::no=$no;

	my($sendrecv,$sname,$name);
	($sendrecvmode,$sname,$name)=(1,GetID2UserName($from)) if $DT->{id}==$to;
	($sendrecvmode,$sname,$name)=(0,GetID2UserName($to  )) if $DT->{id}==$from;
	$name="($name)" if $name ne '';
	my $fmttime=GetTime2FormatTime($time);
	
	my $cmdname=$CMDLIST[$cmd];
	
	my($itemno,$itemcount,$trademode,$hostcode,$boxno,$shopname,$hostname,$shopmsg);
	($itemno,$itemcount)=split(/!/,$data) if $cmd==$CMD_ITEM;
	($itemno,$itemcount,$trademode,$hostcode,$boxno,$shopname,$hostname,$shopmsg)=split(/!/,$data,6),($shopname,$hostname,$shopmsg)=($shopname=~/^(.*)!([^!]*)!([^!]*)$/) if $cmd==$CMD_TRADE;
	my $ITEM=$ITEM[$itemno],my($taxrate,$tax)=GetSaleTax($itemno,$itemcount,$price,$usertaxrate+($cmd==$CMD_TRADE?$sitetaxrate:0)) if $cmd==$CMD_ITEM || $cmd==$CMD_TRADE;
	$shopmsg=EscapeHTML($shopmsg);
	
	my $yesno=$flag & $FLAG_RETURN_YESNO ? "�͂�" : "������";
	my $workflag_pay =$flag & $FLAG_PAY;
	my $workflag_read=$flag & $FLAG_TO_READ;
	my $workflag_expire=$modtime<$expiretime;
	
	my $returnmail="<a href=\"box-edit.cgi?$USERPASSURL&cmd=newmail&sendmail=".($DT->{id}==$to?$from:$to)."\">���b�Z�[�W�ԐM</a>" if $cmd!=$CMD_TRADE;
	
	$disp.=GetTagDelete(($workflag_read?'�폜':'�����폜'))."�F" if ($workflag_read || $workflag_expire) && $sendrecvmode==0;
	$disp.=$SENDRECV[$sendrecvmode]."�F".$fmttime."�F".$sname.$name."�F".$cmdname."�F".$returnmail."<BR>";
	my $ret="";
	if($sendrecvmode==0)
	{
		if($cmd==$CMD_MAIL)
		{
			$ret.="�^�C�g���F".$data."<BR>";
			$ret.="���e�F".$msg."<BR>";
			$ret.="��񗿁F\\".$price."<BR>"   if $price;
			$ret.="�󂯎�苑�ۂ���܂���<BR>" if $workflag_read && $price && !$workflag_pay;
			$ret.="\\$price�������܂���<BR>"   if $price && $workflag_pay;
			$ret.="�Ԏ����͂��Ă��܂��F�ԓ��́u".$yesno."�v�ł�" if $workflag_read && (!$price || ($price && $workflag_pay));
		}
		if($cmd==$CMD_MONEY)
		{
			$ret.="�^�C�g���F".$data."<BR>";
			$ret.="���e�F".$msg."<BR>";
			$ret.="�����z�F\\".$price."<BR>";
			$ret.="\\$price�󂯎���܂���<BR>" if $workflag_pay;
			$ret.="�󂯎���f���܂���<BR>"   if !$workflag_pay && $workflag_read;
		}
		if($cmd==$CMD_ITEM)
		{
			$ret.=$ITEM->{name}." ".$itemcount.$ITEM->{scale}."<BR>";
			$ret.="���e�F".$msg."<BR>";
			$ret.="����F\\".$price."�@���p�ŁF\\".$tax."�@�ŗ��F".$taxrate."%<BR>" if $price;
			$ret.="�\\�z��掞�ԁF".GetTime2HMS(GetTimeDeal($price,$itemno,$itemcount))."<br>";
			$ret.="\\$price�������܂���<BR>"       if $price && $workflag_pay;
			$ret.="���i�󂯎���f���܂���<BR>" if $workflag_read && !$workflag_pay;
			$ret.="���i���󂯎���܂���<BR>"     if $workflag_read && $workflag_pay;
		}
		if($cmd==$CMD_TRADE)
		{
			$ret.="<b>".($trademode ? "�A�o":"�A��:$shopname:$hostname")."</b><br>";
			$ret.=$ITEM->{name}." ".$itemcount.$ITEM->{scale}."<BR>";
			$ret.="���e�F".($trademode ? $msg : $shopmsg)."<BR>";
			$ret.="����F\\".$price."�@���p�ŁF\\".$tax."�@�ŗ��F".$taxrate."%<BR>" if $price &&  $trademode;
			$ret.="�x���ϑ���F\\".$price."<BR>"                                    if $price && !$trademode;
			$ret.='�\�z��掞�ԁF'.GetTime2HMS(GetTimeDeal($price,$itemno,$itemcount))."<br>" if  $trademode || !$DT->{user}{"_so_trtm_$no"};
			$ret.='����ώ��ԁF'.  GetTime2HMS($DT->{user}{"_so_trtm_$no"})           ."<br>" if !$trademode &&  $DT->{user}{"_so_trtm_$no"};
			if($trademode) # 0:�A�� 1:�A�o
			{
				$ret.="���i������A\\$price�������܂���<BR>"       if $workflag_pay && $workflag_read;
				$ret.="���i�͔���܂���ł���<BR>"                 if !$workflag_pay && $workflag_read;
			}
			else
			{
				$ret.="���i���󂯎��܂���<BR>"     if $workflag_pay && $workflag_read;
				$ret.="���i����ɓ���邱�Ƃ��o���܂���ł���<BR>" if !$workflag_pay && $workflag_read;
			}
		}
		$ret.="�ԓ��҂��ł�" if !$workflag_read;
	}
	else
	{
		$ret.='<B>�ۊǊ������߂��܂����̂ō폜�����\��������܂�</B><BR>' if !$workflag_read && $workflag_expire;
		if($cmd==$CMD_MAIL)
		{
			$ret.="�^�C�g���F".$data."<BR>";
			$ret.="���e�F".$msg."<BR>"        if $workflag_pay || !$price;
			$ret.="��񗿁F\\".$price."<BR>"  if $price;
			$ret.="\\$price�x�����܂���<BR>"  if $workflag_pay;
			$ret.="���񋟂�f��܂���<BR>"  if $price && !$workflag_pay && $workflag_read;
			$ret.="�Ԏ��𑗂�܂����F�ԓ��́u".$yesno."�v�ł�" if $workflag_read && (!$price || ($price && $workflag_pay));
			$ret.="���e������ɂ�\\$price�x�����K�v������܂�"
				."�u".GetTagAllow('�x����')."�v�u".GetTagDeny('���Ȃ�')."�v" 
				if $price && !$workflag_pay && !$workflag_read;
			$ret.="�ԓ���I�����Ă��������u".GetTagAllow('�͂�')."�v�u".GetTagDeny('������')."�v" 
				if (!$price || ($price && $workflag_pay)) && !$workflag_read;
		}
		if($cmd==$CMD_MONEY)
		{
			$ret.="�^�C�g���F".$data."<BR>";
			$ret.="���e�F".$msg."<BR>";
			$ret.="�����z�F\\".$price."<BR>";
			$ret.="\\$price�󂯎��܂���<BR>"   if $workflag_pay;
			$ret.="�����󂯎���f��܂���<BR>" if !$workflag_pay && $workflag_read;
			$ret.="����\\$price���󂯎��܂����H"
				."�u".GetTagAllow('�󂯎��')."�v�u".GetTagDeny('�󂯎��Ȃ�')."�v" 
				if !$workflag_read;
		}
		if($cmd==$CMD_ITEM)
		{
			$ret.=$ITEM->{name}." ".$itemcount.$ITEM->{scale}."<BR>";
			$ret.="���e�F".$msg."<BR>";
			$ret.="����F\\".$price."<BR>"                 if $price;
			$ret.="����ԁF".GetTime2HMS(GetTimeDeal($price,$itemno,$itemcount))."<br>";
			$ret.="\\$price�x����"                         if $price && $workflag_pay;
			$ret.="���i���󂯎��܂���<BR>"               if $workflag_pay;
			$ret.="���i�󂯎���f��܂���<BR>"           if !$workflag_pay && $workflag_read;
			$ret.="������x������"                         if $price && !$workflag_read;
			$ret.="���i���󂯎��܂����H"
				."�u".GetTagAllow('�󂯎��')."�v�u".GetTagDeny('�󂯎��Ȃ�')."�v" 
				if !$workflag_read;
		}
	}
	$disp.=$ret;
	$disp.="<HR SIZE=\"1\">";
}
#$disp.=$TBE if !$MOBILE;

$disp.=$pagecontrol;

sub GetTagDelete
{
	my($msg)=@_; $msg='�폜' if $msg eq '';
	return "<a href=\"box-edit.cgi?$USERPASSURL&del=$no\">$msg</a>";
}
sub GetTagDeny
{
	my($msg)=@_; $msg='��拑��' if $msg eq '';
	return "<a href=\"box-edit.cgi?$USERPASSURL&dny=$no\">$msg</a>";
}
sub GetTagAllow
{
	my($msg)=@_; $msg='��旹��' if $msg eq '';
	return "<a href=\"box-edit.cgi?$USERPASSURL&alw=$no\">$msg</a>";
}
1;
