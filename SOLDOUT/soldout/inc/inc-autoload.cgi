# $Id: inc-autoload.cgi 96 2004-03-12 12:25:28Z mu $

#AUTOLOAD�p�̃C���f�b�N�X�������쐬���܂��B
#�r�����䂵�Ă��Ȃ��̂Ŗ�肪�N���邩������܂���B

sub MakeIndexAutoLoad
{
	my($functionname)=@_;
	my $requirefile="";
	%autoload=();
	
	opendir(DIR,$AUTOLOAD_DIR);
	foreach my $file (sort(readdir(DIR)))
	{
		next if $file!~/\.cgi$/;
		
		open(IN,"$AUTOLOAD_DIR/$file");
		while(<IN>)
		{
			next if !/^\s*sub\s+([^_]\w+)\s*$/;
			
			$requirefile="$AUTOLOAD_DIR/$file" if $1 eq $functionname;
			my $key=$1;
			$file=~/^([\w\-]+)\.cgi$/;
			$autoload{$key}=$1;
		}
	}
	closedir(DIR);
	
	open(OUT,">".GetPath("autoload"));
	print OUT "\%autoload=qw(".join(" ",%autoload).");1;";
	close(OUT);
	
	require $requirefile if $requirefile ne '';
}
1;
