#! /usr/local/bin/perl
# $Id: box-edit.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
GetQuery();

Lock() if $Q{cmd}ne'newmail' && $Q{cmd}ne'newmoney' && $Q{cmd}ne'newitem';

DataRead();
CheckUserPass();

$backurl="<HR><A HREF=\"box.cgi?$USERPASSURL\">[�ꗗ�ɖ߂�]</A>";

$Q{price}=int($Q{price}+0);
$Q{itemcnt}=int($Q{itemcnt}+0);
ReadBox();

if($Q{cmd}eq'newmail')
{
	CheckOutBoxBuffer();
	RequireFile('inc-html-box-new-mail.cgi');
}
elsif($Q{cmd}eq'newmoney')
{
	CheckOutBoxBuffer();
	RequireFile('inc-html-box-new-money.cgi');
}
elsif($Q{cmd}eq'newitem')
{
	CheckOutBoxBuffer();
	RequireFile('inc-html-box-new-item.cgi');
}
elsif($Q{reset}ne'')
{
	if($DT->{boxcount}<0)
	{
		$DT->{boxcount}=0;
		DataWrite();
		$disp.="��M�������Z�b�g���܂���";
	}
	else
	{
		$disp.="���Z�b�g����K�v�͂���܂���";
	}
}
elsif($Q{del})
{
	getBoxDetail($Q{del},0,'nocheckshop');
	if($flag & $FLAG_TO_READ)
	{
		DeleteBox($no);
		WriteBox();
		$disp.="���b�Z�[�W���폜���܂���";
		$DT->{boxcount}--;
		SetUserDataEx($DT,"_so_trtm_$no","");
		#$DT->{boxcount}=0 if $DT->{boxcount}<0;
		DataWrite();
	}
	elsif($modtime<$NOW_TIME-$BOX_STOCK_TIME)
	{
		CheckTradeProcess() if $cmd==$CMD_TRADE;
		DeleteBox($no);
		WriteBox();
		if($to>=100)
		{
			if(exists $id2idx{$to})
			{
				my $DTS=$DT[$id2idx{$to}];
				$DTS->{boxcount}--;
				#$DTS->{boxcount}=0 if $DTS->{boxcount}<0;
			}
		}
		SetUserDataEx($DT,"_so_trtm_$no","");
		$disp.="���b�Z�[�W�������폜���܂���";
		DataWrite();
	}
}
elsif($Q{sendmail})
{
	CheckOutBoxBuffer();
	$Q{sendmail}+=0;
	$Q{price}+=0;
	($precheckerror,$DTS)=PreCheckNewBoxArg('mail',$Q{sendmail},$Q{price});
	if($Q{conf} ne '' || $Q{ok} eq '' || $precheckerror ne '')
	{
		RequireFile('inc-html-box-new-mail.cgi');
	}
	else
	{
		CheckNewBoxArg();
		
		UseTime($TIME_SEND_MONEY) if $Q{price};
		NewBox($CMD_MAIL,$Q{sendmail},0,$Q{msg},$Q{title},$Q{price});
		WriteBox();
		$disp.=$DTS->{shopname}."�փ��b�Z�[�W�𑗐M���܂���";
		$DTS->{boxcount}++;
		DataWrite();
		WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."�֗����t�����𑗐M���܂���",1) if $Q{price};
	}
}
elsif($Q{sendmoney})
{
	CheckOutBoxBuffer();
	$Q{sendmoney}+=0;
	$Q{price}+=0;
	($precheckerror,$DTS)=PreCheckNewBoxArg('money',$Q{sendmoney},$Q{price});
	if($Q{conf} ne '' || $Q{ok} eq '' || $precheckerror ne '')
	{
		RequireFile('inc-html-box-new-money.cgi');
	}
	else
	{
		CheckNewBoxArg();
		
		UseTime($TIME_SEND_MONEY) if $Q{price};
		NewBox($CMD_MONEY,$Q{sendmoney},0,$Q{msg},$Q{title},$Q{price});
		WriteBox();
		$disp.=$DTS->{shopname}."��\\".$Q{price}."�������܂���";
		$DT->{money}-=$Q{price};
		$DT->{paytoday}+=$Q{price};
		$DTS->{boxcount}++;
		DataWrite();
		WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."��\\$Q{price}�������܂���",1);
	}
}
elsif($Q{senditem})
{
	CheckOutBoxBuffer();
	$Q{senditem}+=0;
	$Q{price}+=0;
	$Q{itemno}+=0;
	$Q{itemcnt}+=0;
	($precheckerror,$DTS)=PreCheckNewBoxArg('item',$Q{senditem},$Q{price},$Q{itemno},$Q{itemcnt});
	if($Q{conf} ne '' || $Q{ok} eq '' || $precheckerror ne '')
	{
		RequireFile('inc-html-box-new-item.cgi');
	}
	else
	{
		$Q{msg}=" " if $Q{msg}eq"";
		CheckNewBoxArg();
		$Q{msg}="" if $Q{msg}eq" ";
		my $itemno=CheckItemNo($Q{itemno},$DT);
		my $ITEM=$ITEM[$itemno];
		my $price=$Q{price};
		$price*=$Q{itemcnt} if $Q{unit};
		
		if($Q{senditem}>=100) # >=100:�ʏ�̓X�ܑ��� ==1:�f��
		{
			UseTime($TIME_SEND_ITEM);
			NewBox($CMD_ITEM,$Q{senditem},0,$Q{msg},$itemno."!".$Q{itemcnt},$price);
			WriteBox();
			$disp.=$DTS->{shopname}."��".$ITEM->{name}."��".$Q{itemcnt}.$ITEM->{scale}."����܂���";
			$DTS->{boxcount}++;
			$DT->{item}[$itemno-1]-=$Q{itemcnt};
			DataWrite();
			WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."��".$ITEM->{name}.":".$Q{itemcnt}.$ITEM->{scale}."��".($price?"\\$price�ɂ�":"")."����܂���",1);
		}
		elsif($Q{senditem}==1 && $TRADE_ENABLE)
		{
			CheckTradeProcess();
			OutError('���z���s���ł�') if $price<=0;
			UseTime($TIME_SEND_ITEM);
			NewBox($CMD_TRADE,1,0,$Q{msg},$itemno."!".$Q{itemcnt}."!1",$price);
			WriteBox();
			$disp.=$ITEM->{name}."��".$Q{itemcnt}.$ITEM->{scale}."�A�o���܂���";
			$DT->{item}[$itemno-1]-=$Q{itemcnt};
			DataWrite();
			WriteLog(3,0,0,$DT->{shopname}."��".$ITEM->{name}.":".$Q{itemcnt}.$ITEM->{scale}."��".($price?"\\$price�ɂ�":"")."�A�o���܂���",1);
		}
	}
}
elsif($Q{tradein})
{
	CheckTradeProcess();
	CheckOutBoxBuffer();
	if($Q{ok} eq '')
	{
		RequireFile('inc-html-box-tradein.cgi');
	}
	else
	{
		my %itemcode2idx=();
		foreach(0..$MAX_ITEM){$itemcode2idx{$ITEM[$_]->{code}}=$_;}
		my($hostcode,$boxno,$itemcode,$itemcnt,$price)=split(/!/,$Q{tradein});
		$price=int($price);
		my $itemno=$itemcode2idx{$itemcode};
		my $ITEM=$ITEM[$itemno];
		OutError('�s���ȗv���ł�') if CheckItemFlag($itemno,'notradein');
		OutError('����������܂���') if $DT->{money}<$price;
		OutError('�s���ȗA�o�i�̂悤�ł��̂Ŏ葱���ł��܂���') if $itemcnt=~/\D/ or $price=~/\D/;
		
		my($shopname,$hostname,$msg);
		open(IN,GetPath($TRADE_FILE));
		($TRADE_STOCK_TIME)=split(/[\t\n]/,<IN>);
		while(<IN>)
		{
			chop;
			my($trademode,$tradetime,$tradecode,$shopinfo)=split(/\t/);
			next if $trademode!=1 || $tradecode ne $Q{tradein};
			
			$shopname=(split(/!/,$shopinfo,3))[-1];
			($shopname,$hostname,$msg)=split(/,/,$shopname);
			last;
		}
		close(IN);
		
		my $newboxno=NewBox($CMD_TRADE,1,0,$Q{msg},"$itemno!$itemcnt!0!$hostcode!$boxno!$shopname!$hostname!$msg",$price);
		WriteBox();
		$disp.=$ITEM->{name}.":".$itemcnt.$ITEM->{scale}."�̗A���葱�������܂���";
		$DT->{money}-=$price;
		UseTime(SetUserDataEx($DT,"_so_trtm_$newboxno",GetTimeDeal($price,$itemno,$itemcnt)));
		DataWrite();
		WriteLog(1,$DT->{id},0,$ITEM->{name}.":".$itemcnt.$ITEM->{scale}."�̗A���葱�������܂���",1);
	}
}
elsif($Q{alw} || $Q{dny})
{
	getBoxDetail(($Q{alw}!=0 ? $Q{alw}+0 : $Q{dny}+0),1);
	goto esc_box_edit if $flag & $FLAG_TO_READ;
	
	my $idx=$id2idx{$from};
	my $DTS=$DT[$idx];
	my $workflag_pay=$flag & $FLAG_PAY;
	my $boxcountnoop=0;
	
	if($cmd==$CMD_MAIL)
	{
		if($price && !$workflag_pay)
		{
			if($Q{alw})
			{
				if($price>$DT->{money})
				{
					$disp.="����������܂���ł���";
				}
				else
				{
					$DT->{money}-=$price;
					$DTS->{moneystock}+=$price;
					$DT->{paytoday}+=$price;
					$disp.="\\$price�x�����܂���";
					WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."�֏��\\$price���x�����܂���",1);
					EditBox($no,"|".$FLAG_PAY);
					DataWrite();
					WriteBox();
				}
				goto esc_box_edit;
			}
			else
			{
				$disp.="��M�����ۂ��܂���";
				WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."����̏��񋟂����ۂ��܂���",1);
				EditBox($no,"|".$FLAG_TO_READ);
			}
		}
		else
		{
			if($Q{alw})
			{
				$disp.="�ԓ��Ƃ��āu�͂��v�𑗐M���܂���";
				EditBox($no,"|".($FLAG_TO_READ+$FLAG_RETURN_YESNO));
			}
			else
			{
				$disp.="�ԓ��Ƃ��āu�������v�𑗐M���܂���";
				EditBox($no,"|".$FLAG_TO_READ);
			}
		}
	}
	if($cmd==$CMD_MONEY)
	{
		if($Q{alw})
		{
			$DT->{moneystock}+=$price;
			$disp.="\\$price�󂯎��܂���";
			EditBox($no,"|".($FLAG_PAY+$FLAG_TO_READ));
			WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."����̑���\\$price���󂯎��܂���",1);
		}
		else
		{
			$disp.="�����̎󂯎������ۂ��܂���";
			EditBox($no,"|".($FLAG_TO_READ));
			WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."����̑������󂯎�苑�ۂ��܂���",1);
		}
	}
	if($cmd==$CMD_ITEM)
	{
		if($Q{alw})
		{
			if($price>$DT->{money})
			{
				$disp.="����������܂���ł���";
				goto esc_box_edit;
			}
			else
			{
				my($itemno,$itemcnt)=split(/!/,$data);
				UseTimeDeal($price,$itemno,$itemcnt);
				$DT->{money}-=$price;
				$DT->{paytoday}+=$price;
				
				my($taxrate,$tax)=GetSaleTax($itemno,$num,$price*$num,GetUserTaxRate($DTS));
				$DTS->{moneystock}+=$price-$tax;
				$DTS->{saletoday}+=$price;
				$DTS->{taxtoday}+=$tax;
				
				my $itemplus=$itemcnt;
				my $ITEM=$ITEM[$itemno];
				$itemplus=$ITEM->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$itemplus>$ITEM->{limit};
				$DT->{item}[$itemno-1]+=$itemplus;
				$disp.="\\$price�x�����A" if $price;
				$disp.=$ITEM->{name}."��".$itemcnt.$ITEM->{scale}."�󂯎��܂���";
				$disp.="�@���A�����ő吔�𒴂����̂�".($itemcnt-$itemplus).$ITEM->{scale}."��j�����܂���" if $itemplus!=$itemcnt;
				EditBox($no,"|".($FLAG_PAY+$FLAG_TO_READ));
				WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."�֏��i(".$ITEM->{name}.":".$itemcnt.$ITEM->{scale}.")�̑��\\$price���x�����܂���",1) if $price;
				WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."����̏��i(".$ITEM->{name}.":".$itemcnt.$ITEM->{scale}.")���󂯂Ƃ�܂���",1) if !$price;
			}
		}
		else
		{
			$disp.="���i�̎󂯎������ۂ��܂���";
			EditBox($no,"|".($FLAG_TO_READ));
			WriteLog(3,0,0,$DT->{shopname}."��".$DTS->{shopname}."����̏��i�󂯎������ۂ��܂���",1);
		}
	}

	WriteBox();
	$DT->{boxcount}--;
	$DT->{boxcount}=0 if $DT->{boxcount}<0;
	$DTS->{boxcount}++;
	$DT->{money}=$MAX_MONEY if $DT->{money}>$MAX_MONEY;
	DataWrite();
}

