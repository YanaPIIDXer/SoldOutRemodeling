#! /usr/local/bin/perl
# $Id: moneystock.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
GetQuery();

$money=int($Q{money}+0);

if($Q{ok} && $money>0)
{
	Lock();
	DataRead();
	CheckUserPass();
	
	$money=$MAX_MONEY-$DT->{money} if $DT->{money}+$money>$MAX_MONEY;
	$money=$DT->{moneystock} if $money>$DT->{moneystock};
	my $usetime=GetTimeDeal($money);
	OutError('���Ԃ�����܂���') if GetStockTime($DT->{time})<$usetime;
	
	$DT->{money}+=$money;
	$DT->{moneystock}-=$money;
	
	UseTimeDeal($money);

	my $ret="\\".$money."�������܂���";
	$disp.=$ret;
	WriteLog(0,$DT->{id},0,$ret,1);
	
	DataWrite();
	DataCommitOrAbort();
	UnLock();
}
else
{
	DataRead();
	CheckUserPass();
	$errormsg ="";
	$errormsg.='���z���s���ł�<br>' if $money<0;
	$errormsg.='���z���������܂�<br>' if $money>$DT->{moneystock};
	my $usetime=GetTimeDeal($money);
	$errormsg.='���Ԃ�����܂���<br>' if GetStockTime($DT->{time})<$usetime;
	RequireFile('inc-html-moneystock.cgi');
}

OutHTML('��������',$disp);
