#! /usr/local/bin/perl
# $Id: item-send.cgi 96 2004-03-12 12:25:28Z mu $

$NOMENU=1;
require './_base.cgi';
GetQuery();

Lock();
DataRead();
CheckUserPass();

$itemno=CheckItemNo($Q{item});
$itemname=$ITEM[$itemno]->{name};
$scale=$ITEM[$itemno]->{scale};
$count=CheckCount($Q{cnt1},$Q{cnt2},0,$DT->{item}[$itemno-1]);

OutError('�s���ȗv���ł�') if CheckItemFlag($itemno,'notrash');
OutError('�j�����ʂ��w�肵�Ă�������') if !$count;

#UseTime($TIME_SEND_ITEM);#���ԏ������
$ret=$itemname."��".$count.$scale."�������܂���";
$DT->{item}[$itemno-1]-=$count;
WriteLog(0,$DT->{id},0,$ret,1);
WriteLog(0,0,0,$DT->{shopname}."��".$itemname."�����������悤�ł�",1);

$DTwholestore[$itemno-1]+=$count;
my $limit=0;
foreach $DT (@DT)
	{$limit+=$DT->{item}[$itemno-1];}

my $ITEM=$ITEM[$itemno];
my $limitcount=$ITEM->{wslimit}<0 ? -$ITEM->{wslimit} : int($ITEM->{wslimit}*($#DT+1));

if($limit+$DTwholestore[$itemno-1]>$limitcount)
{
	$limit=$limitcount if $limitcount<$limit;
	$DTwholestore[$itemno-1]=$limitcount-$limit;
}
$DTwholestore[$itemno-1]=0 if $DTwholestore[$itemno-1]<0;

DataWrite();
DataCommitOrAbort();
UnLock();

$disp.=$ret;
OutHTML('�q��',$disp);

