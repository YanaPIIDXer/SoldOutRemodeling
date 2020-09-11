# ���̃t�@�C���̃p�[�~�b�V������644(or604or600)�ł��B
# $Id: _config.cgi 100 2004-03-15 11:32:20Z mu $

#----------------------
# ��������ΐݒ聟���� 
#----------------------
$MASTER_PASSWORD	='password';		# �Ǘ��҃p�X���[�h(�}�X�^�[�p�X���[�h) �����p�p���̂݁�
$ADMIN_EMAIL		='example@example.com';		# �Ǘ��҃��[���A�h���X
$TOWN_CODE			='';		# ���̊X�̃R�[�h
								#   ���̊X�Əd�����Ȃ��ŗL�̃R�[�h �����p�p��10�����ȓ��������̂݁�
								#   �ړ]�@�\����іf�Ջ@�\���g�p���Ȃ��ꍇ�͐ݒ肵�Ȃ��ł��������B

#----------
# �\���ݒ� 
#----------
$HTML_TITLE	='FUCKING SOLD OUT';				# �S�y�[�W��HTML�^�C�g��(HTML�s��)
$GAME_TITLE	='<H1>FUCKING SOLD OUT</H1>';		# �g�b�v�y�[�W�̃^�C�g��(HTML��)
$GAME_SUB_TITLE	='';					# �g�b�v�y�[�W�̃^�C�g���̎��ɕ\�������T�u�^�C�g��(HTML��)
$GAME_INFO	='';						# �g�b�v�y�[�W�̃^�C�g��or�T�u�^�C�g���̎��ɕ\����������(HTML��)
$BBS_INFO	='';						# �f���̐���(HTML��)
$CHAT_INFO	='';						# ��˒[�̐���(HTML��)
$GLOBAL_MSG_INFO='';					# �L��f���̃f�t�H���g����(HTML��)
										#   $GLOBAL_MSG_INFO{�J�e�S���[�R�[�h}���ݒ肳��Ă���΂����炪�D��
$RULE_INFO	='�E1�l1�X��';				# ���̃T�C�g�̃��[��(HTML��)
$MARKET_INFO	='';					# �O�o�̐���(HTLM��)

#------------
# �\���F�ݒ� 
#------------
#<body>�ȊO�̑����̓X�^�C���V�[�g�ōs�����j�ł�
$HTML_BODY_BGCOLOR		='#ffffff';	# <BODY>�w�i�F
$HTML_BODY_TEXT			='#000033';	# <BODY>�e�L�X�g
$HTML_BODY_LINK			='#5566ff';	# <BODY>�����N�F
$HTML_BODY_ALINK		='#5566ff';	# <BODY>�A�N�e�B�u�����N�F
$HTML_BODY_VLINK		='#5566ff';	# <BODY>�K��σ����N�F
$HTML_BODY_BACKGROUND	='';		# <BODY>�w�i�摜

