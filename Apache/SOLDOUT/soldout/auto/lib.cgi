# $Id: lib.cgi 96 2004-03-12 12:25:28Z mu $
# �J�X�^�}�C�Y�ɕ֗��Ȋ֐��Q
# SOLD OUT �� auto �f�B���N�g���ɃR�s�[���Ă��������B
# ���ł��ǂ�����ł��g����悤�ɂȂ�܂��B
# package �� main �ɂȂ�̂ŁA�������������ӂ��B

# usage : LibMin($a,$b) $a��$b���r���ď���������Ԃ�
sub LibMin{return $_[0]<$_[1] ? $_[0] : $_[1]}

# usage : LibMax($a,$b) $a��$b���r���đ傫������Ԃ�
sub LibMax{return $_[0]>$_[1] ? $_[0] : $_[1]}

# usage : LibSwap(\$a,\$b) $a��$b����������
sub LibSwap{my $tmp=${$_[0]}; ${$_[0]}=${$_[1]}; ${$_[1]}=$tmp; return}

sub LibGetCount
{
	# usage: LibGetCount($count)
	#
	# ex: LibGetCount(100);    # 100
	#     LibGetCount(12.3);   # 12 or 13
	#     LibGetCount(-12.3);  # -12 or -13
	#     LibGetCount(0);      # 0
	#
	# �m���t�������J�E���g
	# �m�����g���ď��������𐮐��ɕϊ����� (3.1�Ȃ�1/10�̊m����4�ɕϊ������)
	#
	# $count : �������܂ސ���
	# �߂�l : ����
	my($val)=@_;
	my $int=int $val;
	$val>0 ? ($int++) : ($int--) if $val!=$int and rand 1<abs($val-$int);
	return $int;
}

sub LibEditData
{
	# usage: LibEditData($ref,$val[,{[min=>$min,][max=>$max,][set=>1,][float=>1,][abs=>1,]}])
	#
	# ex: $data=100;
	#     LibEditData(\$data,123);             # $data+=123;              (�߂�l  123)       # $data == 223
	#     LibEditData(\$data,-123);            # $data-=123;              (�߂�l -123)       # $data == 100
	#     LibEditData(\$data,123,{max=>200});  # $data+=100;              (�߂�l  100)       # $data == 200
	#     LibEditData(\$data,12.3);            # $data+=12; or $data+=13; (�߂�l 12 or 13)   # $data == 112 or 113
	#     LibEditData(\$data,123,{set=>1});    # $data=123;               (�߂�l 123)        # $data == 123
	#     LibEditData(\$data,-23.45,{abs=>1}); # $data-=23 or 24          (�߂�l 23 or 24)   # $data == 100 or 99
	#     LibEditData(\$data,"string!!");      # $data="string!!"         (�߂�l "string!!") # $data eq "string!!"
	#
	# �␳�t���f�[�^�ύXor�u���֐�
	# ���݂̒l�𑝌������A�K�v�ł���΍ŏ��l�ő�l�̃`�F�b�N&�␳���s���܂��B
	# ���l + - .(�R���})�ȊO�̒l���܂܂�Ă���ꍇ��A�I�v�V�����Ŏw�肳�ꂽ�ꍇ�͒u�������܂��B
	#
	# $ref   : �Ώەϐ��̃��t�@�����X (\$data ���X)
	# $val   : �����l or ������
	# min    : option �ŏ��l (�ȗ����͍ŏ��w�薳��)
	# max    : option �ő�l (�ȗ����͍ő�w�薳��)
	# float  : option ������F�߂� (���̃I�v�V�������Ȃ��ꍇ�͏�����LibGetCount�ŕ␳����)
	# set    : option �����ł͂Ȃ�$val�ɒu�������� (������ł͕K�{�̃I�v�V����)
	# abs    : option �߂�l�̑����l���Βl��
	# �߂�l : ���ۂɑ����ł����l or �ݒ��̒l
	#        : $ref �ɕϐ��̃��t�@�����X���^�����Ȃ������ꍇ�� undef
	my($ref,$val,$option)=@_;
	return undef if ref $ref ne "SCALAR";
	
	return $$ref=$val if $val eq "" or $val=~/[^\d\-\+\.e]/;
	
	$val=LibGetCount($val) if !$option->{float};
	$val=$$ref+$val if !$option->{set};
	$val=LibMax($val,$option->{min}) if exists $option->{min};
	$val=LibMin($val,$option->{max}) if exists $option->{max};
	
	my $old=$$ref;
	$$ref=$val;
	return $option->{set} ? $val : ($option->{abs} ? abs($val-$old) : ($val-$old));
}

