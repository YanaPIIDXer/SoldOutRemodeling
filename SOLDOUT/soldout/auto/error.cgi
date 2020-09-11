# $Id: error.cgi 96 2004-03-12 12:25:28Z mu $

sub OverLoad
{
	print <<"HTML";
Cache-Control: no-cache, must-revalidate
Pragma: no-cache
Content-type: text/html

<html>
<head>
<title>�ߕ���</title>
</head>
<body>
���݃T�[�o�������׏�Ԃł��B
�\\���󂠂�܂��񂪂��΂炭�A�N�Z�X�������킹�Ă��������B<br>
���דx $_[0] CPUs
</body></html>
HTML
	exit;
}

sub OutError
{
	while($LOCKED){UnLock()};
	my %msg=
	(
		"not defined function"=>
			'��`����Ă��Ȃ��֐����Ăяo���܂����B�Ǘ��҂Ɉȉ��̏���A�����Ă��������B<hr>'.
			"not defined function '$_[1]'",
		"busy"=>
			'�A�N�Z�X�����ݍ����Ă���܂��B'.
			'���΂炭�ҋ@������A�g�b�v�y�[�W����蒼���Ă��������B'.
			($AUTO_UNLOCK_TIME*2).'�b�ȏ�o���Ă��ڑ��ł��Ȃ��ꍇ�̓G���[�̉\��������܂��̂�'.
			'�Ǘ��l <a href="mailto:'.$ADMIN_EMAIL.'">'.$ADMIN_EMAIL.'</a> �܂ŘA�������肢���܂��B',
		"no data"=>
			'�Q�[���f�[�^��������܂���ł����B'.
			'�g�b�v����蒼���Ă݂Ă��������B'.
			'���̃��b�Z�[�W�������ꍇ�A�f�[�^�t�@�C�����j�����Ă��邩������܂���B'.
			'�Ǘ��҂ɘA�����I',
		"no user"=>
			'ID�������̓p�X���[�h���Ⴂ�܂��B��'.$_[1],
		"error rename"=>
			'�f�[�^�X�V�Ɏ��s���܂���',
		"timeout"=>
			'�^�C���A�E�g�ł��B�g�b�v�����X�������Ă��������B',
		"bad request"=>
			'�s�����N�G�X�g�ł��B�u���E�U�́u�߂�/�i�ށv���g���Ă���ꍇ�͎g��Ȃ��悤�ɂ��Ă��������B',
		"attack report"=>
			'�O��̃��O�C���ォ��p�X���[�h�F�؎��s��'.$_[1].'�񂠂�܂����B'.
			'�g�Ɋo���������ꍇ�A���҂��ɍU������Ă���\��������܂��̂ŁA'.
			'�p�X���[�h�𐄑�����ɂ������̂ɕύX����Ȃǂ��Ď��q�����肢���܂��B'.
			'�ȉ��͔F�؎��s���̏��ł��B<hr>'.
			'���s��:'.$_[1].'��<br>'.
			'�ŏI���s����:'.GetTime2FormatTime($_[2]).'<br>'.
			'IP�A�h���X:'.$_[3].'<br>'.
			'�u���E�U���:'.$_[4].'<br>'.
			'<hr>���̌x�������x�������悤�ł�����A��L����Y���ĊǗ��҂܂ŘA�������肢���܂��B'.
			'�Ȃ��A���̉�ʂ͓�x�ƕ\������܂���B�K�v�ł���Ίe�����������肢���܂��B'.
			'<hr><a href="index.cgi">[�g�b�v�֖߂�]</a>',
	);
	my $msg=defined $msg{$_[0]} ? $msg{$_[0]} : $_[0];
	OutHTML('ERROR',$msg);
	exit;
}

sub OutErrorNoUser
{
	eval(<<'__function__');
	
	WriteErrorLog(
		join("\t",
			(
				"name=".$Q{nm},
				"pass=".$Q{pw},
				"session=".$Q{ss},
				"query=".$Q{INPUT_DATA},
				"ua=".$ENV{HTTP_USER_AGENT},
				"referer=".$ENV{HTTP_REFERER},
				"accept=".$ENV{HTTP_ACCEPT},
			)
		),
		$LOG_LOGIN_FILE,
	);
	OutError('���O/�p�X���[�h���Ⴄ���A�o�^�������ꂽ�\��������܂� �� \''.$_[0].'\'');
__function__
}

sub WriteErrorLog
{
	eval(<<'__function__');
	my($msg,$file)=@_;
	
	return if !$LOG_SIZE_MAX || $file eq '';
	
	my $fn=GetPath($LOG_DIR,$file);
	rename($fn,GetPath($LOG_DIR,$file."-old")) if (stat($fn))[7]>$LOG_SIZE_MAX;
	open(ERR,">>$fn") or return;
	print ERR
		join("\t",
			(
				$NOW_TIME,
				$ENV{SCRIPT_NAME},
				$ENV{REMOTE_ADDR},
				$ENV{REMOTE_HOST},
				GetTrueIP(),
				$USER,
				$msg,
			)
		)."\n";
	close(ERR);
__function__
}

sub OutErrorBadRequest
{
	OutError('�s�����N�G�X�g�ł��B�u���E�U�́u�߂�/�i�ށv���g���Ă���ꍇ�͎g��Ȃ��悤�ɂ��Ă��������B');
}
sub OutErrorTimeOut
{
	OutError($_[0].'�g�b�v�����X�������Ă��������B');
}

sub OutErrorBlockLogin
{
	OutError('
		���Ȃ���'.$_[0].'�̂��߃A�N�Z�X��������Ă��܂��B
		�v���C���́u�T�C�g���v�u�X���v�u���[�U���v�u�X�ܖ��v��Y���āA�g�b�v�y�[�W�L�ڂ̊Ǘ��҃��[���A�h���X�܂Ń��[���ŘA�����Ă��������B
		���̍ہA�v���o�C�_�̃��[���A�h���X�i�A�J�E���g�j�𗘗p���Ă��������B
		�����̃��[���A�h���X�ihotmail.com���j�ł̘A���͕s�Ƃ��܂��B
	');
}

sub OutErrorBusy
{
	OutError('
		�A�N�Z�X�����ݍ����Ă���܂��B
		���΂炭�ҋ@������A�g�b�v�y�[�W����蒼���Ă��������B
		'.($AUTO_UNLOCK_TIME*2).'
		�b�ȏ�o���Ă��ڑ��ł��Ȃ��ꍇ�̓G���[�̉\��������܂��̂�
		�Ǘ��҂܂ŘA�������肢���܂��B
	');
}

1;
