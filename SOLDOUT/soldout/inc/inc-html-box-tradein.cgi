# $Id: inc-html-box-tradein.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

$disp.="���f��(�A���葱��)<HR>";

CheckTradeProcess();

my %itemcode2idx=();
foreach(0..$MAX_ITEM){$itemcode2idx{$ITEM[$_]->{code}}=$_;}
my($hostcode,$boxno,$itemcode,$itemcnt,$price)=split(/!/,$Q{tradein});
my $itemno=$itemcode2idx{$itemcode};

if($Q{ng} eq '')
{
	$disp.=<<"HTML";
	�A���葱���m�F<hr>
	���i���F$ITEM[$itemno]->{name}<br>
	���ʁF$itemcnt$ITEM[$itemno]->{scale}<br>
	����z�F\\$price<br>
	����ԁF${\GetTime2HMS(GetTimeDeal($price,$itemno,$itemcnt))}<br>
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=tradein VALUE="$Q{tradein}">
	<INPUT TYPE=SUBMIT NAME=ok VALUE="�葱�����s">
	<INPUT TYPE=SUBMIT NAME=ng VALUE="���~">
	</FORM>
	������O�����ŁA���Ԃ��葱���Ɠ����ɏ����܂��B����Ɏ��s�����ꍇ�͑S�z/�S���Ԗ߂��Ă��܂��B
HTML
}
else
{
	$disp.="�A���葱���𒆎~���܂���";
}
1;
