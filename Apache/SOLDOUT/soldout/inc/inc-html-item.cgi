# $Id: inc-html-item.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

GetMarketStatus();

$disp.="���q��<HR>";

my $ITEM=$ITEM[$itemno];

my $itemimage=GetTagImgItemType($itemno,0,2);
#$itemimage.="<br>" if $itemimage ne '';
$disp.= $itemimage;
$disp.="����:".GetTagImgItemType(0,$ITEM[$itemno]->{type}).$ITEM->{name}."<BR>";
$disp.="�݌�:$DT->{item}[$itemno-1] $ITEM->{scale}<BR>";
$disp.="�W��:\\$ITEM->{price}<BR>";
$disp.="�ێ�:\\$ITEM->{cost}<BR>";
$disp.="����:$ITEM->{info}<BR>";
$disp.="<HR SIZE=1>";
if($ITEM->{marketprice})
{
	$disp.="����:\\$ITEM->{marketprice}<br>";
	$disp.="�ň��l:\\$ITEM->{marketpricelow}<br>";
	$disp.="�ō��l:\\$ITEM->{marketpricehigh}<br>";
}
else
{
	$disp.="����:�̔��X�܂Ȃ�<br>";
}
$disp.="����:".GetMarketStatusGraph($ITEM->{uppoint})."<br>";
$disp.="<HR SIZE=1>";

if(CheckItemFlag($itemno,'noshowcase'))
{
	$disp.='���̏��i�͒�ł��܂���<br>';
}
else
{
	$disp.="<FORM ACTION=\"showcase-edit.cgi\" $METHOD>\n";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"$Q{bk}\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=item VALUE=\"$itemno\">";
	$disp.="���̏��i��";
	$disp.="<SELECT NAME=no>";
	foreach my $cnt (1..$DT->{showcasecount})
	{
		$disp.="<OPTION VALUE='".($cnt-1)."'".($showcase==$cnt?' SELECTED':'').">";
		$disp.="�I$cnt($ITEM[$DT->{showcase}[$cnt-1]]->{name})";
	}
	$disp.="</SELECT>";
	$disp.="�֕W�����i��";
	$disp.=<<STR;
<SELECT NAME=per>
<OPTION VALUE='50'>5����
<OPTION VALUE='60'>4����
<OPTION VALUE='70'>3����
<OPTION VALUE='80'>2����
<OPTION VALUE='90'>1����
<OPTION VALUE='100' SELECTED>�܂�
<OPTION VALUE='110'>1����
<OPTION VALUE='120'>2����
</SELECT>
�܂���
<INPUT TYPE=TEXT NAME=yen SIZE=6 VALUE="$Q{pr}">�~
��
<INPUT TYPE=SUBMIT VALUE='�񂷂�'>
(����${\GetTime2HMS($TIME_EDIT_SHOWCASE)}����)
</FORM>
STR
}

1;
