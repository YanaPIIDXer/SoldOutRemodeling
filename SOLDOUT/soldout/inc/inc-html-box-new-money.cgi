# $Id: inc-html-box-new-money.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

$disp.="���X�֔�<HR>";

$Q{price}=0 if $Q{price} eq '';

if($Q{conf} ne '' && $precheckerror eq '')
{
	$disp.=<<"HTML";
	�����m�F<hr>
	����F$DT[$id2idx{$Q{sendmoney}}]->{shopname}<br>
	�^�C�g���F$Q{title}<br>
	���e�F$Q{msg}<br>
	�����z�F\\$Q{price}<br>
	����ԁF${\GetTime2HMS($TIME_SEND_MONEY)}<br>
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=sendmoney VALUE="$Q{sendmoney}">
	<INPUT TYPE=HIDDEN NAME=title VALUE="$Q{title}">
	<INPUT TYPE=HIDDEN NAME=msg VALUE="$Q{msg}">
	<INPUT TYPE=HIDDEN NAME=price VALUE="$Q{price}">
	<INPUT TYPE=SUBMIT NAME=ok VALUE="���M">
	<INPUT TYPE=SUBMIT NAME=ng VALUE="�ĕҏW">
	</FORM>
HTML
#����ԁF${\GetTime2HMS(GetTimeDeal($Q{price}))}<br>
}
else
{
	my $formsend="<OPTION VALUE='-1'>����I��";
	foreach (@DT)
	{
		$formsend.="<OPTION VALUE=\"$_->{id}\"".($Q{sendmoney}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
	}
	
	$disp.=<<"HTML";
	�����i���݂̏����� \\$DT->{money}�j<hr>
	$precheckerror
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	$TB
	$TR$TD����$TD<SELECT NAME=sendmoney>$formsend</SELECT>$TRE
	$TR$TD�^�C�g��$TD<INPUT TYPE=TEXT NAME=title SIZE=50 VALUE="$Q{title}">$TD(20�����ȓ�)$TRE
	$TR$TD���e$TD<INPUT TYPE=TEXT NAME=msg SIZE=50 VALUE="$Q{msg}">$TD(100�����ȓ�)$TRE
	$TR$TD�����z$TD<INPUT TYPE=TEXT NAME=price SIZE=6 VALUE="$Q{price}">�~$TRE
	$TBE
	<INPUT TYPE=HIDDEN NAME=conf VALUE="conf">
	<INPUT TYPE=SUBMIT VALUE="�����m�F"> (����${\GetTime2HMS($TIME_SEND_MONEY)}����)
	</FORM>
	����拑�ۂ����ƁA���̎����͔j������܂��B
HTML
}

1;
