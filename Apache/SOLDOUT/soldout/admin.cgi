#! /usr/local/bin/perl
# ���T�[�o�̐ݒ�ɏ]���ĕύX���Ă��������B
# ���̃t�@�C���̃p�[�~�b�V������755(or705or700)�ł��B
# $Id: admin.cgi 96 2004-03-12 12:25:28Z mu $

BEGIN{$SIG{__WARN__}=$SIG{__DIE__}=sub{$incdir=$INCLUDE_DIR; $incdir||="./inc"; require "$incdir/inc-error.cgi"; die($_[0]);};}
print "Set-Cookie: SESSION=-check-cookie-!".time().";\n";

$MYNAME=$ENV{SCRIPT_NAME};
$MYNAME =~s/^.*\///;

open(IN,$MYNAME); $myfirstline=<IN>; $myfirstline=~s/[\r\n]//g; close(IN);
@log=();

($MYDIR,$MYNAME)=($ENV{SCRIPT_NAME}=~/^.*\/([^\/]+)\/([^\/]+)$/); # ���t�@�C����/�f�B���N�g����
require './_config.cgi';

push(@BACKUP_FILES,
	(
		$BBS_FILE,
		$CHAT_FILE,
		$GLOBAL_MSG_FILE,
		(map{$GLOBAL_MSG_FILE.'-'.$_}keys %GMSG_CATEGORY_NAME),
		$LOG_FILE.'-s0',
		$LOG_FILE.'-s1',
		$LOG_FILE.'-s2',
		$BOX_FILE,
		$PERIOD_FILE,
		$GUILDBAL_FILE,
		$DATA_FILE,
	)
);

GetQuery();

OutError('�Ǘ��҃p�X���[�h���ݒ肳��Ă��܂���') if $MASTER_PASSWORD eq '';
OutError('�Ǘ��҃��[���A�h���X���ݒ肳��Ă��܂���') if $ADMIN_EMAIL eq '';
OutError('�X�R�[�h���ݒ肳��Ă��܂���') if ($MOVETOWN_ENABLE || $TRADE_ENABLE) && !$TOWN_CODE;
OutError('$DATA_DIR �̐ݒ�s�ǁA�������́A$DATA_DIR �f�B���N�g�����쐬����Ă��܂���') if !-e $DATA_DIR;
OutError('$SESSION_DIR $TEMP_DIR $LOG_DIR $BACKUP_DIR $SUBDATA_DIR �ӂ�̐ݒ肪�ُ�ł�') if $SESSION_DIR eq '' || $TEMP_DIR eq '' || $LOG_DIR eq '' || $BACKUP_DIR eq '' || $SUBDATA_DIR eq '';

sub OutError
{
	print "Cache-Control: no-cache, must-revalidate\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html; charset=Shift_JIS\n\n";
	print "<HTML><HEAD><TITLE>�Ǘ����j���[</TITLE></HEAD>";
	print "<BODY>";
	print $_[0]."<br>";
	print '<font color=red><b>readme.html���̐��������Q�Ƃ��Đ������ݒ肵�ĉ�����</b></font>' if !$_[1];
	print qq|<FORM ACTION="$MYNAME" METHOD="POST"><INPUT TYPE=HIDDEN NAME=admin VALUE="$Q{admin}">|;
	print qq|<INPUT TYPE="SUBMIT" VALUE="�Ǘ����j���[�֖߂�"></FORM>|;
	print "</BODY>";
	print "</HTML>";
	exit;
}

$checkdatadir=' �f�B���N�g�� '.$DATA_DIR.' �̃p�[�~�b�V�������������Ă�������';

