# $Id: inc-html-box-new-item.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

my $usertaxrate=GetUserTaxRate($DT);
my $sitetaxrate=($Q{senditem}==1 ? GetTradeTaxRate():0);

my($taxrate,$tax)=GetSaleTax($Q{itemno},$Q{itemcnt},$Q{price}*($Q{unit}?$Q{itemcnt}:1),$usertaxrate+$sitetaxrate);

$disp.="���X�֔�<HR>";

$Q{price}=0 if $Q{price} eq '';
$Q{itemcnt}=1  if $Q{itemcnt} eq '';
$price=$Q{price}*($Q{unit}?$Q{itemcnt}:1);

if($Q{conf} ne '' && $precheckerror eq '')
{
	$disp.=<<"HTML";
	���i���t�m�F<hr>
	����F${\(GetID2UserName($Q{senditem}))[0]}<br>
	���e�F$Q{msg}<br>
	���i���F$ITEM[$Q{itemno}]->{name}<br>
	���ʁF$Q{itemcnt}$ITEM[$Q{itemno}]->{scale}<br>
	����z�F\\$Q{price}${\($Q{unit}?"�~".$Q{itemcnt}:"")}
	${\($tax?"�@���p�ŁF\\$tax�@�ŗ��F$taxrate%":"")}
	${\($Q{senditem}==1?"�@�萔���F\\".int($price/10):"")}
	<BR>
	���t���ԁF${\GetTime2HMS($TIME_SEND_ITEM)}<br>
	����̎�掞��(�\\�z)�F${\GetTime2HMS(GetTimeDeal($price,$Q{itemno},$Q{itemcnt}))} <br>��<b>�y�m�F�I�z</b><br>
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	<INPUT TYPE=HIDDEN NAME=senditem VALUE="$Q{senditem}">
	<INPUT TYPE=HIDDEN NAME=title VALUE="$Q{title}">
	<INPUT TYPE=HIDDEN NAME=msg VALUE="$Q{msg}">
	<INPUT TYPE=HIDDEN NAME=price VALUE="$Q{price}">
	<INPUT TYPE=HIDDEN NAME=itemno VALUE="$Q{itemno}">
	<INPUT TYPE=HIDDEN NAME=itemcnt VALUE="$Q{itemcnt}">
	<INPUT TYPE=HIDDEN NAME=unit VALUE="$Q{unit}">
	<INPUT TYPE=SUBMIT NAME=ok VALUE="���M">
	<INPUT TYPE=SUBMIT NAME=ng VALUE="�ĕҏW">
	</FORM>
HTML
	#�^�C�g���F$Q{title}<br>
}
else
{
	my $formsend="<OPTION VALUE='-1'>����I��";
	$formsend.="<OPTION VALUE='1'>�A�o(�f��)" if $TRADE_ENABLE;
 	foreach (@DT)
	{
		$formsend.="<OPTION VALUE=\"$_->{id}\"".($Q{senditem}==$_->{id}?' SELECTED':'').">$_->{shopname}" if $DT->{id}!=$_->{id};
	}
	
	my @sort;
	foreach(1..$MAX_ITEM){$sort[$_]=$ITEM[$_]->{sort}};
	my @itemlist=sort { $sort[$a] <=> $sort[$b] } (1..$MAX_ITEM);
	my $formitem="";
	foreach my $idx (@itemlist)
	{
		my $cnt=$DT->{item}[$idx-1];
		my $price=$ITEM[$idx]->{price};
		my $deny_send =CheckItemFlag($idx,'nosend')     ? '[�~���t]' : '';
		my $deny_trade=CheckItemFlag($idx,'notradeout') ? '[�~�A�o]' : '';
		$formitem.="<OPTION VALUE=\"$idx\"".($Q{itemno}==$idx?' SELECTED':'').">$deny_send$deny_trade$ITEM[$idx]->{name}($cnt/\\$price)" if $cnt;
	}
	
	$disp.=<<"HTML";
	���i���t<hr>
	$precheckerror
	<FORM ACTION="$MYNAME" $METHOD>
	$USERPASSFORM
	$TB
	$TR$TD����$TD<SELECT NAME=senditem>$formsend</SELECT>$TRE
	$TR$TD���e$TD<INPUT TYPE=TEXT NAME=msg SIZE=50 VALUE="$Q{msg}">$TD(100�����ȓ�)$TRE
	$TR$TD���i(�݌ɐ�)$TD<SELECT NAME=itemno>$formitem</SELECT>$TRE
	$TR$TD����$TD<INPUT TYPE=TEXT NAME=itemcnt VALUE="$Q{itemcnt}">$TRE
	$TR$TD����z$TD<INPUT TYPE=TEXT NAME=price SIZE=6 VALUE="$Q{price}">�~ <INPUT TYPE=CHECKBOX NAME=unit${\($Q{unit}?" CHECKED":"")}>�P���w��$TRE
	$TBE
	<INPUT TYPE=HIDDEN NAME=conf VALUE="conf">
	<INPUT TYPE=SUBMIT VALUE="���t�m�F"> (����${\GetTime2HMS($TIME_SEND_ITEM)}����)
	</FORM>
	������z��ݒ肷��ƁA���i�ƈ��������ɑ���̒������o���܂��B<BR>
	����拑�ۂ����ƁA���̏��i�͔j������܂��B<BR>
	������͎󂯎��̍ہA���z�ɉ����Ď��Ԃ�����܂��B(�����قǑ����̎��Ԃ������)<BR>
	���A�o�Ŕ��p����Ȃ������ꍇ�́A���z��1/10���萔���Ƃ��Ĉ����ꏤ�i���߂��Ă��܂��B
HTML
}

1;
