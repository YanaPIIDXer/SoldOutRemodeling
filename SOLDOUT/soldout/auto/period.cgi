# $Id: period.cgi 96 2004-03-12 12:25:28Z mu $

sub TurnPeriod
{
	$PERIOD_MODE=1;
	foreach(keys(%GUILD))
	{
		$GUILD_DATA{$_}->{in}=0;
		$GUILD_DATA{$_}->{out}=0;
	}
	
	if(defined($DT[0]))
	{
		#���̎��_�ł̃g�b�v�̓X��TOP�J�E���^��+1
		$DT[0]->{rankingcount}++;
		
		#�D���Ҕ��\
		my $DT=$DT[0];
		my $count=$DT->{rankingcount}==1 ? "���D��" : $DT->{rankingcount}."�x�ڂ̗D��";
		my $msg="�u�����̗D���X��".$DT->{shopname}."����ł����B".$count."���߂łƂ��������܂��B�v";
		WriteLog(1,0,0,$msg,1);
		
		$msg="�u�_����".$DT->{point}."�_";
		$msg.="�ŁA2�ʂƂ̍���".($DT->{point}-$DT[1]->{point})."�_" if defined($DT[1]);
		$msg.="�ł����B�v";
		WriteLog(1,0,0,$msg,1);
	}
	
	require "$ITEM_DIR/funcupdate.cgi" if $DEFINE_FUNCUPDATE;
	
	#���Z���̃J�X�^������
	UpdateResetBefore() if defined(&UpdateResetBefore);
	
	my $dtcount=0;
	foreach my $DT (@DT)
	{
		#next if !$DT->{status};
		$dtcount++;
		
		#�����L���O&�_���o�b�N�A�b�v
		$DT->{rankingyesterday}=$dtcount;
		$DT->{pointyesterday}=$DT->{point};
	
		#�����ɐŋ��z����
		my($taxtoday)=GetTaxToday($DT);
		
		#����ڍ׏����X�V�E������
		$DT->{profitstock}=int(($DT->{profitstock}*$PROFIT_DAY_COUNT+$DT->{saletoday}-$DT->{paytoday})/($PROFIT_DAY_COUNT+1));
		$DT->{saleyesterday}=$DT->{saletoday};
		$DT->{saletoday}=0;
		$DT->{payyesterday}=$DT->{paytoday};
		$DT->{paytoday}=0;
		$DT->{itemyesterday}=$DT->{itemtoday};
		$DT->{itemtoday}={};
		$DT->{taxyesterday}=$taxtoday+$DT->{taxtoday};
		$DT->{taxtoday}=0;
		
		#�O�̂��ߏ������I�[�o�[�`�F�b�N���s���l�C��
		foreach my $cnt (1..$MAX_ITEM)
		{
			$DT->{item}[$cnt-1]=$ITEM[$cnt]->{limit} if $DT->{item}[$cnt-1]>$ITEM[$cnt]->{limit};
			$DT->{item}[$cnt-1]=int($DT->{item}[$cnt-1]);
		}
		
		#�ێ��������
		my $cost=int($DT->{costtoday});
		$cost+=$SHOWCASE_COST[$DT->{showcasecount}-1];
		$DT->{money}-=$cost;
		$DT->{paytoday}+=$cost;
		
		#�����ɐŋ���������
		$DT->{money}-=$taxtoday;
		#$DT->{paytoday}+=$taxtoday; #�R�����g�A�E�g/�x�����ɓ���Ȃ�
		
		#�M���h���
		if($DT->{guild} ne '')
		{
			my $money=int($DT->{saleyesterday}*$GUILD{$DT->{guild}}->[$GUILDIDX_feerate]/1000);
			EditGuildMoney($DT->{guild},$money);
			$DT->{money}-=$money;
		}
		
		#�M���h�������y�i���e�B
		if($DT->{guild} eq '' && $GUILD_UNATTACH_PENALTY)
		{
			my $money=int($DT->{saleyesterday}*$GUILD_UNATTACH_PENALTY/1000);
			$DT->{money}-=$money;
			WriteLog(2,0,0,$DT->{shopname}."���M���h�������y�i���e�B���󂯂܂����B-\\".$money,1);
		}
		
		$DT->{moneystock}+=$DT->{money},$DT->{money}=0 if $DT->{money}<0;
		$DT->{money}+=$DT->{moneystock},$DT->{moneystock}=0 if $DT->{moneystock}<0;
		
		#�|�Y����
		if($DT->{money}<0)
		{
			CloseShop($DT->{id},'�����s���|�Y');
			WriteLog(1,0,0,$DT->{shopname}."�������s���ɂ��|�Y���܂���",1);
		}
		$DT->{costyesterday}=$cost;
		$DT->{costtoday}=0;
		
		#�n���x���R����
		foreach my $key (keys(%{$DT->{exp}}))
		{
			$DT->{exp}{$key}-=int($DT->{exp}{$key}*$EXP_DOWN_RATE/1000) if $EXP_DOWN_RATE;
			$DT->{exp}{$key}-=$EXP_DOWN_POINT;
			delete $DT->{exp}{$key} if $DT->{exp}{$key}<=0;
		}
	}
	SortDT();
	
	#���Z���̃J�X�^�������i���Z�b�g��j
	UpdateResetAfter() if defined(&UpdateResetAfter);
	
	#�f�[�^�o�b�N�A�b�v($BACKUP�����$BACKUP��)
	mkdir($BACKUP_DIR.$BACKUP,$DIR_PERMISSION) if !(-e $BACKUP_DIR.$BACKUP);
	rename($BACKUP_DIR.$BACKUP,$BACKUP_DIR."_work");
	foreach my $count (reverse(1..$BACKUP-1))
	{
		mkdir($BACKUP_DIR.$count,$DIR_PERMISSION) if !(-e $BACKUP_DIR.$count);
		rename($BACKUP_DIR.$count,$BACKUP_DIR.($count+1));
	}
	rename($BACKUP_DIR."_work",$BACKUP_DIR."1");
	
	foreach my $filetype (@BACKUP_FILES)
	{
		open(IN,GetPath($filetype));
		open(OUT,">".GetPath($BACKUP_DIR."1",$filetype));
		while(<IN>){print OUT $_;}
		close(OUT);
		close(IN);
	}
	
	#�����ȃZ�b�V�����f�[�^(�����؂�)���폜
	opendir(SESS,$SESSION_DIR);
	my @dir=readdir(SESS);
	closedir(SESS);
	my $sessiontimeout=$NOW_TIME-$EXPIRE_TIME;
	
	foreach(map{"$SESSION_DIR/$_"}grep(/^.+\.cgi$/,@dir))
	{
		unlink $_ if (stat($_))[9]<$sessiontimeout; # $EXPIRE_TIME�g���Ȃ���Ώ���
	}
	
	MakeGuildFile();
	
	undef $PERIOD_MODE;
}
1;
