# $Id: inc-html-ownerinfo.cgi 96 2004-03-12 12:25:28Z mu $

if(!$GUEST_USER)
{
	my $tm=$NOW_TIME-$DT->{time};
	if($tm<0)
	{
		$tm=-$tm;
		$tm='�s���\�܂ł��� '.GetTime2HMS($tm);
	}
	else
	{
		$tm=$MAX_STOCK_TIME if $tm>$MAX_STOCK_TIME;
		$tm=GetTime2HMS($tm);
	}
	my $rankmsg=GetRankMessage($DT->{rank});
	
	$disp.=<<STR;
	���X�܏��<BR>
	$TB$TR
	$TD
	RANK ${\($id2idx{$DT->{id}}+1)}$TDE
	$TD�X��:$DT->{shopname}$TDE
	$TD����:\\$DT->{money}$TDE
	$TD������:\\$DT->{moneystock}$TDE
	$TD����:$tm$TDE
	$TRE$TBE
	<HR SIZE=1>
STR
}
1;
