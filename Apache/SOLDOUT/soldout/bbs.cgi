#! /usr/local/bin/perl
# $Id: bbs.cgi 96 2004-03-12 12:25:28Z mu $

$NOITEM=1;
require './_base.cgi';
OutError('�g�p�s�ł�') if !$USE_BBS;

GetQuery();

DataRead();
CheckUserPass(1);
OutError('�g�p�s�ł�') if $GUEST_USER && $DENY_GUEST_BBS;

$LOG_FILE=$BBS_FILE;
$BBSMODE=1;
($Q{msg},$errormsg)=WriteBBS($Q{msg},100) if !$GUEST_USER && $Q{msg};

ReadLog();
RequireFile('inc-html-bbs.cgi');

$Q{bk}="none",$NOMENU=1 if $MASTER_USER;
OutHTML($BBS_TITLE,$disp,$OUTPUT_LAST_MODIFIED ? (stat(GetPath($LOG_FILE)))[9] : 0);
