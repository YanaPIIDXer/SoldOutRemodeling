# $Id: inc-html-other.cgi 106 2004-03-17 13:15:34Z mu $

RequireFile('inc-html-ownerinfo.cgi');

$disp.="���e��葱��<HR>";

$disp.=<<STR;
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
�R�����g
<INPUT TYPE=TEXT NAME=cmt SIZE=50 VALUE="$DT->{comment}">
<INPUT TYPE=SUBMIT VALUE="�ύX����">
</FORM>
STR

$disp.=<<STR;
<HR>
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
�M���h����/�E��(��p\\200000)
<INPUT TYPE=TEXT NAME=guild VALUE="$DT->{guild}">
<INPUT TYPE=SUBMIT VALUE="����"><br>
����F${\(GetMenuTag("guild","�M���h�R�[�h"))}�����<br>
�E�ށF�uleave�v�Ɠ���
</FORM>
STR

$disp.=<<STR;
<HR>
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
�X�ܖ��ύX(������p\\200000)
<INPUT TYPE=TEXT NAME=rename SIZE=40 VALUE="">
<INPUT TYPE=SUBMIT VALUE="��������">
</FORM>
STR

if($USE_USER_TITLE && $DTidx==0)
{
	$disp.=<<STR;
<HR>
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
�T�u�^�C�g���ύX(�S�p20�����ȓ�:HTML�s��)
<INPUT TYPE=TEXT NAME=usertitle SIZE=40 VALUE="">
<INPUT TYPE=SUBMIT VALUE="�ύX����">
</FORM>
�������_�Ńg�b�v�̓X�܂ɂ̂ݗ^�����錠���ł��B<br>
���T�u�^�C�g���̍폜�� delete �Ɠ��͂��Ă��������B
STR
}

$disp.=<<STR;
<HR>
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
<INPUT TYPE=HIDDEN NAME="option" value="set">
�I�v�V����<br>
<INPUT TYPE=CHECKBOX NAME=short_menu VALUE="on"${\($DT->{options}&1 ? ' checked' : '')}>�Z�k���j���[<br>
<INPUT TYPE=SUBMIT VALUE="�ݒ肷��">
</FORM>
STR

$disp.=<<STR;
<HR>
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
�p�X���[�h�ύX<br>
<INPUT TYPE=TEXT NAME=pwvrf SIZE=10 VALUE="">���݂̃p�X���[�h<br>
<INPUT TYPE=TEXT NAME=pw1 SIZE=10 VALUE="">�V�����p�X���[�h<br>
<INPUT TYPE=TEXT NAME=pw2 SIZE=10 VALUE="">�m�F<br>
<INPUT TYPE=SUBMIT VALUE="�ύX����">
</FORM>
STR

$disp.=<<STR;
<HR>
<FORM ACTION="user.cgi" $METHOD>
$USERPASSFORM
�X���܂�(�X)<BR>
<INPUT TYPE=TEXT NAME=pwvrf SIZE=10 VALUE="">���݂̃p�X���[�h<br>
<INPUT TYPE=TEXT NAME=cls SIZE=10 VALUE="">�m�F�̂��߁A closeshop �Ɖp�������œ��͂��Ă�������<br>
<INPUT TYPE=SUBMIT VALUE="�X���܂�����">
</FORM>
STR

1;
