#! /usr/local/bin/perl
# $Id: buy-s.cgi 96 2004-03-12 12:25:28Z mu $

$NOMENU=1;
require './_base.cgi';

GetQuery();

$id=int($Q{id}+0);
$showcase=int($Q{sc}+0);
$itemno=int($Q{it}+0);
$price=int($Q{pr}+0);
$num=int(($Q{num2} ? $Q{num2} : $Q{num1})+0);


Lock();
DataRead();
CheckUserPass();

if($id==0)
{
	# �s��
	$DTS=GetWholeStore();
	$DTS->{_wholestore_}=1;
}
else
{
	# ��ʓX
	OutError('�X�I��������������܂���') if !defined($id2idx{$id});
	$DTS=$DT[$id2idx{$id}];
}
OutError('�����̓X���甃���C�ł����H') if $DT==$DTS;
CheckShowCaseNumber($DTS,$showcase);
CheckItemNo($itemno,$DTS);
OutError('���̏��i�͍w���s�ł�') if $id && CheckItemFlag($itemno,'nobuy');

my $baseprice=$DTS->{price}[$showcase];
my($guild,$guildrate,$guildmargin)=CheckGuild($DT,$DTS,$baseprice);
my $saleprice=$baseprice+($guild==1 ? -$guildmargin : $guildmargin);

if($itemno!= $DTS->{showcase}[$showcase]
|| $price != $saleprice
|| !$DTS->{item}[$itemno-1]
)
{
	OutError('���i�≿�i���ω������悤�ł�');
}

$num=$DTS->{item}[$itemno-1] if $DTS->{item}[$itemno-1]<$num;

if($num+$DT->{item}[$itemno-1]>$ITEM[$itemno]->{limit})
{
	$num=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1];
	$num=0 if $num<0;
}
$num=int($DT->{money}/$price) if $DT->{money}<$num*$price;
$num=0 if $num<0;

OutError('��₩���ł����H') if !$num;

#UseTime($TIME_SHOPPING);
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if !$id;

my $usetime=GetTimeDeal($baseprice*$num,$itemno,$num);
UseTime($usetime);

my($taxrate,$tax)=GetSaleTax($itemno,$num,$baseprice*$num,GetUserTaxRate($DTS));

$DTS->{item}[$itemno-1]-=$num;
$DTS->{itemtoday}{$itemno}+=$num;
$DT->{item}[$itemno-1]+=$num;
$DTS->{moneystock}+=$num*$baseprice-$tax;
$DT->{money}-=$num*$price;
$DTS->{saletoday}+=$num*$baseprice;
$DT->{paytoday}+=$num*$price;
$DTS->{taxtoday}+=$tax;

EditGuildMoney($DT->{guild} ,-$guildmargin*$num) if $guild==1;
EditGuildMoney($DTS->{guild}, $guildmargin*$num) if $guild==2;



#����؂ꎞ�̐l�CDOWN(����X��) �����M���h�̏ꍇ��SKIP
if($DTS->{item}[$itemno-1]==0 && $guild!=1 && $guild!=-1)
{
	my $rankdown+=($DTS->{rank}/100)**3/1000; #�l�C�ɉ����ă_�E��
	#$rankdown+=70*4/($nowranking+3); #�����L���O�ɉ����ă_�E��

	if($rankdown<1 && $rankdown>0)
		{$rankdown=1 if rand(1/$rankdown)<1;}
	$DTS->{rank}-=int($rankdown);
	$DTS->{rank}=0 if $DTS->{rank}<0;
}

my $ret=$DTS->{shopname}."���".$ITEM[$itemno]->{name}."��".$num.$ITEM[$itemno]->{scale}."\@\\".$price."(�v\\".($price*$num).")�ɂĎd���܂���".
        "/".GetTime2HMS($usetime)."����";
$ret.="/".('�M���h������','�M���h�Ԋ���')[$guild-1].'@\\'.$guildmargin if $guild>0;
$ret.="/�M���h�������̕⏕������܂���ł���" if $guild==-1;
WriteLog(0,$DT->{id},0,$ret,1);

@item::DT=@DT;
$item::DT=$DT;
@item::ITEM=@ITEM;
$item::ITEM=$ITEM;
$item::BUY={
	dt		=>	$DT,
	dts		=>	$DTS,
	whole	=>	$DTS->{_wholestore_},
	item	=>	$ITEM[$itemno],
	itemno	=>	$itemno,
	num		=>	$num,
	price	=>	$price,
	baseprice=>	$baseprice,
	tax		=>	$tax,
	guild	=>	$guild,
	guildmargin	=>	$guildmargin,
};
RequireFile("inc-item.cgi");
require "$ITEM_DIR/funcbuy.cgi" if $DEFINE_FUNCBUY;

if($ITEM[$itemno]->{funcbuy})
{
	#@@item funcb ����
	my $item=$ITEM[$itemno];
	my $file="$ITEM_DIR/item-b/$item->{no}$FILE_EXT";
	my $func="item::".$item->{funcsale};
	my $funcexists=defined &$func;
	require $file if -e $file;
	&$func($item::BUY);
	undef &$func if !$funcexists;
	delete $INC{$file};
	undef @item::DT;
	undef $item::DT;
	undef @item::ITEM;
	undef $item::ITEM;
}

SetWholeStore($DTS) if $id==0;

WriteGuildData() if $guild>0;
DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$ret."<HR><A HREF=\"stock.cgi?$USERPASSURL\">[�q�ɂ�]</A>";

OutHTML('�d����',$disp);
