# $Id: inc-html-moneystock.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

$disp.="����������<HR>";

if($Q{conf}ne'' && $errormsg eq '' && $money>0 && $money<=$DT->{moneystock})
{
	$disp.="�����z�F\\".$money."<br>����� ".GetTime2HMS(GetTimeDeal($money))."<br>";
	$disp.=<<"HTML";
	<FORM ACTION="moneystock.cgi" $METHOD>
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=money VALUE="$money">
	<INPUT TYPE=SUBMIT NAME=ok VALUE="������">
	<INPUT TYPE=SUBMIT VALUE="������">
	</FORM>
HTML
}
else
{
	my $maxmoney=$DT->{moneystock};
	my $usetime=GetTimeDeal($maxmoney)-$TIME_SEND_MONEY;
	my $stocktime=GetStockTime($DT->{time})-$TIME_SEND_MONEY;
	$maxmoney=0 if $stocktime<0;
	$maxmoney=int($maxmoney/$usetime*$stocktime) if $usetime>0 && $stocktime>0 && $stocktime<$usetime;

	$disp.=<<"HTML";
	<FORM ACTION="moneystock.cgi" $METHOD>
	$USERPASSFORM$errormsg
	�����ɂ�������o�����z
	<INPUT TYPE=TEXT NAME=money SIZE=10 VALUE="$money">
	<INPUT TYPE=HIDDEN NAME=conf VALUE="conf">
	<INPUT TYPE=SUBMIT VALUE="���z����">
	</FORM>
	<FORM ACTION="moneystock.cgi" $METHOD>
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=money VALUE="$maxmoney">
	<INPUT TYPE=HIDDEN NAME=conf VALUE="conf">
	<INPUT TYPE=SUBMIT VALUE="�ő�z�w��">
	</FORM>
HTML
	$disp.="(�����:".GetTime2HMS($TIME_SEND_MONEY)."�{\\$TIME_SEND_MONEY_PLUS�ɂ�".GetTime2HMS($TIME_SEND_MONEY).")";
}
1;
