# $Id: inc-html-buy.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if !$id;
my $usetime=GetTimeDeal($price,$itemno,1);

my $baseprice=$price;
my($guild,$guildrate,$guildmargin)=CheckGuild($DT,$DTS,$baseprice);
my $saleprice=$baseprice+($guild==1 ? -$guildmargin : $guildmargin);
$price=$saleprice;

$disp.="���w��<HR>";

my $ITEM=$ITEM[$itemno];

$disp.=$TB.$TR.$TD."�X��".$TD.GetTagImgGuild($DTS->{guild}).$DTS->{shopname}.$TRE;
$disp.=$TR.$TD."���i".$TD.GetTagImgItemType($itemno).$ITEM->{name}.$TRE;
#$disp.=$TR.$TD.$TD.$ITEM->{info}.$TRE;
$disp.=$TR.$TD."���i".$TD.'@\\'.$baseprice.$TRE;
$disp.=$TR.$TD.("�M���h���������i","�M���h�Ԋ������i")[$guild-1].$TD.'@\\'.$saleprice.$TRE if $guild>0;
$disp.=$TR.$TD."�M���h�����s��".$TD."�M���h�������⏕�͂���܂���".$TRE if $guild==-1;
$disp.=$TR.$TD.'�̔��݌�'.$TD.$stock.$ITEM->{scale}.$TRE;
$disp.=$TR.$TRE;
$disp.=$TR.$TD.'���X�ۗL��'.$TD.($DT->{item}[$itemno-1]+0).$ITEM->{scale}.$TRE;
$disp.=$TBE;

if($DT->{item}[$itemno-1]>=$ITEM->{limit})
	{$disp.='<BR>���̏��i�͂���ȏ�X�g�b�N�ł��܂���<BR>';}
elsif($DT->{money}<$price)
	{$disp.='<BR>����������܂���<BR>';}
elsif(GetStockTime($DT->{time})<$usetime)
	{$disp.='<BR>���Ԃ�����܂���<BR>';}
else
{
	$disp.="<FORM ACTION=\"buy-s.cgi\" $METHOD>";
	$disp.="$USERPASSFORM";
	$disp.="<INPUT TYPE=HIDDEN NAME=bk VALUE=\"$Q{bk}\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=id VALUE=\"$id\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=pr VALUE=\"$price\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=sc VALUE=\"$showcase\">";
	$disp.="<INPUT TYPE=HIDDEN NAME=it VALUE=\"$itemno\">";
	$disp.="��L�� ";
	$limit=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
	$money=$MAX_MONEY;
	$money=int($DT->{money}/$price) if $price;
	$msg{1}=1;
	$msg{10}=10;
	$msg{100}=100;
	$msg{1000}=1000;
	$msg{10000}=10000;
	$msg{$stock}="$stock(�S��)";
	$msg{$limit}="$limit(�q�ɍő�)";
	$msg{$money}="$money(�����ő�)";
	$disp.="<SELECT NAME=num1 SIZE=1>";
	my $oldcnt=0;
	foreach my $cnt (sort { $a <=> $b } (1,10,100,1000,10000,$stock,$limit,$money))
	{
		last if $stock<$cnt || $DT->{money}<$cnt*$price || $cnt>$limit || $cnt==$oldcnt;
	
		$disp.="<OPTION VALUE=\"$cnt\">$msg{$cnt}";
		$oldcnt=$cnt;
	}
	$disp.="</SELECT> $ITEM[$itemno]->{scale}�A�������� ";
	$disp.="<INPUT TYPE=TEXT NAME=num2 SIZE=5> $ITEM[$itemno]->{scale} ";
	$disp.="<INPUT TYPE=SUBMIT VALUE='����'>";
	$disp.="<br>(�����:".GetTime2HMS($usetime).")";
	$disp.="</FORM>";
}

1;
