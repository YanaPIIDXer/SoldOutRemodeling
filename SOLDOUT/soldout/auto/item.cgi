# $Id: item.cgi 96 2004-03-12 12:25:28Z mu $

sub CheckShowCaseItem
{
	my($DT,$sc)=@_;
	
	$sc+=0;
	my $itemno=$DT->{showcase}[$showcase];
	$itemno=0 if $itemno && !$DT->{item}[$itemno-1];

	return ($itemno,$DT->{price}[$sc],$DT->{item}[$itemno-1]) if $itemno;

	return (0,0,0);
}

sub CheckItemNo
{
	my($itemno,$DT)=@_;
	$itemno+=0;
	$DT=$main::DT if !$DT;
	
	OutError('����ȃA�C�e���͂Ȃ��ł��B') if $itemno<1 || $itemno>$MAX_ITEM;
	OutError('�A�C�e���̍݌ɂ�����܂���B') if !$DT->{item}[$itemno-1];

	return $itemno;
}

sub GetTagImgItemType
{
	my($itemno,$type,$mode)=@_;
	
	my $ITEM;
	if(!$type)
	{
		return "" if !$itemno;
		$ITEM=$ITEM[$itemno];
		$type=$ITEM->{type};
	}
	
	if(!$MOBILE)
	{
		return qq|<IMG class="s" SRC="$IMAGE_URL/item-typesign$type$IMAGE_EXT">| if $mode==1;
		if($ITEM->{existimage})
		{
			my $filename=$ITEM->{existimage}==1 ? "item-code-$ITEM->{code}" : "item-no-$itemno";
			return qq|<IMG class="|.($mode==2?'il':'i').qq|" SRC="$IMAGE_URL/$filename$IMAGE_EXT">|;
		}
		return qq|<IMG class="i" SRC="$IMAGE_URL/item-type$type$IMAGE_EXT">| if $mode!=2;
		return "";
	}
	
	return "" if $mode==2;
	return $ITEMTYPE[$type].($mode==1?'���X':'').":";
}

#���i���l�ɂ��ŗ�/�ŋ��v�Z
sub GetSaleTax
{
	my($itemno,$itemcnt,$price,$plustaxrate)=@_;
	
	my $taxrate=$ITEM[$itemno]->{price} && $itemcnt ? ($price/$itemcnt/$ITEM[$itemno]->{price}-1) : 0;
	$taxrate=$taxrate**2*5 if $taxrate>0;
	my $taxratedown=1;
	$taxratedown=$taxrate+1,$raxrate=0 if $taxrate<0;
	$taxrate=int(($taxrate+$plustaxrate)*$taxratedown);
	$taxrate=99 if $taxrate>99;
	my $tax=int($price*$taxrate/100);
	
	return ($taxrate,$tax);
}

# ����/���i�ړ����̎��ԏ���v�Z
sub GetTimeDeal
{
	my($price,$itemno,$itemcount)=@_;
	
	if(!$itemno)
	{
		#�����ړ�
		return 0 if !$price;
		return $TIME_SEND_MONEY if !$TIME_SEND_MONEY_PLUS;
		return int($TIME_SEND_MONEY*$price/$TIME_SEND_MONEY_PLUS)+$TIME_SEND_MONEY;
	}
	
	return 0 if !$itemcount;
	
	my $mul=1;
	
	$mul=$ITEM[$itemno]->{price}/($price/$itemcount) if $price && $ITEM[$itemno]->{price};
	$mul=20 if (!$price && $ITEM[$itemno]->{price}) || $mul>20;
	
	return int($TIME_SEND_ITEM*$mul);
}

# ����/���i�ړ����̎��ԏ���
sub UseTimeDeal
{
	my($price,$itemno,$itemcount)=@_;
	
	UseTime(GetTimeDeal($price,$itemno,$itemcount));
}

sub CheckItemFlag
{
	my($itemno,$flagname)=@_;
	
	return 0 if $itemno<0 || $itemno>$MAX_ITEM;
	
	$flagname='s' if $flagname eq 'noshowcase'; # s ��s��
	$flagname='m' if $flagname eq 'nosend';     # m ���t�s��
	$flagname='e' if $flagname eq 'notradeout'; # e �A�o�s��
	$flagname='i' if $flagname eq 'notradein';  # i �A���s��
	$flagname='t' if $flagname eq 'notrash';    # t �j���s��
	$flagname='b' if $flagname eq 'nobuy';      # b �w���s��(���X��I����)
	
	return $ITEM[$itemno]->{flag}=~/$flagname/;
}

1;
