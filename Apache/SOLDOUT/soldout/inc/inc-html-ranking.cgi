# $Id: inc-html-ranking.cgi 96 2004-03-12 12:25:28Z mu $

my ($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
	=GetPage($Q{pg},($MYNAME eq 'index.cgi' ?$TOP_RANKING_PAGE_ROWS:$RANKING_PAGE_ROWS),$DTusercount);

$disp.="�������L���O<HR>";
$disp.="�l��:".int($DTpeople/10)."<BR>";

my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);
$disp.=$pagecontrol."<BR>";

$disp.=$TB;

if(!$MOBILE)
{
	$disp.=$TR;
	$disp.=$TDNW."����<BR><SMALL>(�O����)</SMALL><br>�_��";
	$disp.=$TDNW.$SHOP_ICON_HEADER if $SHOP_ICON_HEADER && !$MOBILE;
	$disp.=$TDNW."�X��<BR>�l�C";
	$disp.=$TDNW."��������";
	$disp.=$TDNW."����<BR>�O������";
	$disp.=$TDNW."�O��<BR>�ێ���<BR>�ŋ�";
	$disp.=$TD."�戵���i�@�ꉟ���i<BR>�y�n���x���v�z�y�n�Ɓz �R�����g";
	$disp.=$TRE;
}
else
{
	$tdh_rk="RANK:";
	$tdh_pt="�_��:";
	$tdh_nm="�X��:";
	$tdh_pp="�l�C:";
	$tdh_mo="����:";
	$tdh_ts="�{��:";
	$tdh_ys="��:";
	$tdh_cs="�ێ�:";
	$tdh_sc="�ꉟ:";
	$tdh_cm="�ꌾ:";
	$tdh_tx="���:";
	$tdh_ex="�n��:";
	$tdh_fd="�n��:";
}

foreach my $idx ($pagestart..$pageend)
{
	my $DT=$DT[$idx];
	
	my $rankupdown="";
	if($DT->{rankingyesterday})
	{
		$rankupdown=$DT->{rankingyesterday}-$idx-1;
		$rankupdown=$rankupdown==0 ? "��": $rankupdown<0 ? "��".(-$rankupdown) : "��".$rankupdown;
		$rankupdown="<small>($rankupdown)</small>";
	}
	my $itemtype=-1;
	my $itempro="";
	my $salelist="";
	foreach my $no (@{$DT->{showcase}})
	{
		$salelist.=GetTagImgItemType($no);
		$itemtype=0,next if $itemtype!=-1 && $ITEM[$no]->{type}!=$itemtype;
		$itemtype=$ITEM[$no]->{type};
	}
	$itempro=GetTagImgItemType(0,$itemtype,1)." " if $itemtype;
	my $itemno=$DT->{showcase}[0];
	$salelist.=" ".$ITEM[$itemno]->{name}." \\".$DT->{price}[0] if $itemno;
	
	my $expsum=0;
	foreach(values(%{$DT->{exp}})){$expsum+=$_;}
	$expsum="�y".int($expsum/10)."%�z";
	
	my $job=$JOBTYPE{$DT->{job}};
	$job="�y$job�z" if $job;
	
	$disp.=$TR;
	$disp.=$TDNW.$tdh_rk."<b>".($idx+1)."</b>".$rankupdown."<br>";
	$disp.=    $tdh_pt.$DT->{point};
	$disp.=$TD.GetTagImgShopIcon($DT->{icon}) if $SHOP_ICON_HEADER && !$MOBILE;
	$disp.=$TD.$tdh_nm;
	$disp.=    "<a href=\"shop.cgi?ds=$DT->{id}&$USERPASSURL\">" if !$GUEST_USER;
	$disp.=    GetTagImgGuild($DT->{guild}).$itempro.$job.$DT->{shopname}."[".$DT->{name}."]";
	$disp.=    "</a>" if !$GUEST_USER;
	$disp.=GetTopCountImage($DT->{rankingcount}+0) if $DT->{rankingcount};
	$disp.="<BR>";
	$disp.=    $tdh_pp.GetRankMessage($DT->{rank});
	$disp.=$TDNW.$tdh_ts."\\".$DT->{saletoday};
	$disp.=$TDNW.$tdh_mo.GetMoneyMessage($DT->{money})."<BR>";
	$disp.=    $tdh_ys."\\".$DT->{saleyesterday};
	$disp.=$TDNW.$tdh_cs."\\".($DT->{costyesterday}+0)."<br>";
	$disp.=    $tdh_tx."\\".($DT->{taxyesterday}+0);
	
	$disp.=$TD;
	
	$disp.=$tdh_sc.$salelist;
	
	$disp.="<BR>";
	
	$disp.=$tdh_ex.$expsum;
	$disp.=$tdh_fd."�y".GetTime2HMS($NOW_TIME-$DT->{foundation})."�z";
	$disp.=$tdh_cm.$DT->{comment} if $DT->{comment};
	$disp.=$TRE;
}
$disp.=$TBE;

$disp.=$pagecontrol;
1;
