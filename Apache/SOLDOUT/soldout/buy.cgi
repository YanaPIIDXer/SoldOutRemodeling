#! /usr/local/bin/perl
# $Id: buy.cgi 96 2004-03-12 12:25:28Z mu $

$NOMENU=1;
require './_base.cgi';

GetQuery();

DataRead();
CheckUserPass();

($id,$showcase,$mstno)=split('!',$Q{buy},3);
$id=int($id+0);
$showcase=int($showcase+0);

if($id==0)
{
	# �s��
	$DTS=GetWholeStore();
}
else
{
	# ��ʓX
	$DTS=$DT[(CheckUserID($id))[1]];
}

$showcase=CheckShowCaseNumber($DTS,$showcase);
($itemno,$price,$stock)=CheckShowCaseItem($DTS,$showcase);

OutError("��I�ɂ͉�������܂���") if !$itemno || !$stock;
OutError("�񂪕ω������悤�ł�") if $itemno!=$mstno;
OutError('���̏��i�͍w���s�ł�') if $id && CheckItemFlag($itemno,'nobuy');

RequireFile('inc-html-ownerinfo.cgi');
RequireFile('inc-html-buy.cgi');

OutHTML(($id==0?'�s��':$DTS->{shopname}).'���d��',$disp);

exit;
