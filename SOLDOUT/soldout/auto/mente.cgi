# $Id: mente.cgi 96 2004-03-12 12:25:28Z mu $

sub MenteDisplay
{
	#�����e��
	my $msg="";
	if(-f "./lock")
	{
		open(IN,"./lock");
		$msg=join("",<IN>);
		close(IN);
	}
	elsif(-f "$DATA_DIR/lock")
	{
		open(IN,"$DATA_DIR/lock");
		$msg=join("",<IN>);
		close(IN);
	}
	if($ENV{REMOTE_ADDR} ne $msg)
	{
		$msg='�������܃V�X�e�������e�i���X���ł��B<br>�\���󂲂����܂��񂪁A���΂炭���҂��������B' if $msg eq '';
		print "Content-type: text/html\n\n<html><head><title>��~��</title></head><body>$msg</body></html>";
		exit;
	}
}
1;
