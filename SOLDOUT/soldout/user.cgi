#! /usr/local/bin/perl
# $Id: user.cgi 106 2004-03-17 13:15:34Z mu $

require './_base.cgi';
require $JCODE_FILE;

GetQuery();

#�R�����g�ύX
if(defined($Q{cmt}))
{
	$comment=jcode::sjis($Q{cmt},$CHAR_SHIFT_JIS&&'sjis');
	OutError('�R�����g�̕������������ł��B') if length($comment)>50;
	$comment=~s/&/&amp;/g;
	$comment=~s/>/&gt;/g;
	$comment=~s/</&lt;/g;
}

#�p�X���[�h�ύX
if(defined($Q{pw1}))
{
	OutError('���݂̃p�X���[�h�����͂���Ă��܂���B') if $Q{pwvrf}eq'';
	OutError('�m�F���͂ƕs��v�̂��ߕύX���~���܂��B') if $Q{pw1}ne$Q{pw2};
	OutError('�ύX�p�X���[�h�����͂���Ă��܂���B') if $Q{pw1}eq'';
	OutError('�p�X���[�h�Ɏg�p�ł��Ȃ�����������܂����̂ŕύX���~���܂��B') if $Q{pw1}=~/[^a-zA-Z0-9_\-]/;
	OutError('�p�X���[�h��12�����܂łł��B') if length($Q{pw1})>12;
}

#�X���܂�
if(defined($Q{cls}))
{
	OutError('���݂̃p�X���[�h�����͂���Ă��܂���B') if $Q{pwvrf}eq'';
	OutError('�X���܂��������ꍇ�� closeshop �Ɠ��͂��Ă��������B') if $Q{cls}ne'closeshop';
}

#�X�ܖ��ύX
if($Q{rename}ne'')
{
	$Q{rename}=jcode::sjis($Q{rename},$CHAR_SHIFT_JIS&&'sjis');
	OutError('���O�E�X���E�p�X���[�h�Ɏg�p�ł��Ȃ��������܂܂�Ă��܂��B') if $Q{rename} =~ /([,:;\t\r\n<>&])/;
	OutError('�X����20�����ȓ��ł��B') if length($Q{rename})>40;
	OutError('�X�����Z�����܂��B') if length($Q{rename})<4;
	OutError('���O�E�X�����󔒂ɂȂ��Ă��邩�A�g�p�s�������g�p����Ă��܂��B') if $Q{rename}=~/^(\s|\x81\x40)+$/;
}

#�M���h���E��
if($Q{guild}ne'')
{
	OutError('����ȃM���h�͑��݂��܂���') if $Q{guild} ne 'leave' && !defined($GUILD{$Q{guild}}->[$GUILDIDX_name]);
}

#�\���s���ύX
if($Q{pagerows}ne'')
{
	$Q{pagerows}=int($Q{pagerows});
	OutError('0�`50�Ŏw�肵�Ă��������B') if $Q{pagerows}<0 || $Q{pagerows}>50;
}

#�T�u�^�C�g���ύX
if($Q{usertitle})
{
	OutError('�ύX����������܂���') if !$USE_USER_TITLE || $DTidx!=0;
	OutError('�T�u�^�C�g�����������܂�') if length $Q{usertitle} > 40;
}

Lock();
DataRead();
CheckUserPass();

#�R�����g�ύX
if(defined($Q{cmt}))
{
	$DT->{comment}=$comment;
	$disp.="�R�����g�X�V���܂���";
}

#�p�X���[�h�ύX
if(defined($Q{pw1}))
{
	VerifyPass();
	$DT->{pass}=$PASSWORD_CRYPT ? crypt($Q{pw1},GetSalt()) : $Q{pw1};
	$disp.="�p�X���[�h�ύX���܂���<BR>�g�b�v�����X�������Ă�������<BR><BR>";
	#$disp.="<A HREF='index.cgi?u=$DT->{name}!$Q{pw1}'>�g�b�v��</A>"; #�Z�L�����e�B�I�ɕs�K��
}