if($Q{admin} ne $MASTER_PASSWORD)
{
	$disp.=<<"HTML";
	<FORM ACTION="$MYNAME" METHOD="POST">
	�Ǘ��҃p�X���[�h <INPUT TYPE=PASSWORD NAME=admin>
	<INPUT TYPE=SUBMIT VALUE="�Ǘ����j���[��">
	</FORM>
HTML
}
elsif($Q{init})
{
	CheckLock();
	#�e��f�B���N�g�����_�~�[index.html �쐬
	foreach my $dir ($DATA_DIR,$SESSION_DIR,$TEMP_DIR,$LOG_DIR,$SUBDATA_DIR,$BACKUP_DIR)
	{
		if(!-d $dir)
		{
			if(mkdir($dir,$DIR_PERMISSION))
				{push(@log,'�f�B���N�g�� '.$dir.' ���쐬���܂���');}
			else
			{
				push(@log,'�f�B���N�g�� '.$dir.' �͍쐬�o���܂���ł���');
				push(@log,' �ݒ�����������A�蓮�ō쐬���Ă�������');
			}
		}
		if(!-e "$dir/index.html")
		{
			if(open(OUT,">$dir/index.html"))
			{
				print OUT "<html></html>";
				close(OUT);
				push(@log,'�f�B���N�g�� '.$dir.' �փ_�~�[��index.html���쐬���܂���');
			}
			else
			{
				push(@log,'�f�B���N�g�� '.$dir.' �ւ̃_�~�[index.html�쐬�Ɏ��s���܂���');
				push(@log,' �f�B���N�g�� '.$dir.' �̃p�[�~�b�V�������������Ă�������');
			}
		}
	}
	
	#���b�N�t�@�C���쐬
	if(!GetFileList($DATA_DIR,"^$LOCK_FILE"))
	{
		if(open(DATA,">$DATA_DIR/$LOCK_FILE"))
		{
			print DATA '���b�N�t�@�C���ł��B�폜���Ă͂����܂���B';
			close(DATA);
			push(@log,'���b�N�t�@�C�����쐬���܂���');
		}
		else
		{
			push(@log,'���b�N�t�@�C���̍쐬�Ɏ��s���܂���');
		}
	}
	
	#�V�K�Q�[���f�[�^�쐬
	if(!-e "$DATA_DIR/$DATA_FILE$FILE_EXT")
	{
		if(open(DATA,">$DATA_DIR/$DATA_FILE$FILE_EXT"))
		{
			print DATA time()."\n100000,100\n\n\n//\n"; #�l��10000�ŏ�����
			close(DATA);
			unlink(map{"$DATA_DIR/$_$FILE_EXT"}grep($_ ne $DATA_FILE,@BACKUP_FILES)); #�֘A�t�@�C��������������
			push(@log,'�Q�[���f�[�^��V�K�쐬���܂���');
		}
		else
			{push(@log,'�Q�[���f�[�^�̐V�K�쐬�Ɏ��s���܂���',$checkdatadir);}
	}
	
	#�ŏI�X�V���������p�t�@�C���쐬
	MakeFile("$DATA_DIR/$LASTTIME_FILE$FILE_EXT",'�ŏI�X�V���������p�t�@�C��','');
	#�M���h��`�t�@�C���x�[�X�쐬
	MakeFile("$DATA_DIR/$GUILD_FILE$FILE_EXT",'�M���h��`�t�@�C��','1;');
	
	sub MakeFile
	{
		if(!-e $_[0])
		{
			if(open(DATA,">$_[0]"))
			{
				print DATA $_[2];
				close(DATA);
				utime(1,1,$_[0]);
				push(@log,$_[1].'���쐬���܂���');
			}
			else
				{push(@log,$_[1].'�쐬�Ɏ��s���܂���',$checkdatadir);}
		}
	}
	push(@log,'������/�C���̕K�v�͂���܂���ł���') if !scalar(@log);
}
elsif($Q{uninit})
{
	CheckLock();
	#data�ȉ��S�폜
	delete_dir($DATA_DIR);
	
	sub delete_dir
	{
		my($dir,$owndelete)=@_;
		
		return if !-d $dir;
		
		opendir(DIR,$dir);
		my @filelist=grep(!/^\.\.?$/,readdir(DIR));
		closedir(DIR);
		foreach my $file (@filelist)
		{
			$file="$dir/$file";
			if(-f $file)
			{
				if(unlink($file))
					{push(@log,$file.' ���폜���܂���');}
				else
					{push(@log,' '.$file.' �̍폜�Ɏ��s���܂���');}
			}
			delete_dir($file,1) if -d $file;
		}
		if($owndelete)
		{
			if(rmdir($dir))
				{push(@log,'�f�B���N�g�� '.$dir.' ���폜���܂���');}
			else
				{push(@log,' �f�B���N�g��'.$dir.' �̍폜�Ɏ��s���܂���');}
		}
	}
	push(@log,'�폜���ׂ��f�[�^������܂���ł���') if !scalar(@log);
}
elsif($Q{mentemode})
{
	if($Q{mentemode}eq'on')
	{
		if(-d "$DATA_DIR/lock")
			{push(@log,'���݃����e���[�h�ł�');}
		elsif(mkdir("$DATA_DIR/lock",$DIR_PERMISSION))
			{push(@log,'�����e���[�h�ɓ���܂���');}
		else
			{push(@log,'�����e���[�h�Ɉڍs�ł��܂���ł���',$checkdatadir);}
	}
	elsif($Q{mentemode}eq'off')
	{
		if(!-d "$DATA_DIR/lock")
			{push(@log,'���݃����e���[�h�ł͂���܂���');}
		elsif(rmdir("$DATA_DIR/lock"))
			{push(@log,'�����e���[�h���������܂���');}
		else
			{push(@log,'�����e���[�h�̉����Ɏ��s���܂���',$checkdatadir);}
	}
}
elsif($Q{backup})
{
	CheckLock();
	#�o�b�N�A�b�v�������ɕ���
	my @files=map{"$_$FILE_EXT"}@BACKUP_FILES;
	my @errorfiles=grep(!-e $_,map{"$Q{backup}/$_"}@files);
	
	if(scalar(@errorfiles))
	{
		push(@log,map{$_.' �����݂��܂���ł���'}@errorfiles);
		push(@log,'�o�b�N�A�b�v�f�[�^���s���S�Ȃ̂ŏ����𒆎~���܂���');
	}
	else
	{
		my $time=(stat("$Q{backup}/$DATA_FILE$FILE_EXT"))[9];
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d",$y+1900,$m+1,$d,$h,$min);
		
		foreach my $file (@files)
		{
			my $inok=open(IN,"$Q{backup}/$file");
			my $outok=open(OUT,">$DATA_DIR/$file");
			if($inok && $outok)
			{
				my @data=<IN>;
				close(IN);
				if($file eq $DATA_FILE.$FILE_EXT)
				{
					#data.cgi�̏ꍇ�͍X�V���������݂�
					$data[0]=time()."\n";
					push(@log,'�ŏI�X�V���������݂ɐݒ肵�܂���');
				}
				if($file eq $LOG_FILE."-s0".$FILE_EXT || $file eq $PERIOD_FILE.$FILE_EXT)
				{
					#period.cgi��log-s0.cgi�̏ꍇ�̓o�b�N�A�b�v�����A�i�E���X��t��
					unshift(@data,time().",1,0,0,�o�b�N�A�b�v�f�[�^�����̂���[$timestr]���_�ɖ߂�܂���\n");
				}
				print OUT @data;
				close(OUT);
				push(@log,$file.' �̕����ɐ������܂���');
			}
			else
			{
				close(IN) if $inok;
				push(@log,$file.' �̕����Ɏ��s���܂���',' �ēx�������s���Ă�������');
			}
		}
	}
}
elsif($Q{settime} || $Q{tlsec} ne '')
{
	CheckLock();
	my $time=$Q{settime};
	$Q{tlyear}-=1900 if $Q{tlyear}>=2000;
	if(!scalar(grep($_ eq '',($Q{tlsec},$Q{tlmin},$Q{tlhour},$Q{tlday},$Q{tlmon},$Q{tlyear}))))
	{
		$time=0;
		eval(<<"EVALCODE");
			require "timelocal.pl";
			$time=timegm($Q{tlsec},$Q{tlmin},$Q{tlhour},$Q{tlday},$Q{tlmon}-1,$Q{tlyear})-$TZ_JST;
EVALCODE
		push(@log,'timelocal.pl �͎g�p�s�ł�') if !$time;
	}
	if(!$time)
	{
		push(@log,'���t�����ݒ肪�s���ł�');
	}
	elsif(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
		my @data=<IN>;
		close(IN);
		$data[0]=$time."\n";
		open(OUT,">$DATA_DIR/$DATA_FILE$FILE_EXT");
		print OUT @data;
		close(OUT);
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d:%02d",$y+1900,$m+1,$d,$h,$min,$s);
		push(@log,'�ŏI�X�V������['.$timestr.']�ɐݒ肵�܂���');
	}
	else
	{
		push(@log,'�f�[�^�t�@�C����ύX�o���܂���ł���');
	}
}
elsif($Q{setscript} && $Q{"1stline"})
{
	CheckLock();
	opendir(DIR,".");
	my @filelist=grep(/^[a-z].+\.cgi$/,readdir(DIR));
	close(DIR);
	my $headline=$Q{"1stline"};
	my $modcount=0;
	foreach my $file (@filelist)
	{
		my $filedate=(stat($file))[9];
		open(IN,$file);
		my @data=<IN>;
		close(IN);
		if($data[0]=~/^\s*#!\s*.+\/perl/)
		{
			$data[0]=$headline."\n";
			if(open(OUT,">$file"))
			{
				print OUT @data;
				close(OUT);
				utime($filedate,$filedate,$file);
				push(@log,$file.' �̃w�b�_�� ['.$headline.'] �ɕύX���܂���');
				$modcount++;
			}
			else
			{
				push(@log,$file.' �̃w�b�_�ύX�Ɏ��s���܂���');
				push(@log,' '.$file.' �̃p�[�~�b�V������ 777 �ɕύX���Ă���ēx���s���Ă�������');
			}
		}
	}
	push(@log,'�w�b�_�����ύX���������܂���');
	push(@log,' �p�[�~�b�V�����͓K�؂Ȑݒ�ɖ߂��Ă����Ă�������');
}
elsif($Q{errorreset})
{
	unlink("$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT");
	push(@log,'�G���[�J�E���g�����Z�b�g���܂���');
}
else
{
	if(-e "$DATA_DIR/$LASTTIME_FILE$FILE_EXT")
	{
		my $init=' �K�v�ɉ����ď�����/�o�b�N�A�b�v������Ƃ��s���Ă�������';
		
		push(@log,' ���i�f�[�^���쐬���Ă�������') if !-e $ITEM_DIR;
		
		push(@log,'���݃����e���[�h�ɂ��A�Q�[���̐i�s���~�܂��Ă��܂�') if -e "./lock" or -e "$DATA_DIR/lock";
		push(@log,'�Q�[���f�[�^���j�����Ă��܂�',$init) if !-e "$DATA_DIR/$DATA_FILE$FILE_EXT";
		push(@log,'�ŏI�X�V���������p�t�@�C�����j�����Ă��܂�',$init) if !-e "$DATA_DIR/$LASTTIME_FILE$FILE_EXT";
		push(@log,'�M���h��`�t�@�C�����j�����Ă��܂�',$init) if !-e "$DATA_DIR/$GUILD_FILE$FILE_EXT";
		
		push(@log,'���b�N�t�@�C�����j�����Ă��܂�',$init) if !GetFileList($DATA_DIR,"^$LOCK_FILE");
		foreach my $dir ($SESSION_DIR,$TEMP_DIR,$LOG_DIR,$SUBDATA_DIR,$BACKUP_DIR)
		{
			push(@log,$dir.' ���j���������͑��݂��܂���',$init) if !-e $dir;
		}
	}
	else
	{
		push(@log,' ���������s���Ă�������');
	}
	
	my $errorcount=(-s "$DATA_DIR/$ERROR_COUNT_FILE$FILE_EXT")+0;
	
	my $backupselect=qq|<option value="" selected>�����������o�b�N�A�b�v��I�����Ă�������|;
	my $backupbasedir=$BACKUP_DIR;
	$backupbasedir=~s/\/([^\/]*)$//;
	foreach(GetFileList($backupbasedir,"^$1"))
	{
		my $file=$_;
		my $time=(stat("$file/$DATA_FILE$FILE_EXT"))[9];
		next if !$time;
		my($s,$min,$h,$d,$m,$y)=gmtime($time+$TZ_JST);
		my $timestr=sprintf("%04d-%02d-%02d %02d:%02d",$y+1900,$m+1,$d,$h,$min);
		$backupselect.=qq|<option value="$_">$timestr|;
	}
	
	my $userselect=qq|<option value="" selected>���[�U��I�����Ă�������|;
	if(open(IN,"$DATA_DIR/$DATA_FILE$FILE_EXT"))
	{
		while(<IN>){s/[\r\n]//g; last if $_ eq '//';}
		my @data=<IN>;
		close(IN);
		if(scalar(@data))
		{
			for(my $idx=0; $idx<$#data; $idx+=2)
			{
				@_=split(/,/,$data[$idx],5);
				
				$userselect.=qq|<option value="$_[2]">$_[2] : $_[3]|;
			}
		}
	}
	
	require "$ITEM_DIR/item.cgi" if -e "$ITEM_DIR/item.cgi";
	
	$disp.="<table><tr valign=\"top\"><td>";
	$disp.="<table bgcolor=\"#eeeeee\">";
	$disp.="<tr><td>perl version</td><td>$]</td></tr>";
	$disp.="<tr><th>�p�[�~�b�V������</th></tr>";
	foreach('.',$DATA_DIR,$INCLUDE_DIR,$AUTOLOAD_DIR,$CUSTOM_DIR,$TOWN_DIR,$GUILD_DIR,"_config.cgi",$MYNAME,"makeitem.cgi")
	{
		$disp.="<tr><td>".$_."<td>".substr(sprintf("%o",(stat($_))[2]),-3,3)."</tr>";
	}
	$disp.="</table>";
	
	$disp.=<<"HTML";
	<td>
	<table><tr>
	<td colspan="4">
	��{�Ǘ�/����Ǘ��@�\\�ȊO�̓����e���[�h�ł�������ł��܂���B
	</tr>
	<tr>
	<td>
	<br>
	��{�Ǘ��@�\\
	</tr>
	<tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="bbs.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�f����:�Ǘ��l���[�h">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="chat.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="��˒[:�Ǘ��l���[�h">
	</FORM>
	</tr>
	<tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="counter.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�����J�E���^">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�����o�[���X�g"><br>
	<INPUT TYPE="CHECKBOX" NAME=host>�z�X�g��������(�\\���x)
	</FORM>
	</tr>
	<tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=log VALUE=".">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�e�탍�O�{��">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="index.cgi" METHOD="POST">
	<INPUT TYPE="SUBMIT" VALUE="�Q�[��TOP">
	</FORM>
	<tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=errorreset VALUE="on">
	<INPUT TYPE="SUBMIT" VALUE="�G���[�J�E���g���Z�b�g[����$errorcount]">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="gmsg.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�L��f����:�Ǘ��l���[�h">
	</FORM>
	</tr>
	<tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=towndata VALUE="look">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�X�f�[�^���X�g"><br>
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=editbbs VALUE="bbs">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�f���n�Ǘ�">
	</FORM>
	</tr>
	</table>
	</tr></table>
	<br>
	�����ݒ��f�[�^�X�V�̂��߂̋@�\\
	<br>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mentemode VALUE="on">
	<INPUT TYPE="SUBMIT" VALUE="�����e���[�h�Ɉڍs">
	</FORM>
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=mentemode VALUE="off">
	<INPUT TYPE="SUBMIT" VALUE="�����e���[�h������">
	</FORM>
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=init VALUE="init">
	<INPUT TYPE="SUBMIT" VALUE="������/�j���C��"><br>
	</FORM>
	<td>
	<FORM ACTION="makeitem.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���i�f�[�^����/�X�V">
	</FORM>
	</tr></table>
	<br>
	����ȏ����ݒ�
	<br>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=setscript VALUE="on">
	<INPUT TYPE="SUBMIT" VALUE="�X�N���v�g�����Z�b�e�B���O"><br>
	<INPUT TYPE="TEXT" NAME=1stline VALUE="$myfirstline" size="50">���X�N���v�g��1�s�ڂ��w��<br>
	<INPUT TYPE="TEXT" NAME=admin VALUE="">���Ǘ��҃p�X���[�h<br>
	���X�N���v�g��1�s�ڂ��ꊇ�ŕύX���܂��B<br>soldout �f�B���N�g���̑S�ẴX�N���v�g�̃p�[�~�b�V������777�Ɏ蓮�ݒ肵�Ă�����s���Ă��������B
	</FORM>
	</tr></table>
	<br>
	����Ǘ��@�\\
	<br>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="new.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�V�K�X�܃I�[�v��">
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="main.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�ܓ��X"><br>
	<SELECT NAME=nm>$userselect</SELECT><BR>
	���{�l���Ǘ��l�Ɠ����ɓ��X����Əd�����O�C���ƂȂ�A�ǂ��炩�����O�A�E�g�������܂�
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="user.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=pwvrf VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�܃p�X���[�h�ύX"><br>
	<SELECT NAME=nm>$userselect</SELECT><BR>
	<INPUT TYPE="TEXT"   NAME=pw1 VALUE="">���V�p�X���[�h<BR>
	<INPUT TYPE="TEXT"   NAME=pw2 VALUE="">���V�p�X���[�h�m�F<BR>
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�ܕX"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<INPUT TYPE="TEXT"   NAME=comment VALUE="">���폜�R�����g<BR>
	<INPUT TYPE="TEXT"   NAME=closeshop VALUE="">���m�F�̂��� closeshop �Ɠ��͂��Ă�������<BR>
	</FORM>
	</tr></table>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�ܕi���^"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<INPUT TYPE="CHECKBOX" NAME=log>���ŋ߂̏o�����Ō��\\����<BR>
	<INPUT TYPE="TEXT"   NAME=comment VALUE="">���R�����g(�C��)<BR>
	<SELECT NAME=senditem>${\join("",map{"<option value=\"$_\">$ITEM[$_]->{name}"}(0..$MAX_ITEM))}</SELECT>���ܕi<br>
	<INPUT TYPE="TEXT"   NAME=count VALUE="1">����<br>
	�����ڑq�ɂ֑���܂��B
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�܋����^"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<INPUT TYPE="CHECKBOX" NAME=log>���ŋ߂̏o�����Ō��\\����<BR>
	<INPUT TYPE="TEXT"   NAME=comment VALUE="">���R�����g(�C��)<BR>
	<INPUT TYPE="TEXT"   NAME=sendmoney VALUE="0">���܋��z<br>
	�����ځu�����v�̕��֑���܂��B
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�������Ԏ��^"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<INPUT TYPE="CHECKBOX" NAME=log>���ŋ߂̏o�����Ō��\\����<BR>
	<INPUT TYPE="TEXT"   NAME=comment VALUE="">���R�����g(�C��)<BR>
	<INPUT TYPE="TEXT"   NAME=sendtime VALUE="0">�����^����(�b�P��)<br>
	��1��=60�b 1����=3600�b 1��=24����=86400�b �ł��B
	</FORM>
	</tr></table>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="���[�U�[�X�ܓ���"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<INPUT TYPE="TEXT"   NAME=blocklogin VALUE="">���������R�i'off'�Ɠ��͂œ�������:'mark'�Ɠ��͂Ń}�[�N���O(���O�C���������O)�Ώہj<BR>
	���[�U�ʂɓ��X������(����)���܂��B�������[�U�[�ւ̕\\���́u���Ȃ���[�������R]�̂��߃A�N�Z�X��������Ă��܂��B�v�ƂȂ�܂��B
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="����IP�A�h���X�d���o�^�`�F�b�N"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<SELECT NAME=nocheckip><option value="check">�`�F�b�N�L��<option value="nocheck">�`�F�b�N����</SELECT><BR>
	IP �A�h���X�� USER AGENT �����̃��[�U�Əd�������ꍇ�A�����I�ɃA�N�Z�X���������邩�ǂ����̐ݒ�ł��B
	�`�F�b�N�L��Ŏ��������L���A�`�F�b�N�����Ŗ����ƂȂ�܂��B
	�V���J�X���̓`�F�b�N�L��ɂȂ��Ă��܂��B�A�������������[�U�̂݃`�F�b�N�����ɂ��邱�Ƃœ��X���ʂɋ��ł��܂��B
	�Ȃ��A���ʂȏꍇ�������A���̐ݒ�͓X�܈ړ]����Ɓu�`�F�b�N�L��v�ɖ߂�܂��B�ʂ̃T�C�g�ɂ͈����p����܂���B
	</FORM>
	</tr></table>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=u VALUE="soldoutadmin!$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�X�֖��������ύX"><br>
	<SELECT NAME=user>$userselect</SELECT><BR>
	<INPUT TYPE="TEXT" NAME=boxcount>���蓮�ݒ肷��\\����(0�`)<br>
	�X�֖��������̕\\�������ۂƍ���Ȃ��ꍇ�Ɏ蓮�ŕύX�ł��܂��B
	�������A�\\���������ۂƍ���Ȃ��Ƃ����󋵂ُ͈�ł��̂ŁA���{�I�ɉ��炩�̌���(�G���[)������Ǝv���܂��B
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=nanclean VALUE="clean">
	<INPUT TYPE="SUBMIT" VALUE="NaN����"><br>
	NaN�Ƃ�������Ȑ��l(?)�ɉ������ꂽ�f�[�^��0�ɒu�������ăQ�[���𑱍s�o����悤�ɂ��܂��B
	�������A�u�����s���ɂ��X�v�u�X�܃X�e�[�^�X�ُ̈�v�u�s��̏������v���̕���p������܂��̂ŁA�������������B
	</FORM>
	</tr></table>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=targz VALUE="make">
	<INPUT TYPE="SUBMIT" VALUE="�o�b�N�A�b�v�_�E�����[�h"><br>
	$DATA_DIR ������ $SUBDATA_DIR �� .tar.gz ���k���A�_�E�����[�h���܂��B<br>
	���v�T�[�o���R�}���h tar
	</FORM>
	<td>
	<FORM TARGET="_blank" ACTION="admin-sub2.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=nm VALUE="soldoutadmin">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}">
	<INPUT TYPE="HIDDEN" NAME=usercheck VALUE="make">
	<INPUT TYPE="SUBMIT" VALUE="�d�����[�U�`�F�b�N�p�f�[�^����"><br>
	$SESSION_DIR �� $DATA_DIR/$IP_FILE$FILE_EXT �� .tar.gz ���k���A�_�E�����[�h���܂��B<br>
	���v�T�[�o���R�}���h tar
	</FORM>
	</tr></table>
	<br>
	�ŏI�X�V�����ύX
	<br>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="SUBMIT" VALUE="�Q�[�����̍ŏI�X�V������ύX����"><br>
	<INPUT TYPE="TEXT" NAME=settime VALUE="${\time()}">���ŏI����(1970/1/1 0:00 ����̕b��)<br>
	<INPUT TYPE="TEXT" NAME=tlyear SIZE=5 VALUE="">/
	<INPUT TYPE="TEXT" NAME=tlmon SIZE=5 VALUE="">/
	<INPUT TYPE="TEXT" NAME=tlday SIZE=5 VALUE=""> 
	<INPUT TYPE="TEXT" NAME=tlhour SIZE=5 VALUE="">:
	<INPUT TYPE="TEXT" NAME=tlmin SIZE=5 VALUE="">:
	<INPUT TYPE="TEXT" NAME=tlsec SIZE=5 VALUE="">�� timelocal.pl ���g����ꍇ�̂݁u����/��/�� ��:��:�b�v�ŕ\\�L��<br>
	<INPUT TYPE="PASSWORD" NAME=admin VALUE="">���Ǘ��҃p�X���[�h<br>
	���ŏI�����ɂ́u���݂̎�����\\���b���v���f�t�H���g�œ��͂���Ă��܂��B
	</FORM>
	</tr></table>
	<br>
	�o�b�N�A�b�v����
	<br>
	<table><tr bgcolor="#eeeeee" valign="top">
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="SUBMIT" VALUE="�o�b�N�A�b�v�𕜌�����"><br>
	<SELECT NAME=backup>$backupselect</SELECT><br>
	<INPUT TYPE="PASSWORD" NAME=admin VALUE="">���Ǘ��҃p�X���[�h<br>
	</FORM>
	</tr></table>
	<br>
	�A���C���X�g�[���p<br>
	�戵�ɂ͏\\���C��t���Ă��������B
	<br>
	<table><tr bgcolor="#eeeeee" valign="top">
	<!--
	<td>
	<FORM ACTION="makeitem.cgi" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=pw VALUE="$Q{admin}!delete">
	<INPUT TYPE="SUBMIT" VALUE="���i�f�[�^�폜">
	</FORM>
	-->
	<td>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=uninit VALUE="delete">
	<INPUT TYPE="SUBMIT" VALUE="�S�f�[�^�폜"><br>
	<INPUT TYPE="PASSWORD" NAME=admin VALUE="">���Ǘ��҃p�X���[�h<br>
	</FORM>
	����܂ł̃Q�[���f�[�^/�֘A�f�B���N�g�����S�č폜����܂��B
	</tr></table>


HTML
}

print "Cache-Control: no-cache, must-revalidate\n";
print "Pragma: no-cache\n";
print "Content-type: text/html; charset=Shift_JIS\n\n";
print "<HTML><HEAD><TITLE>�Ǘ����j���[</TITLE></HEAD>";
print "<BODY>";
foreach(@log)
{
	$_="<b>$_</b>" if substr($_,0,1) eq ' ';
	print $_."<br>";
}
print "<hr>" if scalar(@log) && $disp ne '';
print $disp;
print <<"HTML" if scalar(@log);
	<HR>
	<FORM ACTION="$MYNAME" METHOD="POST">
	<INPUT TYPE="HIDDEN" NAME=admin VALUE="$Q{admin}">
	<INPUT TYPE="SUBMIT" VALUE="�Ǘ����j���[�֖߂�">
	</FORM>
HTML
print "</BODY>";
print "</HTML>";
exit;

sub GetQuery
{
	my($q,@q,$key,$val);
	$q="";
	
	if($ENV{'REQUEST_METHOD'} eq "POST")
	{
		read(STDIN,$q,$ENV{'CONTENT_LENGTH'});
	}
	$q.="&".$ENV{'QUERY_STRING'};

	@q=split(/&/,$q);
	foreach (@q)
	{
		($key,$val)=split(/=/);
		$val =~ tr/\?/ /;
		$val =~ tr/+/ /;
		$val =~ s/\t/ /g;
		$val =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("H2",$1)/eg;
		$val =~ s/"/ /g;
		$val =~ s/'/ /g;
		$val =~ s/,/ /g;
		$val =~ s/[\r\n]//g;
		$Q{$key}=$val;
	}
	if($Q{u} ne '')
	{
		$Q{nm}="";
		$Q{pw}="";
		$Q{ss}="";
		($Q{nm},$Q{pw},$Q{ss})=split(/[!:]/,$Q{u},3);
	}
}

sub CheckLock
{
	return if -e "./lock" or -e "$DATA_DIR/lock";
	OutError('���̑���̓����e���[�h�ł����s���܂���','noerror');
}

sub GetFileList
{
	opendir(DIR,$_[0]);
	my @list=map{$_[0]."/".$_}grep(/$_[1]/ && !/^\.\.?$/,readdir(DIR));
	closedir(DIR);
	
	return @list;
}

