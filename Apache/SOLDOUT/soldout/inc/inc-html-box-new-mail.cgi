# $Id: inc-html-box-new-mail.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

$disp.="���X�֔�<HR>";

$Q{price}=0 if $Q{price} eq '';

if($Q{conf} ne '' && $precheckerror eq '')
{
	$disp.=<<"HTML";
	���b�Z�[�W���M�m�F<hr>
	����F$DT[$id2idx{$Q{sendmail}}]->{shopname}<br>
	�^�C�g���F$Q{title}<br>
	���e�F$Q{msg}<br>
	��񗿁F\\$Q{price}<br>
	${\($Q{price} ? "����ԁF".GetTime2HMS($TIME_SEND_MONEY)."<br>" : "")}
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=sendmail VALUE="$Q{sendmail}">
	<INPUT TYPE=HIDDEN NAME=title VALUE="$Q{title}">
	<INPUT TYPE=HIDDEN NAME=msg VALUE="$Q{msg}">
	<INPUT TYPE=HIDDEN NAME=price VALUE="$Q{price}">
	<INPUT TYPE=SUBMIT NAME=ok VALUE="���M">
	<INPUT TYPE=SUBMIT NAME=ng VALUE="�ĕҏW">
	</FORM>
HTML
}
else
{
	my $formsend="<OPTION VALUE='-1'>����I��";
	foreach (@DT)
	{
		$formsend.="<OPTION VALUE=\"$_->{id}\"".($Q{sendmail}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
	}
	
	$disp.=<<"HTML";
	���b�Z�[�W���M<hr>
	$precheckerror
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	$TB
	$TR$TD����$TD<SELECT NAME=sendmail>$formsend</SELECT>$TRE
	$TR$TD�^�C�g��$TD<INPUT TYPE=TEXT NAME=title SIZE=50 VALUE="$Q{title}">$TD(20�����ȓ�)$TRE
	$TR$TD���e$TD<INPUT TYPE=TEXT NAME=msg SIZE=50 VALUE="$Q{msg}">$TD(100�����ȓ�)$TRE
	$TR$TD���$TD<INPUT TYPE=TEXT NAME=price SIZE=6 VALUE="$Q{price}">�~(��񗿐ݒ莞�̂ݎ���${\GetTime2HMS($TIME_SEND_MONEY)}����)$TRE
	$TBE
	<INPUT TYPE=HIDDEN NAME=conf VALUE="conf">
	<INPUT TYPE=SUBMIT VALUE="���M�m�F">
	</FORM>
	����񗿂�ݒ肷��ƁA���e�{�����ɗ����̒������o���܂��B
HTML
}
1;
