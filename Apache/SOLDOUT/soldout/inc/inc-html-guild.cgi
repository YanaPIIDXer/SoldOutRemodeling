# $Id: inc-html-guild.cgi 96 2004-03-12 12:25:28Z mu $

if($guilddetail)
{
	$disp.="���M���h�ڍ�<HR>";
	
	my $code    =$guilddetail;
	my $name    =$GUILD{$code}->[$GUILDIDX_name];
	my $dealrate=$GUILD{$code}->[$GUILDIDX_dealrate];
	my $feerate =$GUILD{$code}->[$GUILDIDX_feerate];
	my $url     =$GUILD_DETAIL{$code}->{url};
	my $comment =$GUILD_DETAIL{$code}->{comment};
	my $guild={};
	my $rank=0;
	foreach my $guildlist (@guildlist){$rank++; $guild=$guildlist,last if $guildlist->{guild} eq $code;}
	
	$disp.=qq|<p><a target="_blank" href="jump.cgi?guild=$code">|.GetTagImgGuild($code).$name.' �̖{���n��'."</a></p>";
	
	$disp.=$TB;
	$disp.=$TR.$TD.'RANK'.$TD.$rank.$TRE;
	$disp.=$TR.$TD.'�M���h�R�[�h'.$TD.$code.$TRE;
	$disp.=$TR.$TD.'���'.$TD.($guildcount{$code}+0).'�X��'.$TRE;
	$disp.=$TR.$TD.'����'.$TD.'\\'.($guild->{money}+0).($guild->{money}<0 ? '(�Ԏ�)' : '').$TRE;
	$disp.=$TR.$TD.'����'.$TD.'\\'.($guild->{in}+0).$TRE;
	$disp.=$TR.$TD.'�x�o'.$TD.'\\'.($guild->{out}+0).$TRE;
	$disp.=$TR.$TD.'��������'.$TD.($dealrate/10).'%'.$TRE;
	$disp.=$TR.$TD.'��'.$TD.($feerate/10).'%'.$TRE;
	$disp.=$TR.$TD.'�R�����g'.$TD.$comment.$TRE;
	$disp.=$TBE;
	
	$disp.=qq|<p><a href="guild.cgi?pg=$Q{pg}&$USERPASSURL">|.'�ꗗ�ɖ߂�'."</a></p>";
}
else
{
	$disp.="���M���h�ꗗ<HR>";
	
	my($page,$pagestart,$pageend,$pagenext,$pageprev,$pagemax)
		=GetPage($Q{pg},$LIST_PAGE_ROWS,scalar(@guildlist));
	my $pagecontrol=GetPageControl($pageprev,$pagenext,"","",$pagemax,$page);
	$disp.=$pagecontrol."<BR>";
	
	my $rank=$pagestart+1;
	
	$disp.=$TB;
	foreach my $guild (@guildlist[$pagestart..$pageend])
	{
		my $code    =$guild->{guild};
		my $name    =$GUILD{$code}->[$GUILDIDX_name];
		#my $dealrate=$GUILD{$code}->[$GUILDIDX_dealrate];
		#my $feerate =$GUILD{$code}->[$GUILDIDX_feerate];
		#my $url     =$GUILD_DETAIL{$code}->{url};
		#my $comment =$GUILD_DETAIL{$code}->{comment};
		
		$disp.=$TR;
		$disp.=$TD."RANK".$rank++;
		$disp.=$TD.qq|<a href="guild.cgi?detail=$code&pg=$Q{pg}&$USERPASSURL">|.GetTagImgGuild($code).$name."</a>";
		$disp.=$TD."��� ".($guildcount{$code}+0)." �X��";
		$disp.=$TRE;
	}
	$disp.=$TBE;
	
	$disp.=$pagecontrol;
}
1;
