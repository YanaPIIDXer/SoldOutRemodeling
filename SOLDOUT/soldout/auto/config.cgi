# $Id: config.cgi 96 2004-03-12 12:25:28Z mu $

sub ReadConfig
{
	open(IN,$_[0]) or return ();;
	my @data=();
	while(<IN>)
	{
		chop;
		s/#.*$//;
		#�e��ݒ�t�@�C���ł͊댯����̂��߁u< > "�v�͎g�p�s�u&�v�͎g�p��
		#s/&/&amp;/g;
		s/</&lt;/g;
		s/>/&gt;/g;
		s/"/&quot;/g;
		push(@data,$1,$2) if /^\s*(.+?)\s*=\s*(.+?)\s*$/;
	}
	close(IN);
	return @data;
}

1;
