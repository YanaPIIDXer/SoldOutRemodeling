# $Id: inc-html-analyze.cgi 96 2004-03-12 12:25:28Z mu $

$disp.="���s�ꕪ��<HR>";

# ���v/�����o�����X�v�Z
GetMarketStatus();

my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(keys(%marketitemlist)));

$disp.=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);

$disp.=$TB;
$disp.=$TR;
$disp.=$TD.'���i��';
$disp.=$TD.'������<br>�����㐔';
$disp.=$TD.'�O����<br>�����㐔';
$disp.=$TD.'�̔����i<br>����';
$disp.=$TD.'���v�����o�����X<br>';
$disp.=$TRE;
foreach my $ITEM ((sort{$a->{sort} <=> $b->{sort}} values(%marketitemlist))[$pagestart..$pageend])
{
	my $itemno=$ITEM->{no};
	$disp.=$TR;
	$disp.=$TDNW.GetTagImgItemType($itemno).$ITEM->{name};
	$disp.=$TDNW.$ITEM->{todaysale};
	$disp.=$TDNW.$ITEM->{yesterdaysale};
	$disp.=$TDNW.($ITEM->{marketprice} ? "\\".$ITEM->{marketprice} : ($MOBILE?'0':' '));
	$disp.=$TDNW.GetMarketStatusGraph($ITEM->{uppoint});
	#$disp.=$TDNW.$todaystock{$itemno};
	$disp.=$TRE;
}
$disp.=$TBE;
1;