my %_Lib_minmax_table=(
	rank		=>	[100,10000],
	money		=>	[0,$main::MAX_MONEY],
	moneystock	=>	[0,$main::MAX_MONEY],
);

sub LibDTEdit
{
	# usage: LibDTEdit($dt,$key,$val[,{option}])
	#
	# ex: LibDTEdit($dt,'money',12345,{set=>1}); # $dt->{money}=12345;  (�߂�l  12345) # ��������12345��
	#     LibDTEdit($dt,'money',12345);          # $dt->{money}+=12345; (�߂�l  12345) # ��������+12345
	#     LibDTEdit($dt,'money',-50000);         # $dt->{money}-=24690; (�߂�l -24690) # ��������-50000(����Ȃ��̂�0�ɕ␳)
	#     �I�v�V������ LibEditData �Ɠ���
	#
	# �␳�t��$DT�f�[�^�Z�b�g(�␳���X�g��%_Lib_minmax_table)
	# $dt  : ������$DT(���[�U�f�[�^�n�b�V��)
	# $key : �f�[�^�̃L�[
	# $val : LibEditData�Ɠ���
	# �߂�l : LibEditData�Ɠ���
	my($dt,$key,$val,$option)=@_;
	return undef if !$dt or !$key;
	
	if($_Lib_minmax_table{$key})
	{
		$option||={};
		$option->{min}=$_Lib_minmax_table{$key}[0] if !exists $option->{min};
		$option->{max}=$_Lib_minmax_table{$key}[1] if !exists $option->{max};
	}
	$dt->{$key}=0 if !exists $dt->{$key};
	return defined $val ? LibEditData(\$dt->{$key},$val,$option) : $dt->{$key};
}

sub LibDTItem
{
	# usage: LibDTItem($dt,$itemno[,$val[,{option}]])
	#
	# ex: LibDTItem($dt,10,123,{set=>1}); # $dt->{item}[10-1] =123; (�߂�l  123) # �A�C�e��No10��123��
	#     LibDTItem($dt,10,123);          # $dt->{item}[10-1]+=123; (�߂�l  123) # �A�C�e��No10��+123(�݌ɏ���`�F�b�N����)
	#     LibDTItem($dt,10,-500);         # $dt->{item}[10-1]-=246; (�߂�l -246) # �A�C�e��No10��-500(����Ȃ��̂�0�ɕ␳)
	#     �I�v�V������ LibEditData �Ɠ���
	#
	# �␳�t���A�C�e�����擾or����or�u��
	# $dt     : ������$DT(���[�U�f�[�^�n�b�V��)
	# $itemno : ���i�ԍ�(1�`)
	# $val    : LibEditData�Ɠ��� �ȗ����͌��݂̏��������擾
	# �߂�l  : LibEditData�Ɠ���
	#         : $val�ȗ����͌��݂̒l���擾
	my($dt,$itemno,$val,$option)=@_;
	return 0 if $itemno<=0 || $itemno>$main::MAX_ITEM;
	$option||={};
	$option->{min}=0                           if !exists $option->{min};
	$option->{max}=$main::ITEM[$itemno]{limit} if !exists $option->{max};;
	return !defined $val ? ($dt->{item}[$itemno-1]||0) : LibEditData(\$dt->{item}[$itemno-1],$val,$option);
}

