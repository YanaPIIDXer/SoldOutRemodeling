# $Id: inc-html-owner.cgi 96 2004-03-12 12:25:28Z mu $

$disp.="���X�܏��<HR>";
$disp.='�����X�����X����:'.GetTime2FormatTime($DT->{lastlogin}+$EXPIRE_TIME+GetExpireTimeExtend($DT)).'<br>';
my $tm=$NOW_TIME-$DT->{time};
if($tm<0)
{
	$tm=-$tm;
	$tm='�s���\�܂ł��� '.GetTime2HMS($tm);
}else{
	if($tm>$MAX_STOCK_TIME){$tm=$MAX_STOCK_TIME;}
	$tm=GetTime2HMS($tm);
}
my $rankmsg=GetRankMessage($DT->{rank});
my($tax,$taxrate)=GetTaxToday($DT);
if($taxrate)
{
	$taxrate="�ŗ�:$taxrate\%";
}else{
	$taxrate="�Ɛ�";
}

my $expsum=0;
foreach(values(%{$DT->{exp}})){$expsum+=$_;}
$expsum=int($expsum/10)."%";
my $job=$JOBTYPE{$DT->{job}}; $job||='�s��';

if(!$MOBILE)
{
	$disp.=$TB;
	$disp.=$TR.$TD."���O".$TD.$DT->{name}.$TD."�X��".$TD.GetTagImgGuild($DT->{guild}).$DT->{shopname}.$TRE;
	$disp.=$TR.$TD."RANK".$TD.($id2idx{$DT->{id}}+1).$TD."TOP".$TD.($DT->{rankingcount}+0)."�� ".GetTopCountImage($DT->{rankingcount}+0).$TRE;
	$disp.=$TR.$TD."�l�C".$TD.$rankmsg.$TD."����/������".$TD."\\".$DT->{money}."/\\".$DT->{moneystock}.$TRE;
	$disp.=$TR.$TD."��������".$TD."\\".$DT->{saletoday}.$TD."�O������".$TD."\\".$DT->{saleyesterday}.$TRE;
	$disp.=$TR.$TD."�����x��".$TD."\\".$DT->{paytoday}.$TD."�O���x��".$TD."\\".$DT->{payyesterday}.$TRE;
	$disp.=$TR.$TD."��������".$TD.$tm.$TD."�_��".$TD.$DT->{point}.$TRE;
	$disp.=$TR.$TD."�����ێ���<BR><SMALL>(���Z������)</SMALL>".$TD."\\".int($DT->{costtoday})."+\\".$SHOWCASE_COST[$DT->{showcasecount}-1];
	$disp.=    $TD."�O���ێ���".$TD."\\".$DT->{costyesterday}.$TRE;
	$disp.=$TR.$TD."�����ŋ�<BR><SMALL>(���Z������)</SMALL>".$TD."\\".$tax."<br><small>$taxrate</small>".$TD."�O���ŋ�".$TD."\\".($DT->{taxyesterday}+0).$TRE;
	$disp.=$TR.$TD."�x���ϔ��p��".$TD."\\".($DT->{taxtoday}+0).$TD."��{���p�ŗ�".$TD.GetUserTaxRate($DT).'%'.$TRE;
	$disp.=$TR.$TD."�n���x���v".$TD.$expsum;
	$disp.=    $GUILD{$DT->{guild}} ? $TD."�M���h��� <SMALL>�����".($GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/10)."%<br>(���Z������)</SMALL>".$TD.'\\'.int($DT->{saletoday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000) : $TD."�@".$TD."�@";
	$disp.=  $TRE;
	$disp.=$TR.$TD.'�n��'.$TD.GetTime2HMS($NOW_TIME-$DT->{foundation}).$TD.'�E��'.$TD.$job.$TRE;
	$disp.=$TBE;
}
else
{
	$disp.="���O:".$DT->{name}."<BR>";
	$disp.="�X��:".GetTagImgGuild($DT->{guild}).$DT->{shopname}."<BR>";
	$disp.="RANK:".($id2idx{$DT->{id}}+1)."<BR>";
	$disp.="TOP :".($DT->{rankingcount}+0)."��<BR>";
	$disp.="�l�C:".$rankmsg."<BR>";
	$disp.="����:"."\\".$DT->{money}."<BR>";
	$disp.="����:"."\\".$DT->{moneystock}."<BR>";
	$disp.="����:"."\\".$DT->{saletoday}."<BR>";
	$disp.="���:"."\\".int($DT->{saletoday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000)."<BR>" if $DT->{guild} ne '';
	$disp.="�O��:"."\\".$DT->{saleyesterday}."<BR>";
	$disp.="����:"."\\".$DT->{paytoday}."<BR>";
	$disp.="�O��:"."\\".$DT->{payyesterday}."<BR>";
	$disp.="����:"."\\".int($DT->{costtoday})."+\\".$SHOWCASE_COST[$DT->{showcasecount}-1]."<BR>";
	$disp.="�O��:"."\\".$DT->{costyesterday}."<BR>";
	$disp.="�ϐ�:"."\\".($DT->{taxtoday}+0)."<BR>";
	$disp.="����:"."\\".$tax."(".$taxrate.")<BR>";
	$disp.="�O��:"."\\".($DT->{taxyesterday}+0)."<BR>";
	$disp.="����:".$tm."<BR>";
	$disp.="�_��:".$DT->{point}."<BR>";
	$disp.="�n��:".$expsum."<BR>";
	$disp.="�n��:".GetTime2HMS($NOW_TIME-$DT->{foundation})."<BR>";
	$disp.="�E��:".$job."<BR>";
}

1;
