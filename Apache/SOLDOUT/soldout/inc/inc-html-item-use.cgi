# $Id: inc-html-item-use.cgi 96 2004-03-12 12:25:28Z mu $

RequireFile('inc-html-ownerinfo.cgi');

my $count=$USE->{result}->{count};

$disp.="������<BR>";

if(!$count)
{
	$disp.="���s�ł��܂���ł���";
}
else
{

	$disp.=$USE->{result}->{function_return}."<BR>" if $USE->{result}->{function_return};
	$disp.=$USE->{result}->{count}.$USE->{scale}."<BR>";
	$disp.="��p:\\".($USE->{money}*$USE->{result}->{count})."<BR>" if $USE->{money}*$USE->{result}->{count};
	$disp.="����:".GetTime2HMS(GetItemUseTime($USE)*$count)."<BR><BR>";
	
	foreach my $MESSAGE (@{$USE->{result}->{addmsg}})
		{$disp.=$MESSAGE."<BR>" if $MESSAGE;}
	
	if($USE->{result}->{additem}[0])
	{
		my $result=$USE->{result}->{message}->{resultok};
		$disp.=$result."<BR>" if $result;
		
		foreach my $MESSAGE (@{$USE->{result}->{trashmsg}})
			{$disp.=$MESSAGE."<BR>" if $MESSAGE;}
		
		$disp.="����:";
		foreach my $ADDITEM (@{$USE->{result}->{additem}})
		{
			my $no=$ADDITEM->[0];
			$disp.=$ITEM[$no]->{name};
			$disp.=" +".$ADDITEM->[1]." (�c".$DT->{item}[$no-1].") ";
		}
		$disp.="<BR>";
	}
	else
	{
		my $result=$USE->{result}->{message}->{resultng};
		$disp.=$result."<BR>" if $result;
	}
	
	foreach my $MESSAGE (@{$USE->{result}->{usemsg}})
	{
		$disp.=$MESSAGE."<BR>" if $MESSAGE;
	}
	
	if($USE->{result}->{useitem}[0])
	{
		$disp.="����:";
		foreach my $USEITEM (@{$USE->{result}->{useitem}})
		{
			my $no=$USEITEM->[0];
			$disp.=$ITEM[$no]->{name};
			$disp.=" -".$USEITEM->[1]." (�c".$DT->{item}[$no-1].") ";
		}
		$disp.="<BR>";
	}
}
1;
