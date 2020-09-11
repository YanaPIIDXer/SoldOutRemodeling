#! /usr/local/bin/perl
# $Id: new.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
require $JCODE_FILE;
GetQuery();

DataRead();

if($Q{admin} ne $MASTER_PASSWORD)
{
	OutError('�V�K�X�ܓo�^����������܂���') if $NEW_SHOP_ADMIN;
	OutError('���Ȃ��͌��ݓo�^��������Ă��܂�') if $NEW_SHOP_BLOCKIP && GetTrueIP() eq $DTblockip;
	OutError('�o�X�L�[���[�h������������܂���') if $NEW_SHOP_KEYWORD && $Q{sname} && $Q{newkey} ne $NEW_SHOP_KEYWORD;
	checkMaxUser();
}


if($Q{sname}.$Q{name}.$Q{pass1}.$Q{pass2})
{
	$Q{name}=jcode::sjis($Q{name},$CHAR_SHIFT_JIS&&'sjis');
	$Q{sname}=jcode::sjis($Q{sname},$CHAR_SHIFT_JIS&&'sjis');

	if(($Q{sname}.$Q{name}.$Q{pass1}.$Q{pass2}) =~ /([,:;\t\r\n<>&])/
	|| ($Q{pass1}.$Q{pass2}.$Q{name}) =~ /([^A-Za-z0-9_\-])/
	|| $Q{name} eq 'soldoutadmin'
	|| CheckNGName($Q{sname})
	)
	{
		OutError('���O�E�X���E�p�X���[�h�Ɏg�p�ł��Ȃ�'.
		         '�������܂܂�Ă��܂��B');
	}
	if(!$Q{sname} || !$Q{name} || !$Q{pass1} || !$Q{pass2})
	{
		OutError('���O�E�X���E�p�X���[�h����͂��Ă��������B');
	}
	if($Q{sname}=~/^(\s|\x81\x40)+$/ || $Q{name}=~/^(\s|\x81\x40)+$/)
	{
		OutError('���O�E�X�����󔒂ɂȂ��Ă��邩�A�g�p�s�������g�p����Ă��܂��B');
	}
	if($Q{pass1} ne $Q{pass2})
	{
		OutError('�m�F�p�X���[�h������Ă��܂��B');
	}
	if(length($Q{sname})<4)
	{
		OutError('�X���̕����������Ȃ��ł��B');
	}
	if(length($Q{name})>12 || length($Q{sname})>20
	|| length($Q{pass1})>12 || length($Q{pass2})>12)
	{
		OutError('���O(12����)�E�X��(�S�p10����)�E�p�X���[�h(12����)�̕������������ł��B');
	}
	
	Lock();
	DataRead();
	checkMaxUser() if $Q{admin} ne $MASTER_PASSWORD;
	OutError('���ɑ��݂��閼�O�ł��B-> '.$Q{name}) if $name2pass{$Q{name}};
	
	foreach $idx (0..$#DT)
	{
		OutError('���ɑ��݂���X���ł��B-> '.$Q{sname}) if $DT[$idx]->{shopname} eq $Q{sname};
	}
	
	$idx=$DTusercount;
	$DTlasttime=$NOW_TIME if !$idx;
	$DT[$idx]={};
	$DT=$DT[$idx];
	$DT->{status}	    =1;
	$DT->{id}           =$DTnextid;
	$DT->{lastlogin}    =$NOW_TIME;
	$DT->{name}         =$Q{name};
	$DT->{shopname}     =$Q{sname};
	$DT->{pass}         =$PASSWORD_CRYPT ? crypt($Q{pass1},GetSalt()) : $Q{pass1};
	$DT->{money}        =100000;
	$DT->{moneystock}   =0;
	$DT->{time}         =$NOW_TIME-12*60*60;
	$DT->{rank}         =5010;
	$DT->{saleyesterday}=0;
	$DT->{saletoday}    =0;
	$DT->{costtoday}    =0;
	$DT->{costyesterday}=0;
	$DT->{paytoday}     =0;
	$DT->{payyesterday} =0;
	$DT->{showcasecount}=1;
	$DT->{itemyesterday}={};
	$DT->{itemtoday}	={};
	$DT->{remoteaddr}   =GetTrueIP();
	$DT->{rankingyesterday}='';
	$DT->{taxtoday}     =0;
	$DT->{taxyesterday} =0;
	$DT->{foundation}   =$NOW_TIME;
	foreach $cnt (0..$DT->{showcasecount}-1)
	{
		$DT->{showcase}[$cnt]=0;
		$DT->{price}[$cnt]=0;
	}
	foreach $cnt (0..$MAX_ITEM-1)
	{
		$DT->{item}[$cnt]=0;
	}
	
	$DTblockip=$DT->{remoteaddr};
	
	require "$ITEM_DIR/funcnew.cgi" if $DEFINE_FUNCNEW;
	WriteLog(1,0,0,$Q{sname}."���V���J�X���܂���",1) if !$DEFINE_FUNCNEW || !$DEFINE_FUNCNEW_NOLOG;
	
	DataWrite();
	DataCommitOrAbort();
	UnLock();
	
	OutHTML
	(
		'�o�^�I��',
		"���O:$Q{name}<BR>�X��:$Q{sname}<BR>�p�X���[�h:$Q{pass1}<BR><BR>".
		"��L�ɂēo�^���܂����B<BR><BR>".
		"����ł́A���y���݉������B<BR><BR>".
		"���߂Ă̕��́A���j���[�́u�o�c����v����ʂ育���������B<BR><BR>".
		"<A HREF=\"index.cgi?u=$Q{name}!$Q{pass1}\">�Q�[���X�^�[�g</A><BR><BR>".
		"���g�ђ[���̏ꍇ�A��L�����N�Ɉړ���A�u�b�N�}�[�N���Ă����ƃp�X���[�h���͂̎�Ԃ��Ȃ��܂��B".
		"�������A�u�b�N�}�[�N�Ƀp�X���[�h��񂪋L�^����܂��̂ŁA���ӂ��Ă��������B"
	);
	exit;
}

$disp.="�c��".($MAX_USER-$DTusercount)."���l<hr>";

$disp.=<<"HTML";
<FORM ACTION="$MYNAME" $METHOD>
<INPUT TYPE=HIDDEN NAME=admin VALUE="$Q{admin}">
���O <INPUT TYPE=TEXT NAME=name> ���p�p���̂�<BR>
�X�� <INPUT TYPE=TEXT NAME=sname> ���p�S�pOK('��"��,�͋󔒂ɂȂ�܂�)<BR>
�p�X���[�h <INPUT TYPE=PASSWORD NAME=pass1> ���p�p���̂�<BR>
�p�X���[�h�m�F�̂��߂�����x <INPUT TYPE=PASSWORD NAME=pass2><BR>
HTML
if($NEW_SHOP_KEYWORD)
{
	$disp.=<<"HTML";
�o�X�L�[���[�h <INPUT TYPE=TEXT NAME=newkey> �o�X����ɂ͏o�X�L�[���[�h���K�v�ł�(������@�̓T�C�g���ɈႢ�܂�)<BR>
HTML
}
$disp.=<<"HTML";
<INPUT TYPE=SUBMIT VALUE="�o�^">
</FORM>
<hr>
<a target="_blank" href="help.cgi?p=10">���[��(�K��)</a>���ʃE�B���h�E�ŊJ���܂�
<hr>
<a target="_blank" href="help.cgi?p=11">�Z�L�����e�B�ɂ��Ă̏ڍ�</a>���ʃE�B���h�E�ŊJ���܂�<br><br>
�p�X���[�h�ɂ͖�����΂�Ă��\\��Ȃ����̂����g���������B
��΂Ƀv���o�C�_�ڑ��p�⃁�[���A�J�E���g�p�Ȃǂ̏d�v�ȃp�X���[�h�Ɠ������͎̂g��Ȃ��ł��������B
�΂�Ă��{�Q�[���ȊO�ɂ͑��Q���Ȃ��p�X���[�h�ł��肢���܂��B
HTML

OutHTML('�V�K�X�܊J�X',$disp);
exit;

sub checkMaxUser
{
	OutError('�\���󂠂�܂��񂪁A���݋󂫓X�܂�����܂���B<BR>�󂭂̂����҂����������B')
		if $DTusercount>=$MAX_USER;
}

sub CheckNGName
{
	my($sname)=@_;

	return scalar(grep(index($sname,$_)!=-1,@NG_SHOP_NAME));
}
