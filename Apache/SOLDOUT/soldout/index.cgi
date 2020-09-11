#! /usr/local/bin/perl
# $Id: index.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
RequireFile('inc-version.cgi');

Turn();

GetQuery();
GetCookie();
SetCookieSession(); # try cookie
DataRead();

$username=$Q{nm} ? $Q{nm} : $COOKIE{USERNAME};
$password=$Q{pw} ? $Q{pw} : $COOKIE{PASSWORD};

$sub_title=$GAME_SUB_TITLE;
if($USE_USER_TITLE)
{
	my $msg=GetTownData('sub_title');
	$sub_title="<p>$msg</p>" if $msg;
}

$disp.=<<"STR";
$GAME_TITLE
$sub_title
$GAME_INFO
<FORM ACTION="main.cgi" $METHOD>
���O<INPUT TYPE=TEXT NAME=nm VALUE="$username">
�p�X���[�h<INPUT TYPE=PASSWORD NAME=pw VALUE="$password">
<INPUT TYPE=CHECKBOX NAME=ck CHECKED>�N�b�L�[�ŕۑ�
<INPUT TYPE=SUBMIT VALUE="�X�֓���">
</FORM>
STR

$DT={};
$DT->{id}=-1;
$GUEST_USER=1;

RequireFile('inc-html-ranking.cgi');
RequireFile('inc-html-period.cgi');

$disp.="<hr>";
if(!$NEW_SHOP_ADMIN)
{
	$disp.=GetTagA('�y�V�K�X�܃I�[�v���z�c��'.($MAX_USER-$DTusercount).'���l',"new.cgi") if $MAX_USER>$DTusercount;
	$disp.='�y�V�K�X�܃I�[�v���z���ݖ����ɂ��V�K�X�܃I�[�v���ł��܂���' if $MAX_USER<=$DTusercount;
}
else
{
	$disp.=qq|�Q�����������͊Ǘ��҂܂ł��₢���킹������|;
}
$disp.="<br>";
if($MOVETOWN_ENABLE)
{
	$disp.='�y�ړ]�X�܎󂯓���z';
	$disp.='�c��'.($MAX_MOVE_USER-$DTusercount).'���l' if $MAX_MOVE_USER>$DTusercount;
	$disp.='���݈ړ]����ł��܂���' if $MAX_MOVE_USER<=$DTusercount;
	$disp.="<br>";
}
$disp.=qq|<HR>�{�T�C�g�̊Ǘ��� <a href="mailto:$ADMIN_EMAIL">$ADMIN_EMAIL</a>|;
$disp.=qq|<hr>SOLD OUT system ver.$VERSION item ver.$ITEM_VERSION|;
$disp.=qq|<br><A HREF="http://mutoys.com/" target="_blank">MUTOYS�� (SOLD OUT �J����)</A>|; # ���̍s�͂Ȃ�ׂ��ύX���Ȃ��ł�������

OutHTML('�g�b�v',$disp);
exit;

sub GetCookie
{
	foreach(split(/\s*;\s*/,$ENV{HTTP_COOKIE}))
	{
		@_=split(/=/);
		$COOKIE{$_[0]}=$_[1];
		next if $_[0] ne 'shop';
		foreach(split(/,/,$_[1]))
		{
			@_=split(/:/);
			$COOKIE{$_[0]}=$_[1];
		}
	}
}
