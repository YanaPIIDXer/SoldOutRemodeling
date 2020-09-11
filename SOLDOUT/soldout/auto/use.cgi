# $Id: use.cgi 96 2004-03-12 12:25:28Z mu $

sub GetUseItemList
{
	return GetUseItemListSub(@item::USE);
}

sub GetUseItemListSub
{
	my(@USE)=@_;
	foreach my $USE (@USE)
	{
		my $ret=CheckUseItem($USE);
		$USE->{dispok}=1 if $ret==2;
		$USE->{useok}=1 if $ret==1;
	}
	return @USE;
}

sub CheckUseItem
{
	my($USE)=@_;
	my $jobfunc="item::_job_use_$USE->{no}_$DT->{job}_";
	&$jobfunc if defined &$jobfunc;
	
	my $funcbefore=$USE->{functionbefore};
	if($funcbefore)
	{
		my $ret=&{"item::".$funcbefore}($USE);
		return 2 if $ret==2;
		return 0 if $ret==1;
	}
	foreach my $item (@{$USE->{use}})
	{
		return 0 if $DT->{item}[$item->{no}-1]<$item->{count};
	}
	return 1;
}

sub GetUseItem
{
	my($no,@USE)=@_;

	foreach(@USE)
	{
		return $_ if $_->{no}==$no;
	}
	return 0;

}