sub LibDTExp
{
	# usage: LibDTExp($dt,$itemno[,$val[,{option}]])
	#
	# ex: LibDTItem �Ɠ���
	#
	# �␳�t���n���x�擾or����or�u��
	# $dt     : ������$DT(���[�U�f�[�^�n�b�V��)
	# $itemno : ���i�ԍ�(1�`)
	# $val    : LibEditData�Ɠ��� �ȗ����͌��݂̏n���x���擾
	# �߂�l  : LibEditData�Ɠ���
	#         : $val�ȗ����͌��݂̒l���擾
	my($dt,$itemno,$val,$option)=@_;
	return 0 if $itemno<=0 || $itemno>$main::MAX_ITEM;
	$option||={};
	$option->{min}=0    if !exists $option->{min};
	$option->{max}=1000 if !exists $option->{max};;
	return !defined $val ? ($dt->{exp}{$itemno}||0) : LibEditData(\$dt->{exp}{$itemno},$val,$option);
}

sub LibDTUser
{
	# usage: LibDTUser($dt,$key[,$val[,{option}]])
	#
	# ex: LibDTUser($dt,'dust',123,{set=>1}); # $dt->{user}{dust} =123;   (�߂�l  123) # �Ǝ��f�[�^ dust ��123��
	#     LibDTUser($dt,'dust',123);          # $dt->{user}{dust}+=123;   (�߂�l  123) # �Ǝ��f�[�^ dust ��+123(����`�F�b�N�Ȃ�)
	#     LibDTUser($dt,'dust',-500);         # $dt->{user}{dust}-=500;   (�߂�l -500) # �Ǝ��f�[�^ dust ��-500(�����`�F�b�N�Ȃ�)
	#     LibDTUser($dt,'dust',"");           # delete $dt->{user}{dust}; (�߂�l   "") # �Ǝ��f�[�^ dust ���폜
	#     �I�v�V������ LibEditData �Ɠ���
	#
	# $DT->{user}�Ǝ��f�[�^�̎擾or����or�u��
	# $dt  : ������$DT(���[�U�f�[�^�n�b�V��)
	# $key : ���[�U�f�[�^�̓Ǝ��L�[
	# $val : LibEditData�Ɠ��� �ȗ����͌��݂̒l���擾
	# option : LibEditData�Ɠ���
	# �߂�l : LibEditData�Ɠ���
	#        : $val�ȗ����͌��݂̒l���擾
	my($dt,$key,$val,$option)=@_;
	
	my $user_val=main::GetUserDataEx($dt,$key);
	return $user_val if !defined $val;
	
	my $result=LibEditData(\$user_val,$val,$option);
	main::SetUserDataEx($dt,$key,$user_val);
	return $result;
}

sub LibDTEditMoney
{
	# usage: LibDTEditMoney($dt,$val[,{option}])
	#
	# �␳�t�� $DT->{money} & $DT->{moneystock} ����
	# $DT->{money}�𑝌����A�ő�($MAX_MONEY)or�ŏ�(0)�𒴂����ꍇ�Ɏc��̑����� $DT->{monetstock} �ɍs���܂��B
	# �I�v�V�����w��ŁA�umoneystock �D��v�u�ő�ŏ��𒴂��Ă� moneystock �𑝌����Ȃ��v���A����ł��܂��B
	#
	# $dt  : ������$DT(���[�U�f�[�^�n�b�V��)
	# $val : LibEditData�Ɠ���
	# dem_money : option ������money(����)�D��ōs���܂��B(�f�t�H���g)
	# dem_stock : option ������moneystock(����)�D��ōs���܂��B
	# dem_only  : option �����̌��ʍő�ŏ��𒴂��Ă�����(money/moneystock)�𑝌����܂���B
	# �߂�l : LibEditData�Ɠ���
	my($dt,$val,$option)=@_;
	
	$option||={};
	my $target1="money";
	my $target2="moneystock";
	my $abs=exists $option->{abs};
	my $val_orig=$val;
	
	LibSwap(\$target1,\$target2) if exists $option->{dem_stock};
	delete $option->{abs} if $abs;
	
	my $result=LibDTEdit($dt,$target1,$val,$option);
	if(!exists $option->{set} && !exists $option->{dem_only} && $result!=$val)
	{
		my $result2=LibDTEdit($dt,$target2,$val-$result,$option);
		$result+=$result2;
	}
	$option->{abs}=1 if $abs;
	
	return $abs ? abs($result) : $result;
}

