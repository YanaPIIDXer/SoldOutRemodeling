# $Id: inc-html-showcase.cgi 96 2004-03-12 12:25:28Z mu $

my $showcasecount=$DT->{showcasecount};

$disp.="����I�F����$showcasecount�F�ێ��� \\$SHOWCASE_COST[$showcasecount-1]<HR>";

my $usertaxrate=GetUserTaxRate($DT);

$disp.=$TB;
if(!$MOBILE)
{
	$disp.=$TR;
	$disp.=$TD."�INo";
	$disp.=$TD."���i��";
	$disp.=$TD."���l";
	$disp.=$TD."�W�����i";
	$disp.=$TD."���p��";
	$disp.=$TD."�݌ɐ�";
	$disp.=$TD."�������㐔";
	$disp.=$TD."�O�����㐔";
	$disp.=$TD;
	$disp.=$TRE;
}
else
{
	$tdh_pr{$MOBILE}="���l:";
	$tdh_sp{$MOBILE}="�W��:";
	$tdh_tx{$MOBILE}="����:";
	$tdh_st{$MOBILE}="�݌�:";
	$tdh_ts{$MOBILE}="�{��:";
	$tdh_ys{$MOBILE}="��:";
}

for(my $cnt=0; $cnt<$DT->{showcasecount}; $cnt++)
{
	my $itemno=$DT->{showcase}[$cnt];
	my $ITEM=$ITEM[$itemno];
	my $scale=$ITEM->{scale};
	my $stock=$itemno ? $DT->{item}[$itemno-1]:0;

	$disp.=$TR.$TD."�I".($cnt+1);
	$disp.=$TD;
	$disp.="<A HREF='item.cgi?$USERPASSURL&no=$itemno&sc=".($cnt+1)."&pr=".$DT->{price}[$cnt]."&bk=$MYNAME'>" if $stock;
	$disp.=GetTagImgItemType($itemno).$ITEM->{name};
	$disp.="</A>" if $stock;
	
	if($itemno)
	{
		my($taxrate,$tax)=GetSaleTax($itemno,1,$DT->{price}[$cnt],$usertaxrate);
		$disp.=$TD.$tdh_pr{$MOBILE}."\\".$DT->{price}[$cnt];
		$disp.=$TD.$tdh_sp{$MOBILE}."\\".$ITEM->{price};
		$disp.=$TD.$tdh_tx{$MOBILE}."\\".$tax." (�ŗ�".$taxrate."%)";
		$disp.=$TD.$tdh_st{$MOBILE}.$stock.$scale;
		$disp.=$TD.$tdh_ts{$MOBILE}.($DT->{itemtoday}{$itemno}+0).$scale;
		$disp.=$TD.$tdh_ys{$MOBILE}.($DT->{itemyesterday}{$itemno}+0).$scale;
		$disp.=$TD."<A HREF='showcase-edit.cgi?yen=1&$USERPASSURL&item=0&no=$cnt&bk=sc'>�񒆎~</A>";
	}
	else
	{
		$disp.=$TD.$TD.$TD.$TD.$TD.$TD;
	}
	$disp.=$TRE;
}

$disp.=$TBE;

1;
