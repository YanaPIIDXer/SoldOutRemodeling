#! /usr/local/bin/perl
# $Id: help.cgi 96 2004-03-12 12:25:28Z mu $

require './_base.cgi';
RequireFile("inc-help.cgi");

GetQuery();
DataRead();
CheckUserPass(1);

$p=$Q{p}+0;

$func="Page".$p;
if(defined(&$func))
{
	$disp.="<FONT SIZE=\"+1\"><B>$PAGELIST{$p}</B></FONT><HR SIZE=\"1\">";
	Menu(0);
	&$func();
}
else
{
	$disp.="<P>�y�[�W��������܂���ł����B�Ǘ��҂ɘA�����肢���܂��B</P>";
	Menu(0);
}

OutHTML('�o�c����',$disp);
exit;

sub Menu
{
	my($page,$brsw)=@_;
	my $br=$brsw ? "<BR>" : " &gt; ";
	$disp.=$brsw==2 ? $PAGELIST{$page} : GetTagA($PAGELIST{$page},"$MYNAME?$USERPASSURL&p=$page").$br;
}

sub P
{
	my($str)=@_;
	
	$str=~s/\t//g;
	
	foreach(split(/\n\n/,$str))
	{
		s/�E/<BR>�E/g;
		s/^<BR>//;
		s/\$\{(.+)\}/${\eval($1)}/g;
		$disp.="<P>".$_."</P>\n";
	}
}