sub LibDTEditTime
{
	# usage: LibDTEditMoney($dt,$val[,{option}])
	#
	# �␳�t�� $DT->{time} ����
	# $DT->{time} �𑝌����A�������Ԃ̑�����s���܂��B
	# �ő厝������($MAX_STOCK_TIME)���v�Z�ɓ���܂��B
	#
	# $dt  : ������$DT(���[�U�f�[�^�n�b�V��)
	# $val : LibEditData�Ɠ���
	# �߂�l : LibEditData�Ɠ���
	my($dt,$val,$option)=@_;
	
	LibDTEdit($dt,'time',0,{min=>$main::NOW_TIME-$main::MAX_STOCK_TIME}); # �������Ԃ��ő��Ԃɕ␳
	return -LibDTEdit($dt,'time',-$val,{min=>$main::NOW_TIME-$main::MAX_STOCK_TIME});
}

sub LibDTItemList
{
	# usage: LibDTItemList($dt,[,{option}])
	#
	# $DT���L���i���X�g�擾
	# �������Ă��鏤�i�ԍ����X�g�̃��t�@�����X��Ԃ��܂��B
	#
	# $dt  : ������$DT(���[�U�f�[�^�n�b�V��)
	# �߂�l : [�������i�ԍ�1,�������i�ԍ�2,�������i�ԍ�3,...]
	#        : �Ȃɂ������Ă��Ȃ��ꍇ�͋󃊃X�g
	my($dt,$option)=@_;
	$option||={};
	my @itemlist=grep $dt->{item}[$_-1],(1..$main::MAX_ITEM);
	@itemlist=sort{$main::ITEM[$a]->{sort}<=>$main::ITEM[$b]->{sort}} @itemlist if $option->{sort};
	return scalar @itemlist ? \@itemlist : ();
}

sub LibItemCode2No
{
	# usage: LibItemCode2No($item_code)
	#
	# ���i�R�[�h��ԍ��ɕϊ�
	# 
	# $code  : ���i�R�[�h($ITEM[?]->{code})
	# �߂�l : �R�[�h�ɑΉ����鏤�i�ԍ�
	#        : ���݂��Ȃ����i�ł���� 0
	my($code)=@_;
	foreach my $no (1..$main::MAX_ITEM)
	{
		return $no if $main::ITEM[$no]{code} eq $code;
	}
	return 0;
}

sub LibDT{return $_[0]->{$_[1]}||""}                # LibDT($DT,$key)       $DT->{$key}���擾
sub LibItem{return $main::ITEM[$_[0]]->{$_[1]}||""} # LibItem($itemno,$key) $ITEM[$itemno]->{$key} ���擾

sub LibShopname{return LibDT($_[0],'shopname')} # LibShopname($DT)      $DT���t�@�����X����X�ܖ����擾
sub LibItemName{return LibItem($_[0],'name')}   # LibItemName($itemno)  ���i�ԍ����疼�̂��擾
sub LibItemScale{return LibItem($_[0],'scale')} # LibItemScale($itemno) ���i�ԍ����琔���P�ʂ��擾

1;