#�X���܂�
if($Q{cls}eq'closeshop')
{
	VerifyPass();
	if(!$MASTER_USER)
	{
		CloseShop($DT->{id},'����X');
		WriteLog(1,0,0,$DT->{shopname}."���X���܂���",1);
		$disp.="�X���܂��̎葱���������������܂���<BR><BR>"
			  ."�{�Q�[���ւ̎Q���A�{���ɂ��肪�Ƃ��������܂���";
	}
	else
	{
		CloseShop($DT->{id},'�Ǖ�');
		$Q{closecmt}="�y".jcode::sjis($Q{closecmt})."�z" if $Q{closecmt}ne'';
		WriteLog(1,0,0,$Q{closecmt}.$DT->{shopname}."�͒Ǖ�����܂���",1);
		$disp.="�Ǖ�����";
	}
	$DTblockip=$DT->{remoteaddr};
}

#�X�ܖ��ύX
if($Q{rename}ne'')
{
	OutError('����������܂���B') if $DT->{money}<200000;
	foreach my $idx (0..$#DT)
	{
		OutError('���ɑ��݂���X���ł��B-> '.$Q{rename}) if $DT[$idx]->{shopname} eq $Q{rename};
	}
	WriteLog(1,0,0,$DT->{shopname}."���u".$Q{rename}."�v�։������܂����B",1);
	$DT->{shopname}=$Q{rename};
	$DT->{money}-=200000;
	$disp.=$DT->{shopname}."�։������܂����B";
}

#�M���h���E��
if($Q{guild}ne'')
{
	OutError('����������܂���B') if $DT->{money}<200000;
	if($DT->{guild}eq'')
	{
		OutError('�ǂ��ɂ�����Ă��܂���') if $Q{guild} eq 'leave';
		
		my $name=$GUILD{$Q{guild}}->[$GUILDIDX_name];
		WriteLog(1,0,0,$DT->{shopname}."���M���h�u".$name."�v�֓���܂����B",1);
		$DT->{guild}=$Q{guild};
		$disp.=$name."�֓���܂����B";
	}
	else
	{
		OutError('���ݏ������Ă���M���h��މ�Ȃ��Ɠ���ł��܂���') if $Q{guild} ne 'leave';
		
		my $name=$GUILD{$DT->{guild}}->[$GUILDIDX_name];
		$name="���U�����M���h" if $name eq '';;
		WriteLog(1,0,0,$DT->{shopname}."���M���h�u".$name."�v����E�ނ��܂����B",1);
		$disp.=$name."����E�ނ��܂����B";
		$DT->{guild}="";
	}
	$DT->{money}-=200000;
}

#�I�v�V�����ݒ�
if($Q{option} eq 'set')
{
	$DT->{options}=0;
	$DT->{options}|=1 if $Q{short_menu} eq 'on';
	$disp.='�Z�k���j���[:'.($DT->{options}&1 ? '�L��' : '����').'<br>';
}

#�T�u�^�C�g���ύX
if($USE_USER_TITLE && $Q{usertitle} && $DTidx==0)
{
	my $msg=$Q{usertitle};
	$msg=$msg eq 'delete' ? '' : EscapeHTML(jcode::sjis($msg,$CHAR_SHIFT_JIS&&'sjis')." by $DT->{shopname}");
	SetTownData('sub_title',$msg);
	$disp.='�T�u�^�C�g����ύX���܂���';
}

DataWrite();
DataCommitOrAbort();
UnLock();

OutHTML('�e��葱��',$disp);
exit;

sub VerifyPass
{
	OutError('���݂̃p�X���[�h�̓��͂��Ԉ���Ă��܂�')
		if !CheckPassword($Q{pwvrf},$DT->{pass}) && $MASTER_PASSWORD ne $Q{pwvrf};
}