sub UseItem
{
	my($USE,$count)=@_;
	my $usetime=GetItemUseTime($USE);
	
	#�n���x�s���ō�ƕs�\���ǂ����𔻒�(�s�\�Ȃ�count=0)
	$count=0 if $DT->{exp}{$USE->{itemno}}<$USE->{needexp};
	
	#��p�s����count��␳
	$count=int($DT->{money}/$USE->{money}) if $DT->{money}<$USE->{money}*$count;
	
	#���ԕs����count��␳
	$count=int(($NOW_TIME-$DT->{time})/$usetime) if ($DT->{time}+$usetime* $count)>$NOW_TIME;
	
	#�ޗ��s����count��␳
	foreach my $item (@{$USE->{use}})
	{
		my $itemno=$item->{no};
		my $itemcount=$item->{count}*($item->{proba}==0 ? 1 : $count);
	
		if($DT->{item}[$itemno-1]<$itemcount)
		{
			$count=int($DT->{item}[$itemno-1]/$item->{count});
		}
	}
	
	#count�m��
	$USE->{result}->{count}=$count;
	return if !$count; #count��0�Ȃ玸�s
	
	#���ʗp�ϐ�������
	$USE->{result}->{useitem}=[];
	$USE->{result}->{additem}=[];
	
	#���ԂƂ�������
	UseTime($usetime*$count);
	$DT->{money}-=$USE->{money}*$count;
	$DT->{paytoday}+=$USE->{money}*$count;
	
	#�A�C�e������
	foreach my $item (@{$USE->{use}})
	{
		my $itemno=$item->{no};
		my $itemcount=$item->{proba}<1000 ? 0 : $item->{count}*$count;
		if($item->{proba}>0 && $item->{proba}<1000)
		{
			foreach(1..$item->{count}*$count)
			{
				$itemcount++ if rand(1000)<$item->{proba};
			}
		}
		
		if($itemcount)
		{
			$DT->{item}[$itemno-1]-=$itemcount;
			push(@{$USE->{result}->{useitem}},[$itemno,$itemcount]);
			push(@{$USE->{result}->{usemsg}},$item->{message});
		}
	}
	
	#�A�C�e���擾
	foreach my $item (@{$USE->{result}->{create}})
	{
		my $itemno=$item->{no};
		my $itemcount=$item->{proba}<1000 ? 0 : $item->{count}*$count;
		
		if($item->{proba}>0 && $item->{proba}<1000)
		{
			foreach(1..$item->{count}*$count)
			{
				$itemcount++ if rand(1000)<$item->{proba};
			}
		}
		
		if($itemcount)
		{
			if($itemcount+$DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit})
			{
				$itemcount-=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
				my $trashitem="����ȏ㎝�ĂȂ��̂�".$ITEM[$itemno]->{name}."��".($itemcount).$ITEM[$itemno]->{scale}."�j�����܂���";
				$DTwholestore[$itemno-1]+=$itemcount;
				push(@{$USE->{result}->{trashmsg}},$trashitem);
				$itemcount=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
			}
			$DT->{item}[$itemno-1]+=$itemcount;
			push(@{$USE->{result}->{additem}},[$itemno,$itemcount]);
			push(@{$USE->{result}->{addmsg}},$item->{message});
		}
	}
	
	#�s��݌Ƀ`�F�b�N���␳
	CheckWholeStore();
	
	#�A�C�e���ʊ֐����݃`�F�b�N
	RequireFile('inc-item.cgi');
	my $itemfunc="item::".$USE->{result}->{function};
	$itemfunc="" if !defined(&$itemfunc);
	
	#�A�C�e���ʊ֐��Ăяo��
	if($itemfunc ne '')
	{
		#�ϐ��A�N�Z�X�ȕ։�
		@item::DT=@DT;
		$item::DTS=$DT[$USE->{arg}->{targetidx}]; #target�X
		$item::count=$USE->{result}->{count};
		$item::USE=$USE;
		$item::DT=$DT;
		@item::ITEM=@ITEM;
		
		$USE->{result}->{function_return}=&$itemfunc();
	}

	#�n���x����
	if($USE->{exp})
	{
		#�n���x�v���X
		my $exp=$DT->{exp}->{$USE->{itemno}};
		$USE->{result}->{expold}=$exp+0;
		my $expplus=$USE->{exp}*$USE->{result}->{count};
		$expplus=1000-$exp if $exp+$expplus>1000;
		$DT->{exp}->{$USE->{itemno}}+=$expplus;
		
		#�n���x���v�l�`�F�b�N
		my $expsum=0;
		foreach(values(%{$DT->{exp}}))
		{
			$expsum+=$_;
		}
		#�n���x�I�[�o�[������
		if($LIMIT_EXP>0 && $expsum>$LIMIT_EXP)
		{
			$expsum-=$LIMIT_EXP;
			
			my @key=sort { $DT->{exp}{$a} <=> $DT->{exp}{$b} }keys(%{$DT->{exp}});
			my $keycnt=$#key;
			foreach(@key)
			{
				next if $_==$USE->{itemno};
				my $expdown=int($expsum/$keycnt);
				$expdown=$DT->{exp}{$_} if $DT->{exp}{$_}<$expdown;
				$DT->{exp}{$_}-=$expdown;
				delete $DT->{exp}{$_} if !$DT->{exp}{$_};
				$expsum-=$expdown;
				$keycnt--;
			}
		}
	}
}

sub AddItem
{
	my($DT,$itemno,$count)=@_;
	
	$count=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$count>$ITEM[$itemno]->{limit};

	$DT->{item}[$itemno-1]+=$count;
	
	return $count;
}

sub GetBackUrl
{
	my($urltype,$page,$type)=split(/!/,$Q{bk} || $REFERER);
	return "" if $urltype eq 'none';
	
	my %url=(
		s	=>	"stock.cgi?$USERPASSURL&pg=$page&tp=$type",
		p	=>	"shop.cgi?$USERPASSURL&pg=$page",
		p2	=>	"shop.cgi?$USERPASSURL&pg=$page&t=2&itn=$type",
		m	=>	"shop-master.cgi?$USERPASSURL&pg=$page",
		b	=>	"box.cgi?$USERPASSURL&lpg=$page",
		sc	=>	"showcase.cgi?$USERPASSURL",
	);
	my $url=$url{$urltype}; $url||="$urltype?$USERPASSURL";
	
	return '<A HREF="'.$url.'">[�߂�]</A>';
}

1;
