# $Id: trade.cgi 96 2004-03-12 12:25:28Z mu $

# �f�Պ֌W�̎��ɓǂݍ���

sub CheckTradeProcess
{
	my $fn=GetPath($TRADE_LOCK_FILE);
	return if !-e $fn;
	
	if((stat($fn))[9]<$NOW_TIME-60*30)
	{
		#30���ȏ�̃��b�N�ُ͈�ƌ��Ȃ�����
		Lock();
		unlink($fn) if (stat($fn))[9]<$NOW_TIME-60*30; #���ɉ�������Ă���\�����`�F�b�N�����
		UnLock();
	}
	OutError('�������f�ՑD�����`���Ă��܂��̂ŗA�o���葱���͍s���܂���');
}

#�T�C�g�֐ŗ��v�Z
sub GetTradeTaxRate
{
	my $tradeinout=$DTTradeOut-$DTTradeIn;
	my $sitetaxrate=0;
	$sitetaxrate=int($tradeinout/200000) if $tradeinout>0;
	$sitetaxrate=50 if $sitetaxrate>50;

	return $sitetaxrate;
}

1;
