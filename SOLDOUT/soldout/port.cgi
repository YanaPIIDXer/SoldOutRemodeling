#! /usr/local/bin/perl
# $Id: port.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
OutError('�g�p�s�ł�') if !$USE_PORT;

GetQuery();
$NOMENU=1;
$disp.="SOLD OUT �֘A�̊O���T�C�g�ł��B�g�ђ[���ł̉{���͕s�ł��B<BR><BR>";
#$disp.="<a href=\"http://urakanda.virtualave.net/\">�����]�ˑ� (�I�[�N�V����)</a><BR>";

#
# �O�����j���[��L���ɂ���ɂ́A_config.cgi �̐ݒ肪�K�v�ł��B
#
# $disp ��HTML��ǉ�����ƁA�Ǝ��̊O�����j���[���\�z�ł��܂��B
# ���̊O�����j���[����̃����N�ł���΁A�Z�b�V������񓙂��O���T�C�g�֘R��܂���B
#

OutHTML('�O��',$disp);

exit;
