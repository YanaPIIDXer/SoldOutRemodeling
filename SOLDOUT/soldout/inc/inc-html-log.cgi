# $Id: inc-html-log.cgi 96 2004-03-12 12:25:28Z mu $

my $topic=$MYNAME eq "main.cgi";

$disp.="���ŋ߂̏o����(�ŐV��)<HR>";

foreach (sort(@EVENTMSG))
	{$disp.='���:'.$_."<BR>";}
$disp.="<HR SIZE=1>" if defined(@EVENTMSG);

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax);
my $pagecontrol="";

if($topic)
{
	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)=(0,0,$MAIN_LOG_PAGE_ROWS-1,0,0,0);
}
else
{
	($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{lpg},$LIST_PAGE_ROWS,scalar(@MESSAGE));
	
	my $formtarget="<OPTION VALUE=\"\"".($Q{tgt}eq""?" SELECTED":"").">�S";
	foreach (@DT)
	{
		my $name=$_->{shopname};
		#$formtarget.="<OPTION VALUE=\"$name\"".($name eq $Q{tgt}?' SELECTED':'').">$name";
		$formtarget.="<OPTION".($name eq $Q{tgt}?' SELECTED':'').">$name";
	}
	my $formmode="";
	foreach (0..3)
	{
		my $name=('�S','�d�v','���','�s��')[$_];
		$formmode.="<OPTION VALUE=\"$_\"".($Q{lmd}==$_?" SELECTED":"").">$name";
	}
	
	$disp.=<<"HTML";
<form action="$MYNAME" $METHOD>
<input type=hidden name=lpg value="0">
$USERPASSFORM
<select name=tgt>
$formtarget
</select>
<input type=text name=key value="$Q{key}">
<select name=lmd>
$formmode
</select>
<input type=submit value="����">
</form>
HTML

	my $key=$Q{key};
	$key=~s/(\W)/'%'.unpack('H2',$1)/eg;
	my $tgt=$Q{tgt};
	$tgt=~s/(\W)/'%'.unpack('H2',$1)/eg;

	my $search="";
	$search.="&key=".$key if $key ne '';
	$search.="&tgt=".$tgt if $tgt ne '';
	$search.="&lmd=".($Q{lmd}+0) if $Q{lmd};

	$pagecontrol=GetPageControl($pageprev,$pagenext,$search,"lpg",$pagemax,$page);
	$disp.=$pagecontrol;
	
	$disp.="<BR>";
}

foreach my $cnt ($pagestart..$pageend)
{
	my $msg=$MESSAGE[$cnt];
	next if $msg eq '';
	my($tm,$mode,$id,$to,$message,$no)=split(',',$msg);
	
	if($MOBILE)
	{
		if($id==$DT->{id})
			{$disp.="��:".$message;}
		elsif($mode==1)
			{$disp.="���d�v:".$message;}
		elsif($mode==2)
			{$disp.="�����:".$message;}
		elsif($mode==3)
			{$disp.="���s��:".$message;}
		else
			{$disp.=$message;}
	}
	else
	{
		if($id==$DT->{id})
			{$disp.="<FONT COLOR=\"#66cc66\">".$message."(��)</FONT>";}
		elsif($mode==1)
			{$disp.="<FONT COLOR=\"#FF0000\" SIZE=\"+1\"><B>[�d�v]".$message."</B></FONT>";}
		elsif($mode==2)
			{$disp.="<FONT COLOR=\"#FF0000\">[���]".$message."</FONT>";}
		elsif($mode==3)
			{$disp.="[�s��]<B>".$message."</B>";}
		else
			{$disp.=$message;}
	}
	
	$disp.="<BR>";
}

$disp.=$pagecontrol;

1;