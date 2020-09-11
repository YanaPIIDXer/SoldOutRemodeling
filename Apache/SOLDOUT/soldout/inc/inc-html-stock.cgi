# $Id: inc-html-stock.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

my $tp=$Q{tp};
my $pg=$Q{pg};

my $DTitem=$DT->{item};
my $DTitemtoday=$DT->{itemtoday};
my $DTitemyesterday=$DT->{itemyesterday};
my $DTexp=$DT->{exp};

GetMarketStatus();

my %showcase=();
my $itemno;
foreach(0..$DT->{showcasecount}-1)
{
	next if !($itemno=$DT->{showcase}[$_]);
	$showcase{$itemno}.="�I".($_+1)."\\".$DT->{price}[$_]." ";
}
$disp.="���q��<HR>";
foreach my $cnt (0..$#ITEMTYPE)
{
	my $name=$ITEMTYPE[$cnt];
	$name="&lt;".$name."&gt;" if $cnt==$tp;
	$name=GetTagImgItemType(0,$cnt).$name if $cnt && !$MOBILE;
	$name="<A HREF=\"$MYNAME?$USERPASSURL&tp=$cnt\">".$name."</A>" if $cnt!=$tp;
	
	$disp.=$name." ";
}
$disp.="<BR>";

my @itemlist=(1..$MAX_ITEM);
@itemlist=grep($ITEM[$_]->{type}==$tp,@itemlist) if $tp;
@itemlist=grep(
	(
		$DTitem->[$_-1] ||
		$DTitemtoday->{$_} ||
		$DTitemyesterday->{$_} ||
		$DTexp->{$_}
	),
	@itemlist
);

if(!@itemlist)
{
	$disp.="<HR>�݌ɂ�����܂���";
}
else
{
	#@itemlist=sort{ $ITEM[$a]->{sort} <=> $ITEM[$b]->{sort} } @itemlist; # ������ŃG���[�ɂȂ邽�߉��L�ő��
	my @sort;
	foreach(@itemlist){$sort[$_]=$ITEM[$_]->{sort}};
	@itemlist=sort{ $sort[$a] <=> $sort[$b] } @itemlist;
	
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($pg,$LIST_PAGE_ROWS,scalar(@itemlist));
	
	$disp.=$TB;
	if($MOBILE)
	{
		$tdh_sp="�W��:";
		$tdh_cs="�ێ�:";
		$tdh_st="�݌�:";
		$tdh_ts="�{��:";
		$tdh_ex="�n��:";
		$tdh_sc="��:";
		$tdh_mp="����:";
		$tdh_mb="����:";
	}
	else
	{
		$disp.=$TR.$TD.
			join($TD,
				qw(
					����
					�W��<br>���i
					�ێ���<br>1��24���ԕ�
					�݌ɐ�<br>/�ő�
					����<br>�O��<br>����
					�n���x
					��
					�̔����i<br>����
					���v����<br>�o�����X
				)
			).$TRE;
	}
	
	foreach my $cnt (map{$itemlist[$_]}($pagestart..$pageend))
	{
		my $ITEM=$ITEM[$cnt];
		
		my $name=GetTagImgItemType($cnt).$ITEM->{name};
		$name="<A HREF=\"item.cgi?no=$cnt&bk=s!$page!$tp&$USERPASSURL\">".$name."</A>" if $DTitem->[$cnt-1];
		
		$disp.=$TR.$TD.
			join($TD,
				$name,
				$tdh_sp."\\".$ITEM->{price},
				$tdh_cs."\\".$ITEM->{cost},
				$tdh_st.$DTitem->[$cnt-1]."/".$ITEM->{limit},
				$tdh_ts.($DTitemtoday->{$cnt} || $DTitemyesterday->{$cnt} ? ($DTitemtoday->{$cnt}||0)."/".($DTitemyesterday->{$cnt}||0) : '�@'),
				$tdh_ex.($DTexp->{$cnt} ? int($DTexp->{$cnt}/10)."%" : '�@'),
				$tdh_sc.($showcase{$cnt}||'�@'),
				$tdh_mp.($ITEM->{marketprice} ? "\\".$ITEM->{marketprice} : '�@'),
			).
			$TDNW.$tdh_mb.GetMarketStatusGraph($ITEM->{uppoint}||=10).
			$TRE;
	}
	$disp.=$TBE;
	
	$disp.=GetPageControl($pageprev,$pagenext,"tp=$tp","",$pagemax,$page);
}

1;
