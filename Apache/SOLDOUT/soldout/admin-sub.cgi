#! /usr/local/bin/perl
# $Id: admin-sub.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
require $JCODE_FILE;

GetQuery();

Lock();
DataRead();
CheckUserPass();
OutError('') if !$MASTER_USER || $USER ne 'soldoutadmin';

OutError('���[�U��������܂���') if !defined($name2idx{$Q{user}});
my $DT=$DT[$name2idx{$Q{user}}];

$Q{comment}="�y".jcode::sjis($Q{comment})."�z" if $Q{comment} ne '';
$disp.="$DT->{shopname} [$DT->{name}] $Q{comment} ";

#�d���o�^�����A�N�Z�X�����̌ʑΉ�
if($Q{nocheckip})
{
	$disp.='�d���o�^�`�F�b�N�ΏۊO�Ƃ��܂���',$DT->{nocheckip}=1 if $Q{nocheckip} eq 'nocheck';
	$disp.='�d���o�^�`�F�b�N�ΏۂƂ��܂���',$DT->{nocheckip}='' if $Q{nocheckip} eq 'check';
}

#�A�N�Z�X��������
if($Q{blocklogin})
{
	$Q{blocklogin}=jcode::sjis($Q{blocklogin});
	if($Q{blocklogin} eq 'off')
	{
		$disp.='�A�N�Z�X�������������܂���';
		$DT->{blocklogin}='';
	}
	elsif($Q{blocklogin} ne '')
	{
		$disp.='�A�N�Z�X���������܂���['.$Q{blocklogin}.']';
		$DT->{blocklogin}=$Q{blocklogin};
	}
}

#�Ǖ�
if($Q{closeshop} eq 'closeshop')
{
	CloseShop($DT->{id},'�Ǖ�');
	WriteLog(1,0,0,"$Q{comment}$DT->{shopname}�͒Ǖ�����܂���",1);
	$disp.="�Ǖ�����";
	$DTblockip=$DT->{remoteaddr};
}

#�ܕi���^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{senditem})
{
	my $itemno=$Q{senditem};
	my $ITEM=$ITEM[$itemno];
	my $itemcount=$Q{count};
	$itemcount+=$DT->{item}->[$itemno-1];
	$itemcount=$ITEM->{limit} if $itemcount>$ITEM[$itemno]->{limit};
	$DT->{item}->[$itemno-1]=$itemcount;
	
	WriteLog(2,0,0,"$Q{comment}�Ǘ��l����$DT->{shopname}��$ITEM->{name}�������܂���",1) if $Q{log};
	WriteLog(2,$DT->{id},0,"$Q{comment}�Ǘ��l����$ITEM->{name}��$Q{count}$ITEM->{scale}�����Ă��܂���",1);
	$disp.="$ITEM->{name} $Q{count}$ITEM->{scale} �ܕi���^����";
}

#�܋����^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{sendmoney})
{
	$DT->{money}+=$Q{sendmoney};
	
	WriteLog(2,0,0,"$Q{comment}�Ǘ��l����$DT->{shopname}�֏܋��������܂���",1) if $Q{log};
	WriteLog(2,$DT->{id},0,"$Q{comment}�Ǘ��l����\\$Q{sendmoney}�������Ă��܂���",1);
	$disp.="\\$Q{sendmoney} �܋����^����";
}

#�������Ԏ��^(�f�o�b�O�ɂ��g�p�ł��܂�)
if($Q{sendtime})
{
	$DT->{time}-=$Q{sendtime};
	
	WriteLog(2,0,0,"$Q{comment}�Ǘ��l����$DT->{shopname}�֎������ԁu".GetTime2HMS($Q{sendtime})."�v�������܂���",1) if $Q{log};
	WriteLog(2,$DT->{id},0,"$Q{comment}�Ǘ��l���玝������".GetTime2HMS($Q{sendtime})."�������Ă��܂���",1);
	$disp.=GetTime2HMS($Q{sendtime})." �������Ԏ��^����";
}

#�X�֖��������ύX
if($Q{boxcount} ne '')
{
	$DT->{boxcount}=$Q{boxcount}+0;
	$disp.='�X�֖���������'.($Q{boxcount}+0).'�ɐݒ肵�܂���';
}

DataWrite();
DataCommitOrAbort();
UnLock();

$disp="�s�����������Ƃ��̃p�����[�^�𐳂����I��/�L�q���Ă�������" if $disp eq '';

$NOMENU=1;
$Q{bk}="none";
OutHTML('�Ǘ�',$disp);
exit;