esc_box_edit:

DataCommitOrAbort(),UnLock() if $Q{cmd}ne'newmail' && $Q{cmd}ne'newmoney' && $Q{cmd}ne'newitem';

$disp.=$backurl;
OutHTML('�X�֔�',$disp);
exit;

sub getBoxDetail
{
	my($num,$sendrecvmode,$mode)=@_;

	my $idx=SearchBoxIndex($num);
	OutError('���݂��Ȃ����b�Z�[�W�ł�'.$backurl) if $idx==-1;
	
	($no,$from,$to,$flag,$modtime,$cmd,$time,$price,$data,$msg)=split(/,/,$BOX[$idx]);
	
	OutError('���݂��Ȃ��X�܂ł���'.$backurl) if !defined($id2idx{$to}) && $mode ne 'nocheckshop';
	OutError('���݂��Ȃ��X�܂ł���'.$backurl) if !defined($id2idx{$from});
	
	OutError('����������܂���'.$backurl) if $sendrecvmode==0 && $DT->{id}!=$from;
	OutError('����������܂���'.$backurl) if $sendrecvmode==1 && $DT->{id}!=$to;
}

sub CheckOutBoxBuffer
{
	GetOutBox();
	OutError('���M��'.$MAX_BOX.'�ʂ܂łł�<BR>���M�ς݂��폜���Ă�������'.$backurl) if $#OUTBOX+1>=$MAX_BOX;
}