#----------------
# <head>�ǉ��ݒ� 
#----------------
#<body>�ȊO�̑����̓X�^�C���V�[�g�ōs�����j�ł�
$HTML_HEAD=<<'HTML';				# <HEAD>�ǉ�HTML
<Style Type="text/css">
<!--
A:link   {text-decoration:none}
A:visited{text-decoration:none}
A:hover  {text-decoration:underline; color:#669966; background-color:#ccffcc}
IMG {border:1 #000000 none}
IMG.i {width:16; height:16}
IMG.s {width:32; height:16}
IMG.il {width:32; height:32; align:left}
IMG.r {width:16; height:12}
IMG.shopicon {width:32; height:32}
IMG.rank_1 {width:4; height:16}
IMG.rank_5 {width:8; height:16}
IMG.rank_10 {width:12; height:16}
IMG.rank_25 {width:14; height:16}
IMG.rank_50 {width:16; height:16}
IMG.rank_75 {width:18; height:16}
IMG.rank_100 {width:20; height:16}
IMG.rank_150 {width:22; height:16}
IMG.rank_200 {width:24; height:16}
TABLE {background-color: #ccddff}
TR {background-color: #eef4ff}
-->
</Style>
HTML

#----------
# ���ݒ� 
#----------
$HOME_PAGE			='https://github.com/YanaPIIDXer/SoldOutRemodeling';					# �z�[���y�[�WURL
$HOME_PAGE_MOBILE	='https://github.com/YanaPIIDXer/SoldOutRemodeling';					# �g�ђ[���̏ꍇ�̃z�[���y�[�WURL
$IMAGE_DIR			='./image';				# �摜�f�B���N�g��(755)
$IMAGE_URL			='image';				# �摜URL(URL�Ǝ��ۂ̃f�B���N�g�����Ⴄ�ꍇ�ݒ�)
$IMAGE_EXT			='.png';				# �摜�t�H�[�}�b�g(.gif .jpg �����摜��p�ӂ���Ύg�p�\)
$DATA_DIR			='./data';				# �f�[�^�ۑ��p�f�B���N�g��(777)
$AUTOLOAD_DIR		='./auto';				# AUTOLOAD�p�֐��t�@�C���f�B���N�g��(755)
$INCLUDE_DIR		='./inc';				# INCLUDE�f�B���N�g��(755)
$CUSTOM_DIR			='./custom';			# �J�X�^���f�[�^�f�B���N�g��(755)
$TOWN_DIR			='./town';				# ���X�f�[�^�i�[�f�B���N�g��(755)
$MARKET_DIR			='./market';			# �O�o��f�[�^�i�[�f�B���N�g��(755)
$GUILD_DIR			='./guild';				# �M���h�f�[�^�f�B���N�g��(755)
$JCODE_FILE			=$INCLUDE_DIR.'/jcode.pl';# jcode.pl�̈ʒu
$GZIP_PATH			='';					# gzip�̃p�X&�I�v�V����(���k�]�����L���ɂȂ�)
											#   �ݒ�s���̏ꍇ�͓���s��(�p�X�`�F�b�N����)
											#   ��) '/usr/bin/gzip --fast --stdout'
$DIR_PERMISSION		=0777;					# �f�B���N�g���쐬���̃p�[�~�b�V�����iWEB���[�U�̏��L�ɂȂ�\�����l�����邱�Ɓj
$TZ_JST				=60*60*9;				# GMT����̎���
$SENDMAIL			='';					# sendmail�̃p�X&�I�v�V����
											#   �G���[�������[���Ŏ󂯎��ꍇ�̂ݐݒ�

#--------------
# �f�Ջ@�\�ݒ� 
#--------------
$TRADE_ENABLE		=0;			# �f�Ջ@�\�̗L���� 1:�L�� 0:����
								#   �f�Ղ͕ʓr�f�Ջ@�\�񋟃T�C�g�ւ̓o�^���K�v�ł�
$TRADE_HOST_ALLOW	='';		# �f�Ջ���IP�F    �f�ՖԎQ�����ɖf�Ջ@�\�񋟃T�C�g�����w��
$TRADE_HOST_PASSWORD='';		# �f�Ճp�X���[�h�F�f�ՖԎQ�����ɖf�Ջ@�\�񋟃T�C�g�����w��

#--------------
# �ړ]�@�\�ݒ� 
#--------------
$MOVETOWN_ENABLE	=0;			# �ړ]�@�\�̗L���� 1:�L�� 0:����

#--------------
# �O�o�@�\�ݒ� 
#--------------
$MARKET_ENABLE		=0;			# �O�o�@�\�̗L���� 1:�L�� 0:����

#------------------
# _config �ݒ�g�� 
#------------------
# ���ݒ�𓮓I�ɕύX�������ꍇ�͉��L�t�@�C����V�K�쐬���A�L�q���Ă��������B
# �Ⴆ�΁A1�� SOLD OUT �X�N���v�g�����L���ĕ����̊X�𓮍삳�������ꍇ�ȂǁB
require './_config-local-pre.cgi' if -e './_config-local-pre.cgi';

#----------------------------------------------------------------
# �e��f�[�^�t�@�C���ݒ�(�ύX���]�܂����ł������̂܂܂ł�OK�ł�) 
#----------------------------------------------------------------
$FILE_EXT			='.cgi';					# �e��f�[�^�t�@�C���̊g���q

$COMMIT_FILE		='commit';					# �f�[�^�X�V�p�t�@�C����
$LASTTIME_FILE		='lasttime';				# �ŏI�X�V���������p�t�@�C����
$LOCK_FILE			='lockfile';				# ���b�N�p�t�@�C����
$DATA_FILE			='data';					# �f�[�^�t�@�C��
$COUNTER_FILE		='counter';					# �����J�E���^�t�@�C���x�[�X��
$LOG_FILE			='log';						# �ŋ߂̏o�����t�@�C���x�[�X��
$BBS_FILE			='bbslog';					# �f�����O�t�@�C��
$CHAT_FILE			='chatlog';					# ��˒[���O�t�@�C��
$GLOBAL_MSG_FILE	='gmsg';					# �L��f���t�@�C���x�[�X��
$BOX_FILE			='box';						# �X�֔��t�@�C��
$GUILDBAL_FILE		='guildbal';				# �M���h���x�t�@�C��
$GUILD_FILE			='guild';					# �M���h��`�t�@�C��
$PERIOD_FILE		='period';					# ���Z�����O�t�@�C��
$IP_FILE			='ip';						# ���[�U�[��IP���X�g�t�@�C����
$TRADE_FILE			='trade';					# �f�Օi�t�@�C��
$TRADE_LOCK_FILE	='tradelock';				# �f�՗p���b�N�t�@�C��
$ERROR_COUNT_FILE	='errorcnt';				# ���s�G���[�񐔋L�^�t�@�C��

$LOG_ERROR_FILE		='error';					# �G���[���O�t�@�C��
$LOG_DELETESHOP_FILE='delete';					# �X�����X�܂̃o�b�N�A�b�v�f�[�^
$LOG_MOVESHOP_FILE	='moveshop';				# �ړ]�A�N�Z�X���O�t�@�C��
$LOG_TRADE_FILE		='trade';					# �f�ՃA�N�Z�X���O�t�@�C��
$LOG_LOGIN_FILE		='login';					# ���O�C���s�������O�t�@�C��
$LOG_DEBUG_FILE		='debug';					# �f�o�b�O���O�t�@�C��
$LOG_GLOBAL_MSG_FILE='gmsg';					# �L��f�����O�t�@�C��
$LOG_MARK_FILE		='mark';					# �}�[�N���O�t�@�C��
$LOG_SIZE_MAX		=30000;						# �e�탍�O�̍ő�T�C�Y(byte) 0:���O�ۑ����� 1�`:�ő�T�C�Y

$LOG_DIR			=$DATA_DIR.'/log';			# �e��폜�\���O�t�@�C���i�[�f�B���N�g����
$ITEM_DIR			=$DATA_DIR.'/item';			# �A�C�e���f�[�^�f�B���N�g����
$SESSION_DIR		=$DATA_DIR.'/session';		# �Z�b�V����ID�i�[�f�B���N�g����
$BACKUP_DIR			=$DATA_DIR.'/backup';		# �o�b�N�A�b�v�f�B���N�g���x�[�X��
$TEMP_DIR			=$DATA_DIR.'/temp';			# ��Ɨp�f�B���N�g��
$SUBDATA_DIR		=$DATA_DIR.'/subdata';		# �T�u�f�[�^�t�@�C���i�[�f�B���N�g����

#-------------------------------------------------------
# �ȉ��A�Q�[���ݒ�ł��B�K�������ύX�̕K�v�͂���܂���B
#-------------------------------------------------------

#----------
# ��{�ݒ� 
#----------
$HERO_NAME			='�i���^';	# �`���̉p�Y�̖��O(���i�����Ɏg�p�����)
$MAX_USER			=50;		# �V���J�X���ő�X�ܐ�
$MAX_MOVE_USER		=55;		# �ړ]�󂯓���ő�X�ܐ�
								#   ���ۂ̍ő�X�ܐ��͂ǂ��炩�傫�������L��
								#   �����d�v�����X�ܐ��ݒ��傫������ƃT�[�o���ׂ������Ȃ�܂�
								#   �Ȃ�ׂ��f�t�H���g�ݒ�ȉ��ł��肢���܂�
$PASSWORD_CRYPT		=0;			# �p�X���[�h�Í��� 0=���Ȃ� 1=����

#----------
# �����ݒ� 
#----------
$NEW_SHOP_ADMIN		=0;			# �V�K�X�܃I�[�v������ 0:��� 1:�Ǘ��҂̂�
$NEW_SHOP_BLOCKIP	=0;			# 1�œ���IP�ɂ��A���o�^(�X��̍ēo�^���܂�)��j�~
$CHECK_IP			=1;			# ����IP��USER_AGENT�̃A�N�Z�X�������I�ɐ������� 1:�������� 0:�������Ȃ�
@NG_SHOP_NAME		=qw(�Ǘ� �n�� ����);
								# �X�ܖ��Ƃ��Ďg�p�ł��Ȃ��������X�y�[�X��؂�œo�^
$NEW_SHOP_KEYWORD	='';		# �V�K�X�܃I�[�v���ɕK�v�ȃL�[���[�h�̐ݒ�
								#   ���̃L�[���[�h��m���Ă���l�������o�^�ł���悤�ɂȂ�܂��B
								#   �g�p��) ���[���y�[�W�̍Ō�ɂ��̃L�[���[�h���f�ڂ��āA
								#           ���[����ǂ񂾐l�������o�^�ł���悤�ɂ��铙�B
$USE_USER_TITLE		=0;			# �g�b�v�X�܂Ɂu�T�u�^�C�g���v��ύX�ł��錠����^���邩�ǂ����̐ݒ�ł��B
								#   1:�^���� 0:�^���Ȃ�
$CHAR_SHIFT_JIS		=0;			# ���[�U����̓��{����͂� SHIFT JIS �Œ�Ƃ��Ĉ������ǂ��� 0:�������� 1:SHIFT JIS �Œ�
								#   �Œ�ɂ���Ɣ��p�J�i���p�ɂ�镶��������h�����Ƃ��\�ɂȂ�܂����A
								#   EUC �x�[�X�̒[��������̓��͂𐳂��������Ȃ��Ȃ�\��������܂��B
$JUMP_MY_GUILD		=1;			# ���j���[�ɁA��������M���h�{���n�ւ̃����N��\�����邩�ǂ��� 0:���Ȃ� 1:����
$GUILD_UNATTACH_PENALTY	=0;		# �M���h�������̓X�܂ɉۂ��y�i���e�B�� 0:���� 1~1000:���Z���ɔ���グ��0.1~100%�𒥎�

#----------
# ���Ԑݒ� 
#----------
$UPDATE_TIME			=60*5;		# �ŒZ�X�V�T�C�N��(�b)
$EXPIRE_TIME			=3600*24*7;	# �����O�C���o�^��������(�b)
$EXPIRE_EX_TIME			=3600*4;	# �����O�C���o�^����������������(�b) (�����v���C���[�D���ׁ̈A�o�c����1�����ɉ�������鎞�Ԃł��B)
$EXPIRE_MAX_TIME		=3600*24*14;# �����O�C���o�^���������ő�(�b) (�������x)
$AUTO_UNLOCK_TIME		=60;		# ���b�N���������҂��b��
$SESSION_TIMEOUT_TIME	=600;		# �Z�b�V�����^�C���A�E�g�b��(�Z���قǃZ�L�����e�B�I�ɗǂ����s�ւɂȂ�j
$ONE_DAY_TIME			=3600*27;	# ���Z�T�C�N��(�b)(3600*24��24���Ԗ��Ɍ��Z)
$DATE_REVISE_TIME		=0;			# ���Z���������炷�b��(-3600��1���ԑO�|��)
$MAX_STOCK_TIME			=48*60*60;	# �ő厝������(�b)
$BOX_STOCK_TIME			=48*60*60;	# �X�ւ��L���Ȏ���(�b)
$LOG_EXPIRE_TIME		=3600*24;	# �ŋ߂̏o�����̕ۑ�����(���ۂ͂����2�{�̊��ԕۑ������)
$PASSWORD_HASH_EXPIRE_TIME	=60*15;	# �ړ]/�f��/�L��f���Ŏg�p����ꎞ�I�ȃp�X���[�h�̗L������(�b)
									#   �Z���قǃZ�L�����e�B�I�ɗǂ����A�z�X�g�Ԃ̎������l������K�v������B

#--------------
# �\���s���ݒ� 
#--------------
$TOP_RANKING_PAGE_ROWS	=5;		# �u�g�b�v�v�����L���O�\������
$MAIN_LOG_PAGE_ROWS		=10;	# �u�X�����v�ŋ߂̏o�����\������
$SHOP_PAGE_ROWS			=5;		# �u���X�v�X�ܕ\������
$RANKING_PAGE_ROWS		=10;	# �����L���O�\������
$LIST_PAGE_ROWS_PC		=20;	# �e�탊�X�g�\������(PC)
$LIST_PAGE_ROWS_MOBILE	=5;		# �e�탊�X�g�\������(MOBILE)

#----------
# �\���ݒ� 
#----------
$SHOP_ICON_HEADER		='';	# �X�܃A�C�R���̌ď�(�����L���O�\�����ɗ��p)
								#   image/shop-$DT->{icon}.png ���X�܃A�C�R���Ƃ��ĕ\������܂��B
								#   �A�C�R�����g�p���Ȃ��ꍇ�� '' ��ݒ肵�Ă��������B
								#   �ݒ��:$SHOP_ICON_HEADER='�X��';
@TOP_COUNT_IMAGE_LIST	=qw();	# �D���M�͐ݒ�
								#   �M�͂̎�ނ�ݒ肵�܂��B
								#   ���ݒ�()�̏ꍇ�͍��܂Œʂ�̕\���ɂȂ�܂��B
								#   �ݒ��:@TOP_COUNT_IMAGE_LIST=qw(200 150 100 75 50 25 10 5 1);
								#   ���̗�̐ݒ�ł́A�D����93��̏ꍇ�A
								#    image/rank-50.png image/rank-25.png image/rank-10.png
								#    image/rank-5.png image/rank-1.png image/rank-1.png image/rank-1.png
								#   �̏��ɌM�͂��\������܂��B�Ή�����M�͉摜���K�v�ł��B
								#   �摜�̕��ƍ����̐ݒ�̓X�^�C���V�[�g�ōs�Ȃ��Ă��������B
								#   IMG.rank_1 IMG.rank_5 IMG.rank_10 �Ƃ������N���X�ɂȂ�܂��B
								#   �܂��A�M�͂̐������v10�𒴂����ꍇ�͈ȍ~�̕\�����ȗ����܂��B

#--------------
# ���j���[�ݒ� 
#--------------
$USE_BBS			=1;			# �f���g�p 0:�g�p���Ȃ� 1:�g�p����
$BBS_TITLE			='�f����';	# �f�����j���[�^�C�g��
$MAX_BBS_MESSAGE	=100;		# �f���ۑ��s��
$DENY_GUEST_BBS		=0;			# �f���{�� 0:�N�ł�OK 1:�v���C���[�̂�
$SECURE_MODE_BBS	=1;			# �f���r�炵�΍� 0:�������Ȃ� 1:�A�����e��h��
								#   �Z���Ԃ̘A�����e��j�~���܂��B

$USE_CHAT			=1;			# ��˒[�g�p 0:�g�p���Ȃ� 1:�g�p����
$CHAT_TITLE			='��˒[';	# ��˒[���j���[�^�C�g��
$MAX_CHAT_MESSAGE	=20;		# ��˒[�ۑ��s��
$DENY_GUEST_CHAT	=0;			# ��˒[�{�� 0:�N�ł�OK 1:�v���C���[�̂�
$SECURE_MODE_CHAT	=0;			# ��˒[�r�炵�΍� 0:�������Ȃ� 1:�A�����e��h��
								#   �Z���Ԃ̘A�����e��j�~���܂��B

$USE_GLOBAL_MSG		=0;			# �L��f���g�p 0:�g�p���Ȃ� 1:�g�p����
$GLOBAL_MSG_TITLE	='�L��f����';# �L��f�����j���[�^�C�g��
$MAX_GLOBAL_MSG_MESSAGE	=100;	# �L��f���ۑ��s��
$URL_GLOBAL_MSG_CENTER	=	"";	# �L��f���Z���^�[URL
								#   �����Z���^�[��URL���w�肵�܂��B
%GMSG_CATEGORY_NAME	=('_global','�O���ڑ�');
								# �L��f����M�J�e�S���[�i'�R�[�h','����',...�j
								#   �󂯕t����J�e�S���[�̃R�[�h����і��̂̃��X�g�B
								#   �����w�肵�Ȃ��Ă��A�f�t�H���g�̃J�e�S���[�͋����I�Ɏ�M��������B
								#   �R�[�h����і��͔̂C�ӁB
								#   �������A_(�A���_�[�o�[)����n�܂�R�[�h�̓V�X�e���\��B
								#   �����R�[�h���̗p���Ă���L��f���Z���^�[����ъX�Ƃ̌𗬂��\�B

$USE_CUSTOM			=0;			# �J�X�^���y�[�W�g�p  0:�g�p���Ȃ� 1:�g�p����
$CUSTOM_TITLE		='�J�X�^��';# �J�X�^���y�[�W���j���[�^�C�g��
$DENY_GUEST_CUSTOM	=0;			# �J�X�^���y�[�W�{�� 0:�N�ł�OK 1:�v���C���[�̂�
								#   �u0:�N�ł�OK�v�ɐݒ肵�Ă��A�J�X�^���y�[�W�������ł��̓s�x�{���s�ɏo���܂��B

@CUSTOM_MENU=();				# ��ʏ㕔�̃��j���[�ɒǉ�����J�X�^�����j���[ ('URL','����',...)
								# ���T�C�g�ȊO�ւ̃����N���ƃZ�b�V������񂪑��T�C�g�֗��o����̂Œ��ӁB
$USE_PORT			=0;			# [�O��]���j���[�̎g�p 0:�g�p���Ȃ� 1:�g�p����
$OUTPUT_LAST_MODIFIED	=0;		# ��˒[/�f����/�L��f����HTTP�w�b�_LAST-MODIFIED���o�� 0:�o�͂��Ȃ� 1:�o�͂���

#----------------------
# �o�b�N�A�b�v���Ԑݒ� 
#----------------------
$BACKUP_TIME	=3600;	# ����f�[�^�o�b�N�A�b�v�b��
$BACKUP			=3;		# �f�[�^�o�b�N�A�b�v���㐔(��)
@BACKUP_FILES	=();	# �ǉ��o�b�N�A�b�v�Ώۃt�@�C���z��
						#   �ȉ��Ɋ֘A����t�@�C���̓f�t�H���g�Ńo�b�N�A�b�v�ΏۂɂȂ��Ă��܂��B
						#   $BBS_FILE $CHAT_FILE $GLOBAL_MSG_FILE $LOG_FILE $BOX_FILE $PERIOD_FILE $GUILDBAL_FILE $DATA_FILE

#--------------------
# �Q�[���o�����X�ݒ� 
#--------------------
$PROFIT_DAY_COUNT	=3;			# �_���v�Z�̍ۍl������ߋ��̏����v�i���j
$SALE_SPEED			=10;		# ����s���{��(inc-item-data.cgi�ł̐ݒ��1�Ƃ���)
$POP_DOWN_RATE		=5;			# �l�C���R������(�傫���قǁA���݂̐l�C�ɉ����Ă̏㉺�����傫���Ȃ�)
$LIMIT_EXP			=0;			# �n���x�̍��v�l���~�b�g 0:������� 1~:����ݒ�(1=0.1%)
$EXP_DOWN_POINT		=5;			# ���Z���Ɏ��R��������n���x�|�C���g(1%==10)
$EXP_DOWN_RATE		=60;		# ���Z���Ɏ��R��������n���x����(6%==60)
								# ��:���݂̏n���x50%�̏ꍇ�A�Œ��0.5%��50%��6%��3%�A���킹��3.5%��������
$MAX_BOX			=5;			# ���b�Z�[�W�ޑ��M�ő吔
$TOWN_TYPE			="normal";	# �X(���i�f�[�^)�̃^�C�v�ݒ�
								#  normal   -> [�r��^�C�v] �ʏ펞�ԃp�^�[��
								#  sotype1  -> [���H�^�C�v] ���H���ԒZ�k�p�^�[��
								#  sotype2  -> [�����^�C�v] �f�ލ̎掞�ԒZ�k�p�^�[��
								#  timehalf -> [��i�^�C�v] �S���ԒZ�k�p�^�[��

#--------------
# �f�o�b�O�ݒ� 
#--------------
$DEBUG_MOBILE		=0;			# 1�Ōg�ђ[�������Œ�
$DEBUG_PRINT		=0;			# 1�ŉ\�Ȍ���500�G���[�̓��e��\��
								#   �Z�L�����e�B��̌��O�����邽�߁A�f�t�H���g�ł͏o�͖����B
								#   �g�p�̓��[�J���ł̊J�����݂̂Ɍ��肵�Ă��������B
$DEBUG_LOG_ENABLE	=0;			# 1��item::DebugLog()��event::DebugLog()��L����
$MAX_ERROR_COUNT	=5;			# ���[���ŃG���[�񍐂���ő吔(�f�t�H���g�𐄏�)
								#   �����̃G���[���[���Ń��[���{�b�N�X������̂�h�����߂̐����ł��B
								#   ���̉񐔈ȏ�̃��[���񍐂͍s���܂���B
								#   �ݐω񐔂͊Ǘ����j���[�Ń��Z�b�g�ł��܂��B
								#   �G���[���[�����͂����тɃ��Z�b�g����Ƃ����ł��傤�B
								#   ���G���[���[���̗L�����ɂ�$SENDMAIL�̐ݒ肪�K�v�ł��B

#--------------------------------------
# ���l�p�����[�^�����`�F�b�N���O���X�g 
#--------------------------------------
# "nan" �������� "inf" �����͂���Ă�������󂯓����p�����[�^�̃��X�g�ł��B
# "nan" �������� "inf" �𕶎���Ƃ��ė��p����ꍇ�ɂ́A
# ���̃R�}���h�̃X�N���v�g��(bbs,chat��)�ƃp�����[�^��(msg��)�����X�g�ɒǉ����ĉ������B
# ���̃��X�g�ɓ����Ă��Ȃ��p�����[�^�̏ꍇ�A
# "nan" �������� "inf" ����n�܂���͂͑S�� 0 �ɒu���������܂��B
# �����͈ȉ����Q�l�ɂ��Ă��������B("�t�@�C���x�[�X��:�p�����[�^��"=>"str", ...)
%QUERY_TYPE_TABLE=(
	"u"				=>	"str",
	"nm"			=>	"str",
	"pw"			=>	"str",
	"ss"			=>	"str",
	"bbs:msg"			=>	"str",
	"box-edit:cmd"		=>	"str",
	"box-edit:msg"		=>	"str",
	"box-edit:title"	=>	"str",
	"box-edit:tradein"	=>	"str",
	"buy:buy"			=>	"str",
	"chat:msg"			=>	"str",
	"custom:cmd"		=>	"str",
	"gmsg:ct"			=>	"str",
	"item-use:msg"		=>	"str",
	"jump:guild"		=>	"str",
	"jump:town"			=>	"str",
	"jump:gmsgtown"		=>	"str",
	"log:key"			=>	"str",
	"log:tgt"			=>	"str",
	"main:ck"			=>	"str",
	"move-town:towncode"=>	"str",
	"move-town:pass"	=>	"str",
	"move-town:nm"		=>	"str",
	"move-town:name"	=>	"str",
	"new:admin"			=>	"str",
	"new:name"			=>	"str",
	"new:sname"			=>	"str",
	"new:pass1"			=>	"str",
	"new:pass2"			=>	"str",
	"new:newkey"		=>	"str",
	"user:cmt"			=>	"str",
	"user:pw1"			=>	"str",
	"user:pw2"			=>	"str",
	"user:pwvrf"		=>	"str",
	"user:cls"			=>	"str",
	"user:rename"		=>	"str",
	"user:guild"		=>	"str",
	"user:usertitle"	=>	"str",
	"user:closecmt"		=>	"str",
	"admin-sub:user"		=>	"str",
	"admin-sub:comment"		=>	"str",
	"admin-sub:nocheckip"	=>	"str",
	"admin-sub:blocklogin"	=>	"str",
);

# set umask
umask(~$DIR_PERMISSION & 0777);

#------------------
# _config �ݒ�g�� 
#------------------
# �e�T�C�g���̕ύX�_�͂��̃t�@�C�����쐬���A�L�q����ƕ֗���������܂���B���e�͎��R�ł��B
require './_config-local.cgi' if -e './_config-local.cgi';
1;
