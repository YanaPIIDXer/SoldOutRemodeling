# $Id: inc-event.cgi 96 2004-03-12 12:25:28Z mu $

package event; #�ύX�s��

######################################################################
# ���C�x���g�p�����֐��F���O��������
# usage:  WriteLog(�d�v�x,�ΏۓX��ID,���b�Z�[�W)
#           �d�v�x     0==��� 1==�d�v 2==���
#           �ΏۓX��ID 0==�S�X�܈� �X��ID==�v���C�x�[�g
#           ���b�Z�[�W ���O���b�Z�[�W
# return: 0 �Œ�
######################################################################
sub WriteLog
{
	my($mode,$from,$msg)=@_;
	main::WriteLog($mode,$from,0,$msg,1);
	return 0;
}

######################################################################
# ���f�o�b�O�p���O��������
# usage: DebugLog(���b�Z�[�W)
#           ���b�Z�[�W ���O���b�Z�[�W
# return: 0 �Œ�
######################################################################
sub DebugLog
{
	my($msg)=@_;
	main::WriteErrorLog($msg,$main::LOG_DEBUG_FILE) if $main::DEBUG_LOG_ENABLE;
	return 0;
}

######################################################################
# ���s��݌ɒ����F�C�x���g���������������f�p
# usage:  stock_le(�A�C�e���ԍ�,��)
# return: 1 �s��̃A�C�e���̍݌ɂ����ȉ��̏ꍇ
#         0 ��L�ȊO
######################################################################
sub stock_le
{
	my($itemno,$count)=@_;
	return 1 if $main::DTwholestore[$itemno-1]<=$count;
	return 0;
}

######################################################################
# ���s��݌ɒ����F�C�x���g���������������f�p
# usage:  stock_ge(�A�C�e���ԍ�,��)
# return: 1 �s��̃A�C�e���̍݌ɂ����ȏ�̏ꍇ
#         0 ��L�ȊO
######################################################################
sub stock_ge
{
	my($itemno,$count)=@_;
	return 1 if $main::DTwholestore[$itemno-1]>=$count;
	return 0;
}

sub GetUserData
{
	return &main::GetUserData;
}
require "$main::ITEM_DIR/funcevent.cgi" if $main::DEFINE_FUNCEVENT;
1;