sub CheckNewBoxArg
{
	require $JCODE_FILE;
	
	$Q{msg}=CutStr(jcode::sjis($Q{msg},$CHAR_SHIFT_JIS&&'sjis'),200);
	$Q{title}=CutStr(jcode::sjis($Q{title},$CHAR_SHIFT_JIS&&'sjis'),40);
	OutError('���e������܂���'.$backurl) if $Q{msg}eq'';
	$Q{title}="����" if $Q{title}eq'';
	$Q{price}+=0;
	$Q{price}=$MAX_MONEY if $Q{price}>$MAX_MONEY;
}

sub PreCheckNewBoxArg
{
	my($mode,@data)=@_;
	my $DTS={};
	my @ret=();
	
	my $maxlength;
	
	$DTS=$DT[$id2idx{$data[0]}] if defined($id2idx{$data[0]});
	
	if($mode eq 'mail')
	{
		push(@ret,'�������w�肵�Ă��������B') if !defined($id2idx{$data[0]});
		push(@ret,'��񗿂��s���ł��B')         if $data[1]<0;
	}
	elsif($mode eq 'money')
	{
		push(@ret,'�������w�肵�Ă��������B') if !defined($id2idx{$data[0]});
		push(@ret,'�����z��\\0�ȉ��ł��B')      if $data[1]<=0;
		push(@ret,'����������܂���B')         if $data[1]>$DT->{money};
	}
	elsif($mode eq 'item')
	{
		push(@ret,'�������w�肵�Ă��������B')          if !defined($id2idx{$data[0]}) && $data[0]!=1;
		push(@ret,'���i��I�����Ă��������B'),$data[2]=0 if $data[2]<1 || $data[2]>$MAX_ITEM;
		push(@ret,'���t�����s���ł��B')                if $data[3]<=0;
		push(@ret,'���i�݌ɂ�����܂���B')              if $data[2] && $DT->{item}[$data[2]-1]<$data[3];
		push(@ret,'���z���s���ł��B')                    if $data[1]<0;
		push(@ret,'���z���s���ł��B')                    if $data[1]==0 && $data[0]==1;
		push(@ret,'���t�s���i�ł��B')                  if $data[0]!=1 && CheckItemFlag($data[2],'nosend');
		push(@ret,'�A�o�s���i�ł��B')                  if $data[0]==1 && CheckItemFlag($data[2],'notradeout');
	}
	
	push(@ret,'���z���������܂��B') if $data[1]>$MAX_MONEY;
	
	$maxlength=40;
	push(@ret,'�^�C�g���͔��p'.$maxlength.'����(�S�p'.int($maxlength/2).'����)�܂łł��B���ݔ��p'.length($Q{title}).'�����ł��B') if length($Q{title})>$maxlength;
	$maxlength=200;
	push(@ret,'���e���͔��p'.$maxlength.'����(�S�p'.int($maxlength/2).'����)�܂łł��B���ݔ��p'.length($Q{msg}).'�����ł��B') if length($Q{msg})>$maxlength;
	
	push(@ret,'���e��������܂���B') if $Q{msg} eq '' && ($mode ne 'item' || $data[0]!=1) ;
	
	push(@ret,"<hr>") if @ret!=();
	
	return (join("<br>",@ret),$DTS);
}

1;
