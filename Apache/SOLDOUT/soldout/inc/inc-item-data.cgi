# $Id: inc-item-data.cgi 96 2004-03-12 12:25:28Z mu $

# ���̃t�@�C���̓A�C�e���f�[�^�̒�`�t�@�C���ł��B
# �ȒP�Ȑ������Ō�ɂ���܂��̂ŁA�����������B

@@DEFINE							#����{�f�[�^�̒�`�錾
	version	2002-12-02				#�����i�f�[�^�o�[�W�����\�L
	set		HERO_NAME	$$HERO_NAME	#���ϐ��̒�`�i$HERO_NAME���`���A�Q�Ɖj��2001-06-06�ǉ�
									#��$$name��_config.cgi���̕ϐ�$name���Q��

	scale	��			#���f�t�H���g�̐����P�ʂ̒�`
	type0	�S			#���A�C�e�����ޒ�`(type0�͑S�A�C�e���̏W����)
	type1	����		#��type1���ނ̒�`
	type2	�{			#type2���ނ̒�`
	type3	��			#type3���ނ̒�`
	type4	��			#type4���ނ̒�`
	type5	�Z			#type5���ނ̒�`
	type6	��			#type6���ނ̒�`
	type7	��			#type7���ނ̒�`
	type8	�A�N�Z�T��	#type8���ނ̒�`
	type9	�n�}		#type9���ނ̒�`
	type10	����		#type10���ނ̒�`
						#���̗l�Ɋg����
	
	job	drug		��	#���E�ƒ�`(�E�ƃR�[�h{�X�y�[�X}�E�Ɩ�) �E�ƃR�[�h�͉p������10�����ȓ�
	job	tool		���	#�ȉ��J��Ԃ�(�g����)
	job	weapon		���퉮
	job	armor		�h�
	job	material	�R�t
	job	book		�{��
	job	cow			���_��
	job	peddle		�s���l
	
	# �E�ƕʎ��ԒZ�k�p�ϐ��ݒ�
	set job_drug_time_rate		2
	set job_tool_time_rate		2
	set job_weapon_time_rate	2
	set job_armor_time_rate		2
	set job_material_time_rate	2
	set job_book_time_rate		2
	set job_cow_time_rate		2
	set job_peddle_time_rate	2

	MaxMoney	999999999	#���ő厑��
	
	set NewShopMoney	100000					#�������� (@@FUNCNEW�ɂĎg�p)
	set NewShopTime		12*60*60				#����������(�b) (@@FUNCNEW�ɂĎg�p)
	set NewShopItem		��I���z���L�b�g:1	#�����������i (@@FUNCNEW�ɂĎg�p) ���� ���i��:��:���i��:��:...
	
	TimeEditShowcase	10m		#����I���쎞��
	TimeShopping		10m		#���d�����ԁ�2001-06-06�p�~
	TimeSendItem		30m		#���A�C�e���d��/���M����(��{)��2001-06-06�ǉ�
	TimeSendItemPlus	20s		#���A�C�e���d��/���M����(1�ӂ�̒ǉ�����)��2001-06-06�ǉ���2001-07-29�p�~
	TimeSendMoney		20m		#���������M����(��{)��2001-06-06�ǉ�
	TimeSendMoneyPlus	50000	#���������v���Ԍv�Z�p���z(���̋��z�ɂ�TimeSendMoney���Ԃ�����)��2001-06-06�ǉ�
	
	CostShowcase1		0		#����I1���ێ���
	CostShowcase2		2000	#��I2���ێ���
	CostShowcase3		5000	#��I3���ێ���
	CostShowcase4		30000	#��I4���ێ���
	CostShowcase5		100000	#��I5���ێ���
	CostShowcase6		200000	#��I6���ێ���
	CostShowcase7		400000	#��I7���ێ���
	CostShowcase8		1000000	#��I8���ێ���
	
	ItemUseTimeRate		1		#���A�C�e���g�p�����Ԍv�Z�␳�{��(@USE��time,exptime�ɗL��)��2001-06-06�ǉ�
	
	#���}�N����`
	#  ���̋L�q��ł́A�ϐ� TOWN_TYPE (_config.cgi��$TOWN_TYPE) �𔻒f���Ď��ԏ���p�^�[����ύX���܂��B
	#  sotype1  -> [���H�^�C�v] ���H���ԒZ�k�p�^�[��     (MUTOYS�̃g�p�[�Y�X)
	#  sotype2  -> [�����^�C�v] �f�ލ̎掞�ԒZ�k�p�^�[�� (MUTOYS�̃g�p�[�Y�x�O)
	#  timehalf -> [��i�^�C�v] �S���ԒZ�k�p�^�[��       (MUTOYS�̃A���W�X�g�X)
	#  ���̑�   -> [�r��^�C�v] �ʏ펞�ԃp�^�[��         (MUTOYS�̃K�[�l�b�g�X)
	#
	#�����Őݒ肳�ꂽ�}�N���́A�u@@IF towntype eq material @@USEMACRO_timechange�v�̗l�Ȏg���������܂��B
	#����ƁAtowntype �� material �̏ꍇ�̂݁A�}�N�� _timechange �����s����A�ȍ~�̎��Ԃ��Z�k����܂��B
	#�}�N�� _timenormal �Ŏ��Ԃ����ɖ߂�܂��B(timehalf�ȊO)
	#
	#���̎d�g�݂𗝉�����ɂ̓v���O�����̒m�����K�v�ɂȂ�Ǝv���܂��B
	#��L�����Ŏg�p���@��������Ȃ��ꍇ�́A���t���Ȃ���������ł��B
	#
	
	set	TOWN_TYPE	$$TOWN_TYPE	#��_config.cgi�Ŏw�肵���X�^�C�v���擾/�ݒ�
	@@IF TOWN_TYPE eq timeharf set TOWN_TYPE timehalf # ver.2002-01-01-a �܂łƂ̌݊��m��
	
	set towntype normal                           # �ϐ� towntype �� normal �ŏ���������
	@@IF TOWN_TYPE eq sotype1 set towntype manufac  # TOWN_TYPE �� sotype1 �Ȃ�ϐ� towntype �� manufac �ɂ���
	@@IF TOWN_TYPE eq sotype2 set towntype material # TOWN_TYPE �� sotype2 �Ȃ�ϐ� towntype �� material �ɂ���
	#�}�N����`
	@@SETMACRO _timenormal "@@DEFINE ItemUseTimeRate 1"
	@@IF TOWN_TYPE eq timehalf @@SETMACRO _timenormal "@@DEFINE ItemUseTimeRate 0.5" # TOWN_TYPE �� timehalf �̏ꍇ�̃}�N����`
	@@IF TOWN_TYPE eq timequarter @@SETMACRO _timenormal "@@DEFINE ItemUseTimeRate 0.25" # TOWN_TYPE �� timequarter �̏ꍇ�̃}�N����`
	@@SETMACRO _timechange "@@DEFINE ItemUseTimeRate 0.75"
	#�}�N�� _timenormal ���s
	@@USEMACRO _timenormal

#���ȉ��̗l�ȏ����ŊX�^�C�v�𔻒肵�A�}�N�������s�ł����肵�܂��B
@@IF towntype eq material @@USEMACRO_timechange #-------------------------------------------------

@@ITEM				#���A�C�e���f�[�^��`�錾
	no		10				#���A�C�e���ԍ�(1~)
	type	����			#���A�C�e������(@@DEFINE��type?�̒�`���g�p)
	code	book-make		#���R�[�h(�A�C�e�������j�[�N)
	name	�{���M�L�b�g	#������
	info	�{�����M����ׂ̊�{�L�b�g	#������
	price	5000				#���W�����i
	cost	5000
	limit	10/5
	pop		1d				#������s�����(1d��1�����m��)
	scale	�Z�b�g			#�������P��
	plus	2h				#���s����ח�(2h��1���ׂ���m��)
	@@USE			#���A�C�e���g�p�f�[�^��`�錾
		time	6h			#�������
		exp		4%
		exptime	2h
		job		�{��	times/job_book_time_rate
		scale	��			#���g�p�s���P��
		action	����		#���s���\���p
		name	�w�򒲍�����x�����M����					#������
		info	��̍�����׋����A�{�ɂ��悤�Ǝv���܂�	#������
		okmsg	�w�򒲍�����x�����M���܂���				#���g�p���������b�Z�[�W
			use		1	�{���M�L�b�g	#���K�v�A�C�e��
			use		30	��			#  ��,�A�C�e������,����m��,������b�Z�[�W�̏��ň����L�q�B
			use		10	�|�[�V����		#  ����m���ȗ�����100%�B
			use		10	�G�[�e��		#  ���b�Z�[�W�ȗ��̓��b�Z�[�W�����B
			get		1	�򒲍�����		#���擾�A�C�e���B������use�Ɠ����B
	@@USE
		time	8h
		exp		5%
		exptime	3h
		job		�{��	times/job_book_time_rate
		name	�w�v�׍H����x�����M����
		info	�v�׍H�̍�����׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w�v�׍H����x�����M���܂���
			use		1	�{���M�L�b�g
			use		50	�b�̊v
			get		1	�v�׍H����
	@@USE
		time	8h
		exp		5%
		exptime	4h
		job		�{��	times/job_book_time_rate
		name	�w�؍H����x�����M����
		info	�؍H�̍�����׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w�؍H����x�����M���܂���
			use		1	�{���M�L�b�g
			use		50	�؂̎}
			use		10	�ۑ�
			get		1	�؍H�׍H����
	@@USE
		time	10h
		exp		3%
		exptime	5h
		job		�{��	times/job_book_time_rate
		name	�w�����׍H����x�����M����
		info	�����׍H�̋Z�p��׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w�����׍H����x�����M���܂���
			use		2	�{���M�L�b�g
			need	1	�v�׍H����
			need	1	�؍H�׍H����
			use		20	�S��
			use		5	�~�X������
			use		5	�I���n���R����
			get		1	�����׍H����
	@@USE
		time	12h
		exp		1%
		exptime	5h
		job		�{��	times/job_book_time_rate
		name	�w���̒b�����x�����M����
		info	���̒b������׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w���̒b�����x�����M���܂���
			needexp	20%
			need	1	�b�艮�̋Z�p	#���K�v�A�C�e���Buse�̏���m��0%�Œ�ŁB
			use		2	�{���M�L�b�g
			use		20	�S��
			use		1	�ؓ�
			get		1	���̒b����
	@@USE
		time	12h
		exp		1%
		exptime	5h
		job		�{��	times/job_book_time_rate
		name	�w���̍����x�����M����
		info	���̍\����׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w���̍����x�����M���܂���
			needexp	20%
			use		2	�{���M�L�b�g
			need	1	�b�艮�̋Z�p
			use		20	�S��
			use		1	�v�̏�
			get		1	���̍���
	@@USE
		time	12h
		exp		1%
		exptime	5h
		job		�{��	times/job_book_time_rate
		name	�w�Z�̍����x�����M����
		info	�Z�̍\����׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w�Z�̍����x�����M���܂���
			needexp	20%
			need	1	�b�艮�̋Z�p
			use		2	�{���M�L�b�g
			use		20	�S��
			use		1	�v�̋�����
			get		1	�Z�̍���
	@@USE
		time	12h
		exp		1%
		exptime	5h
		job		�{��	times/job_book_time_rate
		name	�w��̍����x�����M����
		info	��̍\����׋����A�{�ɂ��悤�Ǝv���܂�
		okmsg	�w��̍����x�����M���܂���
			needexp	20%
			need	1	���@�̒m��
			use		2	�{���M�L�b�g
			use		1	�؂̏�
			get		1	��̍���

@@ITEM
	no		37
	type	����
	code	book-syugyou
	name	�C�s�L�b�g
	info	�����ȏC�s�����邽�߂̃L�b�g
	price	10000
	cost	10000
	limit	3/1
	pop		1d
	scale	�Z�b�g
	plus	1d
	@@USE
		time	12h
		exp		5%
		scale	�C�s
		action	�C�s����
		name	�b�艮�ɒ�q����
		info	�b�艮�̋Z�p��׋����A�g�ɂ��悤�Ǝv���܂�
		okmsg	�b�艮�̋Z�p��g�ɂ��܂���
			use		1	�C�s�L�b�g
			use		20	�S��
			use		5	�~�X������
			use		3	�I���n���R����
			get		1	�b�艮�̋Z�p
	@@USE
		time	12h
		exp		5%
		scale	�׋�
		action	�C�s����
		name	���@�̊�b�u��
		info	���@�̊�b�ɂ��ĕ׋����A�g�ɂ��悤�Ǝv���܂�
		okmsg	���@�̊�b�����������܂�܂���
			use		1	�C�s�L�b�g
			use		30	����
			get		1	���@�̒m��
	@@USE
		time	12h
		exp		5%
		scale	�J��
		action	�J�Ⴗ��
		name	�Ⴂ��������j(��)�ɂȂ�
		info	���i�̈Ⴂ�����ɂ߁A��������ڂ�{�����Ǝv���܂�
		okmsg	�Ⴂ��������j(��)�ɂȂ����C������
			needexp	20%
			use		1	�C�s�L�b�g
			use		3	��
			use		3	�b�̊v
			use		3	�؂̎}
			use		3	�ۑ�
			use		3	�S��
			use		3	�~�X������
			use		3	�I���n���R����
			use		3	����
			get		1	�ڗ����̐^��
	@@USE
		time	12h
		exp		5%
		scale	�C�s
		action	�C�s����
		name	�o���V�̋Ɉӂ��w��ł݂�
		info	�������邱�Ƃɖ��������Ă݂܂��񂩁H
		okmsg	�Ȃ�ł��o������C�����邼
			use		1	�C�s�L�b�g
			use		20	�v�̋�����
			use		20	�v�̏�
			use		20	�؂̏�
			use		20	�ؓ�
			get		1	��̉��̍�

@@USEMACRO_timenormal #-----------------------------------------------------------------------------


@@ITEM
	no		39
	type	����
	code	book-kaitai
	name	���/����L�b�g
	info	��̂⍫���ƂɕK�v�ȃL�b�g
	price	500
	limit	10/3
	pop		2d
	scale	�Z�b�g
	plus	5h
	@@USE
		name	�ؓ�/�؂̏����̂���
		time	4h
		exptime	2h
		exp		1%
		job		���퉮	times/job_weapon_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�ؓ�
		use		10	�؂̏�
		get		50	�؂̎}	80%
	@@USE
		name	�v�̏�/�����Ă���̂���
		time	4h
		exptime	2h
		exp		1%
		job		�h�	times/job_armor_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�v�̏�
		use		10	�v�̋�����
		get		50	�b�̊v	80%
	@@USE
		name	�؂̏�/�����Ă���̂���
		time	4h
		exptime	2h
		exp		1%
		job		�h�	times/job_armor_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�؂̏�
		use		10	�؂̋�����
		get		50	�؂̎}	80%
	@@USE
		name	�S�̌�/�����̂���
		time	4h
		exptime	3h
		exp		1%
		job		���퉮	times/job_weapon_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�S�̌�
		use		10	�S�̏�
		get		50	�S��	80%
		get		10	����	50%
	@@USE
		name	�S�̏�/�Z����̂���
		time	4h
		exptime	3h
		exp		1%
		job		�h�	times/job_armor_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�S�̏�
		use		10	�S�̊Z
		get		50	�S��	80%
	@@USE
		name	�|�S�̌�/�����̂���
		time	5h
		exptime	3.5h
		exp		1%
		job		���퉮	times/job_weapon_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�|�S�̌�
		use		10	�|�S�̏�
		get		100	�S��	80%
		get		10	����	50%
	@@USE
		name	�|�S�̏�/�Z����̂���
		time	5h
		exptime	3.5h
		exp		1%
		job		�h�	times/job_armor_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�|�S�̏�
		use		10	�|�S�̊Z
		get		100	�S��	80%
	@@USE
		name	�~�X�����̌�/�����̂���
		time	6h
		exptime	4h
		exp		1%
		job		���퉮	times/job_weapon_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�~�X�����̌�
		use		10	�~�X�����̏�
		get		50	�~�X������	70%
		get		20	����	50%
	@@USE
		name	�~�X�����̏�/�Z����̂���
		time	6h
		exptime	4h
		exp		1%
		job		�h�	times/job_armor_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�~�X�����̏�
		use		10	�~�X�����̊Z
		get		50	�~�X������	70%
	@@USE
		name	�I���n���R���̌�/�����̂���
		time	7h
		exptime	5h
		exp		1%
		job		���퉮	times/job_weapon_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�I���n���R���̌�
		use		10	�I���n���R���̏�
		get		50	�I���n���R����	60%
		get		30	����	50%
	@@USE
		name	�I���n���R���̏�/�Z����̂���
		time	7h
		exptime	5h
		exp		1%
		job		�h�	times/job_armor_time_rate
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		10	�I���n���R���̏�
		use		10	�I���n���R���̊Z
		get		50	�I���n���R����	60%
	@@USE
		name	���{�b�g����̂���
		time	12h
		use		1	���/����L�b�g
		need	1	��̉��̍�
		use		1	�X�ԃ��{�b�g
		get		300	�S��
		get		50	�~�X������
		get		10	�I���n���R����
		get		30	����
		get		1	�֒f�̏�
		get		1	�ۑ�
	@@USE
		name	�v�������ꎮ�������
		time	4h
		exptime	2h
		exp		1%
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		10	�v�̏�
		use		10	�v�̋�����
		get		10	�v�������ꎮ
	@@USE
		name	�ؐ������ꎮ�������
		time	5h
		exptime	3h
		exp		1%
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		10	�ؓ�
		use		10	�؂̏�
		use		10	�؂̋�����
		use		10	�؂̏�
		get		10	�ؐ������ꎮ
	@@USE
		name	�S�������ꎮ�������
		time	6h
		exptime	4h
		exp		1%
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		10	�S�̌�
		use		10	�S�̏�
		use		10	�S�̊Z
		use		10	�S�̏�
		get		10	�S�������ꎮ
	@@USE
		name	�|�S�������ꎮ�������
		time	7h
		exptime	4.5h
		exp		1%
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		10	�|�S�̌�
		use		10	�|�S�̏�
		use		10	�|�S�̊Z
		use		10	�|�S�̏�
		get		10	�|�S�������ꎮ
	@@USE
		name	�~�X�����������ꎮ�������
		time	8h
		exptime	5h
		exp		1%
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		10	�~�X�����̌�
		use		10	�~�X�����̏�
		use		10	�~�X�����̊Z
		use		10	�~�X�����̏�
		get		10	�~�X�����������ꎮ
	@@USE
		name	�I���n���R���������ꎮ�������
		time	9h
		exptime	6h
		exp		1%
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		10	�I���n���R���̌�
		use		10	�I���n���R���̏�
		use		10	�I���n���R���̊Z
		use		10	�I���n���R���̏�
		get		10	�I���n���R���������ꎮ
	@@USE
		name	���j���O�b�Y�������
		time	8h
		job		���	times/job_tool_time_rate
		use		1	���/����L�b�g
		use		1	���ʒ��̊ۏĂ�
		use		1	�������̃�����
		use		1	�������u�[�c
		get		1	���j���Z�b�g



@@IF towntype eq manufac @@USEMACRO_timechange #----------------------------------------------------

@@ITEM
	no		15
	type	�{
	code	book-tyougou
	name	�򒲍�����
	info	��𒲍����邽�߂̋Z�p���ł�
	price	15000
	limit	10/1	#�������ő吔�i�����p�^�[��2�j/�̉E���͎s����׍ő吔(1�X�܂�����)
					#  10�X�܂̃Q�[�����ƁA���̗�ł͎s��ɂ͍ő�20���ׂ���B
					#  �܂��A�����̏ꍇ�͐�ΐ��ƂȂ�B(10/-2�Ȃ�s��ɂ͍ő�2��)
					#  �s��ő吔���w�肵�Ȃ������p�^�[��1�̏ꍇ�́A�����ő吔�Ɠ����B
	pop		2d
	plus	20d
	scale	��
	cost	200
	@@use
		time	1h
		exp		1%		#���g�p1��œ�����o���|�C���g�B�i�o���|�C���g�̓A�C�e�����j
		exptime	40m		#���o���|�C���g100%�̏ꍇ�̏����
		job		��	times/job_drug_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�|�[�V�������쐬����
		info	�|�[�V�������쐬���܂���܂�
		okmsg	�|�[�V����������������܂���
		ngmsg	�쐬�Ɏ��s���܂����c	#���擾�A�C�e�����Ȃ������ꍇ�̃��b�Z�[�W
		func	lostbook				#���Ǝ��֐��Ăяo��(inc-item-function.cgi�Œ�`)
		param	50
			use		20	��
			get		20	�|�[�V����	80%
	@@use
		time	1h
		exp		1%
		exptime	40m
		job		��	times/job_drug_time_rate
		name	�n�C�|�[�V�������쐬����
		info	�n�C�|�[�V�������쐬���܂���܂�
		okmsg	�n�C�|�[�V���������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	70
			needexp	20%
			use		20	�|�[�V����
			get		10	�n�C�|�[�V����	90%
	@@use
		time	1h
		exp		1%
		exptime	40m
		job		��	times/job_drug_time_rate
		name	�G�[�e�����쐬����
		info	�G�[�e�����쐬���܂���܂�
		okmsg	�G�[�e�������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	70
			needexp	20%
			use		20	��
			get		10	�G�[�e��	90%
	@@use
		time	1h
		exp		1%
		exptime	40m
		job		��	times/job_drug_time_rate
		name	�n�C�G�[�e�����쐬����
		info	�n�C�G�[�e�����쐬���܂���܂�
		okmsg	�n�C�G�[�e�������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	40%
			use		20	�G�[�e��
			get		10	�n�C�G�[�e��	90%
	@@use
		time	1h
		exp		1%
		exptime	40m
		job		��	times/job_drug_time_rate
		name	�G�������쐬����
		info	�G�������쐬���܂���܂�
		okmsg	�G���������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	150
			needexp	80%
			use		10	�n�C�|�[�V����
			use		10	�n�C�G�[�e��
			get		1	�G����
@@ITEM
	no		16
	type	�{
	code	book-kawazaiku
	name	�v�׍H����
	info	�v�׍H�t��ڎw���l��
	price	25000
	limit	10/1
	pop		2d
	plus	20d
	scale	��
	cost	500
	@@use
		time	1h
		exp		1%
		exptime	30m
		job		�h�	times/job_armor_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�v�̏����쐬����
		info	�v�̏����쐬���܂�
		okmsg	�v�̏������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	50
			use		20	�b�̊v
			get		20	�v�̏�	90%
	@@use
		time	1h
		exptime	30m
		job		�h�	times/job_armor_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�v�̋����Ă��쐬����
		info	�v�̋����Ă��쐬���܂�
		okmsg	�v�̋����Ă����܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			use		30	�b�̊v
			get		20	�v�̋�����	80%
@@ITEM
	no		17
	type	�{
	code	book-mokkouzaiku
	name	�؍H�׍H����
	info	�؍H�׍H�t��ڎw���l��
	price	25000
	limit	10/1
	pop		2d
	plus	20d
	#base	10/100
	scale	��
	cost	500
	@@use
		time	1h
		exp		1%
		exptime	30m
		job		���퉮	times/job_weapon_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�ؓ����쐬����
		info	�ؓ����쐬���܂�
		okmsg	�ؓ������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	50
			use		20	�؂̎}
			get		20	�ؓ�	90%
	@@use
		time	1h
		exptime	30m
		job		���퉮	times/job_weapon_time_rate
		name	�؂̏���쐬����
		info	�؂̏���쐬���܂�
		okmsg	�؂̏�����܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			use		20	�؂̎}
			get		20	�؂̏�	80%
	@@use
		time	2h
		exptime	1h
		job		�h�	times/job_armor_time_rate
		name	�؂̏����쐬����
		info	�؂̏����쐬���܂�
		okmsg	�؂̏������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	30%
			use		4	�ۑ�
			get		20	�؂̏�	90%
	@@use
		time	2h
		exp		1%
		exptime	1h
		job		�h�	times/job_armor_time_rate
		name	�؂̋����Ă��쐬����
		info	�؂̋����Ă��쐬���܂�
		okmsg	�؂̋����Ă����܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	30%
			use		4	�ۑ�
			get		16	�؂̋�����	80%

@@ITEM
	no		66
	type	�{
	code	book-sousyoku
	name	�����׍H����
	info	�����׍H�t��ڎw���l��
	price	40000
	limit	10/2
	pop		2d
	plus	20d
	scale	��
	cost	1000
	@@use
		time	3h
		exp		1%
		exptime	2h
		job		���	times/job_tool_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�S�̃s�A�X���쐬����
		info	�S�̃s�A�X���쐬���܂���܂�
		okmsg	�S�̃s�A�X������������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	60
			need	1	�b�艮�̋Z�p
			need	1	���@�̒m��
			use		20	�S��
			get		20	�S�̃s�A�X	80%
	@@use
		time	4h
		exp		1%
		exptime	3h
		job		���	times/job_tool_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�~�X�����̎w�ւ��쐬����
		info	�~�X�����̎w�ւ��쐬���܂���܂�
		okmsg	�~�X�����̎w�ւ�����������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	80
			need	1	�b�艮�̋Z�p
			need	1	���@�̒m��
			use		20	�~�X������
			use		2	����
			get		20	�~�X�����̎w��	60%
	@@use
		time	5h
		exp		1%
		exptime	4h
		job		���	times/job_tool_time_rate
		scale	�Z�b�g
		action	���܂���
		name	�I���n���R���̘r�ւ��쐬����
		info	�I���n���R���̘r�ւ��쐬���܂���܂�
		okmsg	�I���n���R���̘r�ւ�����������܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			need	1	�b�艮�̋Z�p
			need	1	���@�̒m��
			use		20	�I���n���R����
			use		2	����
			get		20	�I���n���R���̘r��	30%
	@@use
		time	6h
		exp		1%
		exptime	5h
		job		���	times/job_tool_time_rate
		scale	�Z�b�g
		action	���グ��
		name	$HERO_NAME�̎������쐬����		#��$HERO_NAME���Q��
		info	$HERO_NAME�̎��������グ�܂�
		okmsg	�`�������A�ڂ̑O�ɁI
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	200
			need	1	�b�艮�̋Z�p
			need	1	���@�̒m��
			need	1	�ڗ����̐^��
			use		20	�S��
			use		20	�~�X������
			use		20	�I���n���R����
			use		6	����
			get		1	$HERO_NAME�̎����
	
@@ITEM
	no		20
	type	�{
	code	book-ken
	name	���̒b����
	info	����̑�\�u���v�̒b����
	price	50000
	limit	5/0.2
	pop		3d
	plus	80d
	scale	��
	cost	800
	@@use
		time	2h
		exp		2%
		exptime	1h
		job		���퉮	times/job_weapon_time_rate
		scale	�Z�b�g
		action	�b����
		name	�S�̌���b����
		info	�I�[�\�h�b�N�X�ȓS�̌���b���Ă݂܂��傤
		okmsg	�S�̌���b���܂���
		ngmsg	�b����̂Ɏ��s���܂����c
		func	lostbook
		param	100
			need	1	�b�艮�̋Z�p
			use		20	�S��
			get		20	�S�̌�	80%
	@@use
		time	4h
		exptime	2h
		job		���퉮	times/job_weapon_time_rate
		name	�|�S�̌���b����
		info	�|�S�̌���b���Ă݂܂��傤
		okmsg	�|�S�̌���b���܂���
		ngmsg	�b����̂Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	20%
			need	1	�b�艮�̋Z�p
			use		40	�S��
			get		20	�|�S�̌�	80%
	@@use
		time	4h
		exptime	3h
		job		���퉮	times/job_weapon_time_rate
		name	�~�X�����̌���b����
		info	�㋉�`���҂̌�p�B�A�~�X�����̌���b���Ă݂܂��傤
		okmsg	�~�X�����̌���b���܂���
		ngmsg	�b����̂Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	40%
			need	1	�b�艮�̋Z�p
			use		20	�~�X������
			get		20	�~�X�����̌�	60%
	@@use
		time	6h
		exptime	4h
		job		���퉮	times/job_weapon_time_rate
		name	�I���n���R���̌���b����
		info	�߂����Ɏ�ɓ���Ȃ��A�I���n���R���̌���b���Ă݂܂��傤
		okmsg	�I���n���R���̌���b���܂���
		ngmsg	�b����̂Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	60%
			need	1	�b�艮�̋Z�p
			use		20	�I���n���R����
			get		20	�I���n���R���̌�	30%
@@ITEM
	no		21
	type	�{
	code	book-tate
	name	���̍���
	info	����n�h�䑕���u���v�̍���
	price	50000
	limit	5/0.2
	pop		3d
	plus	80d
	scale	��
	cost	800
	@@use
		time	2h
		exp		2%
		exptime	1h
		job		�h�	times/job_armor_time_rate
		scale	�Z�b�g
		action	�쐬����
		name	�S�̏����쐬����
		info	�I�[�\�h�b�N�X�ȓS�̏����쐬���Ă݂܂��傤
		okmsg	�S�̏����쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			need	1	�b�艮�̋Z�p
			use		20	�S��
			get		20	�S�̏�	80%
	@@use
		time	4h
		exptime	2h
		job		�h�	times/job_armor_time_rate
		name	�|�S�̏����쐬����
		info	�|�S�̏����쐬���Ă݂܂��傤
		okmsg	�|�S�̏����쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	40%
			need	1	�b�艮�̋Z�p
			use		40	�S��
			get		20	�|�S�̏�	80%
	@@use
		time	4h
		exptime	3h
		job		�h�	times/job_armor_time_rate
		name	�~�X�����̏����쐬����
		info	�㋉�`���҂̌�p�B�A�~�X�����̏����쐬���Ă݂܂��傤
		okmsg	�~�X�����̏����쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	60%
			need	1	�b�艮�̋Z�p
			use		20	�~�X������
			get		20	�~�X�����̏�	60%
	@@use
		time	6h
		exptime	4h
		job		�h�	times/job_armor_time_rate
		name	�I���n���R���̏����쐬����
		info	�߂����Ɏ�ɓ���Ȃ��A�I���n���R���̏����쐬���Ă݂܂��傤
		okmsg	�I���n���R���̏����쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	80%
			need	1	�b�艮�̋Z�p
			use		20	�I���n���R����
			get		20	�I���n���R���̏�	30%
@@ITEM
	no		22
	type	�{
	code	book-yoroi
	name	�Z�̍���
	info	�ό��n�h�䑕���u�Z�v�̍���
	price	50000
	limit	5/0.2
	pop		3d
	plus	80d
	scale	��
	cost	800
	@@use
		time	2h
		exp		2%
		exptime	1h
		job		�h�	times/job_armor_time_rate
		scale	�Z�b�g
		action	�쐬����
		name	�S�̊Z���쐬����
		info	�I�[�\�h�b�N�X�ȓS�̊Z���쐬���Ă݂܂��傤
		okmsg	�S�̊Z���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			need	1	�b�艮�̋Z�p
			use		20	�S��
			get		20	�S�̊Z	80%
	@@use
		time	4h
		exptime	2h
		job		�h�	times/job_armor_time_rate
		name	�|�S�̊Z���쐬����
		info	�|�S�̊Z���쐬���Ă݂܂��傤
		okmsg	�|�S�̊Z���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	10%
			need	1	�b�艮�̋Z�p
			use		40	�S��
			get		20	�|�S�̊Z	80%
	@@use
		time	4h
		exptime	3h
		job		�h�	times/job_armor_time_rate
		name	�~�X�����̊Z���쐬����
		info	�㋉�`���҂̌�p�B�A�~�X�����̊Z���쐬���Ă݂܂��傤
		okmsg	�~�X�����̊Z���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	50%
			need	1	�b�艮�̋Z�p
			use		20	�~�X������
			get		20	�~�X�����̊Z	60%
	@@use
		time	6h
		exptime	4h
		job		�h�	times/job_armor_time_rate
		name	�I���n���R���̊Z���쐬����
		info	�߂����Ɏ�ɓ���Ȃ��A�I���n���R���̊Z���쐬���Ă݂܂��傤
		okmsg	�I���n���R���̊Z���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	80%
			need	1	�b�艮�̋Z�p
			use		20	�I���n���R����
			get		20	�I���n���R���̊Z	30%
@@ITEM
	no		23
	type	�{
	code	book-tue
	name	��̍���
	info	���@�n�U�������u��v�̍���
	price	50000
	limit	5/0.2
	pop		3d
	plus	80d
	scale	��
	cost	1000
	@@use
		time	2h
		exp		2%
		exptime	1h
		job		���퉮	times/job_weapon_time_rate
		scale	�Z�b�g
		action	�쐬����
		name	�S�̏���쐬����
		info	�I�[�\�h�b�N�X�ȓS�̏���쐬���Ă݂܂��傤
		okmsg	�S�̏���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			need	1	���@�̒m��
			use		20	�S��
			use		2	����
			get		20	�S�̏�	80%
	@@use
		time	4h
		exptime	2h
		job		���퉮	times/job_weapon_time_rate
		name	�|�S�̏���쐬����
		info	�|�S�̏���쐬���Ă݂܂��傤
		okmsg	�|�S�̏���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	60%
			need	1	���@�̒m��
			use		40	�S��
			use		4	����
			get		20	�|�S�̏�	80%
	@@use
		time	4h
		exptime	3h
		job		���퉮	times/job_weapon_time_rate
		name	�~�X�����̏���쐬����
		info	�㋉�`���҂̌�p�B�A�~�X�����̏���쐬���Ă݂܂��傤
		okmsg	�~�X�����̏���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	75%
			need	1	���@�̒m��
			use		20	�~�X������
			use		6	����
			get		20	�~�X�����̏�	60%
	@@use
		time	7h
		exptime	5h
		job		���퉮	times/job_weapon_time_rate
		name	�I���n���R���̏���쐬����
		info	�߂����Ɏ�ɓ���Ȃ��A�I���n���R���̏���쐬���Ă݂܂��傤
		okmsg	�I���n���R���̏���쐬���܂���
		ngmsg	�쐬�Ɏ��s���܂����c
		func	lostbook
		param	100
			needexp	90%
			need	1	���@�̒m��
			use		20	�I���n���R����
			use		10	����
			get		20	�I���n���R���̏�	30%

@@USEMACRO_timenormal #-----------------------------------------------------------------------------
	
@@ITEM
	no		30
	type	��
	code	posyon
	name	�|�[�V����
	info	��̈��
	price	50
	limit	2000/1000
	pop		10m
	plus	300m
	base	500/1500	#���s��ł̉��i�ϓ��p�B�����͊��/���z���B
						#  �݌ɂ�������͕W�����i�ŁA���z�����ɔ��z�ɂȂ�B
						#  ���̔䗦�ŁA����ȉ��̏ꍇ�̓v���~�A���t���B
	scale	��
	cost	10			#��1������̈ێ���z�B���ݒ莞��1/10�������ݒ肳���B
	point	10%
@@ITEM
	no		31
	type	��
	code	posyon-hi
	name	�n�C�|�[�V����
	info	��̈��
	price	250
	limit	1000/500
	base	400/1000
	plus	-1h
	pop		30m
	scale	��
	point	70%
@@ITEM
	no		32
	type	��
	code	eteru
	name	�G�[�e��
	info	��̈��
	price	250
	limit	1000/500
	pop		40m
	plus	400m
	base	400/1000
	scale	��
	cost	30
	point	20%
@@ITEM
	no		33
	type	��
	code	eteru-hi
	name	�n�C�G�[�e��
	info	��̈��
	price	500
	limit	700/350
	base	200/500
	plus	-1h
	pop		80m
	scale	��
	cost	50
@@ITEM
	no		34
	type	��
	code	erikusa
	name	�G����
	info	��̈��
	price	10000
	base	10/20
	plus	-1h
	limit	20
	pop		4h
	scale	��
	cost	800
@@ITEM
	no		40
	type	��
	code	ken-ki
	name	�ؓ�
	info	���y�Y�ɍœK
	price	400
	limit	1000			#�������ő吔�i�����p�^�[��1�j
	base	100/200
	plus	-1h
	pop		1h
	scale	�{
	point	90%		#�����p���̐l�C�㏸���␳�B100%�Ł}0�B
					#  ���ݒ莞��100%�B
@@ITEM
	no		41
	type	��
	code	ken-tetu
	name	�S�̌�
	info	�S�̌�
	price	1000
	limit	500
	base	50/100
	plus	-1h
	pop		3h
	scale	�{
	point	90%
@@ITEM
	no		42
	type	��
	code	ken-hagane
	name	�|�S�̌�
	info	�|�S�̌�
	price	3000
	limit	300
	base	30/60
	plus	-1h
	pop		5h
	scale	�{
	point	80%
@@ITEM
	no		43
	type	��
	code	ken-misuriru
	name	�~�X�����̌�
	info	�~�X�����̌�
	price	8000
	limit	100
	base	20/40
	plus	-1h
	pop		1d
	scale	�{
	point	70%
@@ITEM
	no		44
	type	��
	code	ken-oriharukon
	name	�I���n���R���̌�
	info	�I���n���R���̌�
	price	15000
	limit	50
	base	10/20
	plus	-1h
	pop		2d
	scale	�{
	point	50%

@@ITEM
	no		45
	type	��
	code	tate-kawa
	name	�v�̏�
	info	�������̓}�V
	price	300
	limit	1000
	base	100/200
	plus	-1h
	pop		40m
	scale	��
@@ITEM
	no		46
	type	��
	code	tate-ki
	name	�؂̏�
	info	�q���̗��K�p
	price	800
	limit	1000
	base	100/200
	plus	-1h
	pop		1h
	scale	��
@@ITEM
	no		47
	type	��
	code	tate-tetu
	name	�S�̏�
	info	�S�̏�
	price	1100
	limit	500
	base	50/100
	plus	-1h
	pop		3h
	scale	��
@@ITEM
	no		48
	type	��
	code	tate-hagane
	name	�|�S�̏�
	info	�|�S�̏�
	price	2800
	limit	300
	base	30/60
	plus	-1h
	pop		5h
	scale	��
@@ITEM
	no		49
	type	��
	code	tate-misuriru
	name	�~�X�����̏�
	info	�~�X�����̏�
	price	7500
	limit	100
	base	20/40
	plus	-1h
	pop		1d
	scale	��
@@ITEM
	no		50
	type	��
	code	tate-oriharukon
	name	�I���n���R���̏�
	info	�I���n���R���̏�
	price	12000
	limit	50
	base	10/20
	plus	-1h
	pop		2d
	scale	��


@@ITEM
	no		51
	type	�Z
	code	yoroi-kawa
	name	�v�̋�����
	info	�h�����ʂ��疳��
	price	500
	limit	1000
	base	100/200
	plus	-1h
	pop		50m
	scale	��
@@ITEM
	no		52
	type	�Z
	code	yoroi-ki
	name	�؂̋�����
	info	���낤���ċ�����
	price	900
	limit	1000
	base	100/200
	plus	-1h
	pop		1h
	scale	��
@@ITEM
	no		53
	type	�Z
	code	yoroi-tetu
	name	�S�̊Z
	info	�S�̊Z
	price	1200
	limit	500
	base	50/100
	plus	-1h
	pop		3h
	scale	��
@@ITEM
	no		54
	type	�Z
	code	yoroi-hagane
	name	�|�S�̊Z
	info	�|�S�̊Z
	price	3500
	limit	300
	base	30/60
	plus	-1h
	pop		5h
	scale	��
@@ITEM
	no		55
	type	�Z
	code	yoroi-misuriru
	name	�~�X�����̊Z
	info	�~�X�����̊Z
	price	9000
	limit	100
	base	20/40
	plus	-1h
	pop		1d
	scale	��
@@ITEM
	no		56
	type	�Z
	code	yoroi-oriharukon
	name	�I���n���R���̊Z
	info	�I���n���R���̊Z
	price	18000
	limit	50
	base	10/20
	plus	-1h
	pop		2d
	scale	��

@@ITEM
	no		57
	type	��
	code	tue-ki
	name	�؂̏�
	info	��������̏�
	price	300
	limit	1000
	base	100/200
	plus	-1h
	pop		2h
	scale	�{
	point	200%
@@ITEM
	no		58
	type	��
	code	tue-tetu
	name	�S�̏�
	info	�S�̏�
	price	1100
	limit	500
	base	50/100
	plus	-1h
	pop		5h
	scale	�{
	point	200%
@@ITEM
	no		59
	type	��
	code	tue-hagane
	name	�|�S�̏�
	info	�|�S�̏�
	price	3300
	limit	300
	base	30/60
	plus	-1h
	pop		8h
	scale	�{
	point	210%
@@ITEM
	no		60
	type	��
	code	tue-misuriru
	name	�~�X�����̏�
	info	�~�X�����̏�
	price	10000
	limit	100
	base	20/40
	plus	-1h
	pop		1.5d
	scale	�{
	point	220%
@@ITEM
	no		61
	type	��
	code	tue-oriharukon
	name	�I���n���R���̏�
	info	�I���n���R���̏�
	price	20000
	limit	50
	base	10/20
	plus	-1h
	pop		4d
	scale	�{
	point	230%


@@ITEM
	no		67
	type	�A�N�Z�T��
	code	sousyoku-tetu
	name	�S�̃s�A�X
	info	���芴����s�A�X�ł�
	price	750
	limit	100/0
	pop		3h
	base	20/30
	scale	��
	cost	50
@@ITEM
	no		68
	type	�A�N�Z�T��
	code	sousyoku-misuriru
	name	�~�X�����̎w��
	info	�~�X�����̎w��
	price	1500
	limit	100/0
	pop		6h
	base	20/30
	scale	��
	cost	75
@@ITEM
	no		69
	type	�A�N�Z�T��
	code	sousyoku-oriharukon
	name	�I���n���R���̘r��
	info	�I���n���R���̘r��
	price	3000
	limit	100/0
	pop		12h
	base	20/30
	scale	��
	cost	100
@@ITEM
	no		70
	type	�A�N�Z�T��
	code	sousyoku-nayuta
	name	$HERO_NAME�̎����
	info	�`���̉p�Y���̂��������
	price	50000
	limit	1/0
	pop		2d
	scale	��
	cost	200
	flag	nobuy
	funct	_local_
		#�V���E�E�B���h�E�ɕW�����i�����Œ񒆂̏ꍇ1��10%�̖������l�C�A�b�v
		my($ITEM,@DT)=@_;
		my $rankup=$TIMESPAN/86.4;
		$rankup=$rankup<1 && rand(1)<$rankup ? 1 : int($rankup);
		return if !$rankup;
		foreach my $DT (@DT)
		{
			next if $DT->{showcase}[0]!=$ITEM->{no} || $DT->{price}[0]>$ITEM->{price};
			
			$DT->{rank}+=$rankup;
			$DT->{rank}=10000 if $DT->{rank}>10000;
			DebugLog("item $ITEM->{name} $DT->{shopname} �l�C +".($rankup/100)."\%");
		}
	_local_

@@ITEM
	no		71
	type	����
	code	soubiset-kawa
	name	�v�������ꎮ
	info	�v���̑������܂Ƃ߂��Z�b�g���i
	price	1800
	limit	500/0
	pop		2h
	scale	�Z�b�g
@@ITEM
	no		72
	type	����
	code	soubiset-ki
	name	�ؐ������ꎮ
	info	�ؐ��̑������܂Ƃ߂��Z�b�g���i
	price	3600
	limit	250/0
	pop		4h
	scale	�Z�b�g
@@ITEM
	no		73
	type	����
	code	soubiset-tetu
	name	�S�������ꎮ
	info	�S���̑������܂Ƃ߂��Z�b�g���i
	price	6600
	limit	100/0
	pop		8h
	scale	�Z�b�g
@@ITEM
	no		74
	type	����
	code	soubiset-hagane
	name	�|�S�������ꎮ
	info	�|�S���̑������܂Ƃ߂��Z�b�g���i
	price	18900
	limit	40/0
	pop		1d
	scale	�Z�b�g
@@ITEM
	no		75
	type	����
	code	soubiset-misuriru
	name	�~�X�����������ꎮ
	info	�~�X�������̑������܂Ƃ߂��Z�b�g���i
	price	51750
	limit	20/0
	pop		3d
	scale	�Z�b�g
@@ITEM
	no		76
	type	����
	code	soubiset-oriharukon
	name	�I���n���R���������ꎮ
	info	�I���n���R�����̑������܂Ƃ߂��Z�b�g���i
	price	97500
	limit	10/0
	pop		6d
	scale	�Z�b�g


@@ITEM
	no		1
	type	����
	code	yakusou
	name	��
	info	��ɂȂ鑐
	price	20
	limit	4000/400
	pop		20m
	plus	200m
	base	1000/10000
	scale	�{
	cost	20
	point	10%
@@ITEM
	no		2
	type	����
	code	kemononokawa
	name	�b�̊v
	info	�Ȃ߂����b�̖є�
	price	100
	limit	2000/500
	pop		40m
	plus	-20m
	base	100/700
	scale	��
	cost	30
@@ITEM
	no		3
	type	����
	code	kinoeda
	name	�؂̎}
	info	�r�̑������x�̎}
	price	200
	limit	2000/500
	pop		1h
	plus	-20m
	base	200/600
	scale	�{
	cost	40
@@ITEM
	no		4
	type	����
	code	maruta
	name	�ۑ�
	info	�ۑ�
	price	1200
	limit	500/100
	pop		4h
	plus	-20m
	base	100/500
	scale	�{
	cost	100
@@ITEM
	no		5
	type	����
	code	tetu
	name	�S��
	info	�S�̂����܂�
	price	1000
	limit	1000/300
	pop		3h
	plus	-20m		#���s�ꌸ����(10m��1����m��)
	base	300/800
	scale	kg
	cost	60
@@ITEM
	no		6
	type	����
	code	misuriru
	name	�~�X������
	info	�~�X�����̂����܂�
	price	2500
	limit	700/200
	pop		6h
	plus	-20m
	base	300/600
	scale	kg
	cost	80
@@ITEM
	no		7
	type	����
	code	oriharukon
	name	�I���n���R����
	info	�I���n���R���̂����܂�
	price	5000
	limit	500/150
	pop		12h
	plus	-20m
	base	300/600
	scale	kg
	cost	100
@@ITEM
	no		8
	type	����
	code	magicstone
	name	����
	info	���͂��������߂�ꂽ�z��
	price	1000
	limit	100/20
	pop		3h
	plus	6h
	base	100/500
	scale	��
	cost	100
#	point	300%

@@IF towntype eq material @@USEMACRO_timechange #-------------------------------------------------

@@ITEM
	no		12
	type	�n�}
	code	book-mtsearch
	name	�߂��̎R�ւ̒n�}
	info	�ޗ����B�ɂ͂����Ă����̎R�ł�
	price	10000
	limit	1/1
	pop		2d
	plus	1h
	scale	��
	cost	500
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�T�����ɍs��
		name	�R�̂ӂ��Ƃ�T��
		info	�����ȍޗ������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		100	��	90%	�򑐂��������񐶂��Ă��܂���
			get		5	�b�̊v	90%
			get		5	�؂̎}	90%
			get		5	�ۑ�	30%
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�T�����ɍs��
		name	�ѓ���T��
		info	�����ȍޗ������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		10	��	90%
			get		5	�b�̊v	90%
			get		50	�؂̎}	90%	�؂̎}���������񗎂��Ă��܂���
			get		5	�ۑ�	30%
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�T�����ɍs��
		name	�b����T��
		info	�ޗ������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		10	��	90%
			get		50	�b�̊v	90%	�b������������܂���
			get		5	�؂̎}	90%
			get		5	�ۑ�	30%
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�T�����ɍs��
		name	�G�ؗт̉���T��
		info	�ޗ������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		10	��	90%
			get		5	�b�̊v	90%
			get		5	�؂̎}	90%
			get		50	�ۑ�	30%		�ۑ����������񌩂���܂���
	
@@ITEM
	no		9
	type	�n�}
	code	book-metalsearch
	name	�߂��̍z�R�ւ̒n�}
	info	�e��z���̍̎悪�ł������ł�
	price	10000
	limit	1/0.7
	pop		2d
	plus	1h
	scale	��
	cost	1000
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�̎悵�ɍs��
		name	�S�z�R�֍s��
		info	�����ȍz�������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		30	�S��			80%
			get		2	�~�X������		60%
			get		1	�I���n���R����	40%
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�̎悵�ɍs��
		name	�~�X�����z�R�֍s��
		info	�����ȍz�������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		3	�S��			80%
			get		20	�~�X������		60%
			get		1	�I���n���R����	40%
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�R�t	times/job_material_time_rate
		scale	����
		action	�̎悵�ɍs��
		name	�I���n���R���z�R�֍s��
		info	�����ȍz�������B�ł��邩������܂���
		func	lostbook
		param	100
		ngmsg	�Ȃɂ�������܂���ł����c
			get		3	�S��			80%
			get		2	�~�X������		60%
			get		10	�I���n���R����	40%


@@USEMACRO_timenormal #-------------------------------------------------------------------------------

@@ITEM
	no		14
	type	�n�}
	code	shiire-ken
	name	���s�ւ̒n�}
	info	���̎s��܂ł̒n�}
	price	10000
	limit	1/0.5
	pop		2d
	plus	1h
	scale	��
	cost	1000
	@@use
		time	4h
		exp		1%
		exptime	2h
		job		�s���l	times/job_peddle_time_rate
		scale	����
		action	�d���ɍs��
		price	5000					#���g�p����p�z
		name	���̎s��֎d���ɍs��
		info	�����d���ɍs���܂�
		func	lostbook
		param	100
		ngmsg	�Ȃɂ��d������܂���ł����c
			get		10	�ؓ�				40%
			get		10	�S�̌�				35%
			get		10	�|�S�̌�			15%
			get		10	�~�X�����̌�		09%		�~�X�����̌������������ł�		#���擾�m��,���b�Z�[�W�t���̏����p�^�[��
			get		10	�I���n���R���̌�	03%		�I���n���R���̌����@��o�����Ƃ��ďo�Ă܂���!
		funcb	_local_
			# 1/10�̊m���Ŏ��n�ʂ�2�{�ɂȂ�
			return 0 if rand(1000)>100;
			
			my $USE=$_[0];
			
			# $USE->{result}->{create}->[0..?]->{count} ��2�{�ɂ���
			foreach(@{$USE->{result}->{create}})
			{
				$_->{count}*=2;
			}
			
			# okmsg ��ݒ肷��
			$USE->{result}->{message}->{resultok}='����͎��n��������葽�������ł�';
			return 0;
		_local_

@@ITEM
	no		62
	type	����
	code	cm
	name	�L���p�b�N
	info	���낢��ȕ��@�ōL�����ł��܂�
	price	50000
	limit	3/.1
	pop		7d
	plus	12h
	base	10/200
	scale	�p�b�N
	cost	1000
	@@use
		time	8h
		exp		10%
		price	0
		job		�s���l	times/job_peddle_time_rate
		scale	��
		action	�L������
		name	�r���z��ōL������
		info	�s���|�C���g�̍L�����@�ł�
		param	200,�L�����s���܂���
		func	popup
			use		1	�L���p�b�N
	@@use
		time	12h
		exp		10%
		job		�s���l	times/job_peddle_time_rate
		price	0
		name	�|�X�^�[�ōL������
		info	���ƕ��L���L���ł��܂�
		param	400,�L�����s���܂���
		func	popup
			use		1	�L���p�b�N
	@@use
		time	24h
		exp		10%
		job		�s���l	times/job_peddle_time_rate
		price	0
		name	�L�����y�[���ōL������
		info	��X�I�ɍL�����܂�
		param	1000,�L�����s���܂���
		func	popup
			use		1	�L���p�b�N
		

@@ITEM
	no		13
	type	�{
	code	book-work
	name	�������B�̕��@
	info	�������������K�v�ȂƂ��̓R��
	price	0
	limit	1
	pop		2d
	plus	1d
	scale	��
	@@use
		time	4h
		job		�s���l	times/job_peddle_time_rate
		scale	��
		action	����
		name	�e�B�b�V���z��Ŏ����҂�
		info	����y�ɉ҂��܂��傤
		param	3000
		func	_local_
			# ���o�C�g
			#   param1 �擾�z
			$DT->{money}+=$USE->{param1}*$count;
			
			my $ret='\\'.($USE->{param1}*$count).'�Q�b�g�I';
			
			WriteLog(0,$DT->{id},"�o�C�g���A$ret");
			WriteLog(3,0,$DT->{shopname}."���o�C�g�����悤�ł�");
			
			return $ret;
		_local_
	@@use
		time	8h
		job		�s���l	times/job_peddle_time_rate
		scale	��
		action	����
		name	���ق��y�؍�ƂŎ����҂�
		info	������Ƃ������ǂ��������̉҂��ł�
		param	10000
		func	_local_1

@@ITEM
	no		63
	type	����
	code	edit-showcase
	name	��I���z���L�b�g
	info	��I�̑��z����󂵓��ɕK�v�ȓ���ꎮ�ł�
	price	0
	limit	1
	pop		1d
	plus	1d
	scale	�L�b�g
	flag	noshowcase|nosend|notradein|notradeout		#�����i�ɓ��ꑮ����t���܂�
												#  �ȉ��̑����L�[���[�h���L�q���Ă��������B
												#  | �ŋ�؂邱�Ƃŕ����̑�����t���邱�Ƃ��\�ł�
												#  noshowcase : ��̔��s��
												#  nosend     : �X�֑��t�s��
												#  notrash    : �j���s��
												#  notradein  : �A���s��
												#  notradeout : �A�o�s��
												#  nobuy      : �w���s��(���X��I����)
	@@use
		time	1h
		scale	��
		action	��Ƃ���
		price	0
		name	��I��1�ɂ���
		info	��I��1�ɂ���
		arg		nocount		#���g�p���̑I�����w��B
							#  nocount -> �g�p�񐔑I���Ȃ�
		param	1			#���Ǝ��֐��p�p�����[�^
			use	1	��I���z���L�b�g
		func	_local_
			# ����I���ύX
			#   param1 �ύX��̒I��
			my $oldcnt=$DT->{showcasecount};
			my $newcnt=$USE->{param1};
			$DT->{showcasecount}=$newcnt;
			
			if($oldcnt<$newcnt)
			{
				foreach ($oldcnt..$newcnt-1)
				{
					$DT->{showcase}[$_]=0;
					$DT->{price}[$_]=0;
				}
			}
			if($oldcnt>$newcnt)
			{
				splice(@{$DT->{showcase}},$newcnt);
				splice(@{$DT->{price}},$newcnt);
			}
			my $ret="��I��$DT->{showcasecount}�ɂ��܂���";
			WriteLog(0,$DT->{id},$ret);
			WriteLog(3,0,$DT->{shopname}."�̒�I��$DT->{showcasecount}�ɂȂ�܂���");
			
			return $ret;
		_local_
	@@use
		time	2h
		price	10000
		name	��I��2�ɂ���
		info	��I��2�ɂ���
		func	_local_1
		arg		nocount
		param	2
			use	1	��I���z���L�b�g
	@@use
		time	4h
		price	50000
		name	��I��3�ɂ���
		info	��I��3�ɂ���
		func	_local_1
		arg		nocount
		param	3
			use	1	��I���z���L�b�g
	@@use
		time	8h
		price	150000
		name	��I��4�ɂ���
		info	��I��4�ɂ���
		func	_local_1
		arg		nocount
		param	4
			use	1	��I���z���L�b�g
	@@use
		time	16h
		price	400000
		name	��I��5�ɂ���
		info	��I��5�ɂ���
		func	_local_1
		arg		nocount
		param	5
			use	1	��I���z���L�b�g
	@@use
		time	32h
		price	800000
		name	��I��6�ɂ���
		info	��I��6�ɂ���
		func	_local_1
		arg		nocount
		param	6
			use	1	��I���z���L�b�g
	@@use
		time	40h
		price	1600000
		name	��I��7�ɂ���
		info	��I��7�ɂ���
		func	_local_1
		arg		nocount
		param	7
			use	1	��I���z���L�b�g
	@@use
		time	48h
		price	3200000
		name	��I��8�ɂ���
		info	��I��8�ɂ���
		func	_local_1
		arg		nocount
		param	8
			use	1	��I���z���L�b�g

@@define set shop_icon_header $$SHOP_ICON_HEADER
@@if shop_icon_header eq "" @@skip

	@@use
		time	6h
		name	�X�܊O�ϕύX(���K��)
		info	�X�܂̊O�ς�ύX(�H��)���܂��B
		price	100000
		arg		select|radio|nocount
		argselect	�X�܊O�ϑI��;001;�^�C�v1;002;�^�C�v2;003;�^�C�v3
			use	1	��I���z���L�b�g
		funci	_local_
			return "" if $main::MOBILE;
			
			my $html="";
			$html.='�X�܈ꗗ<br>';
			my @fld=split(/;/,$USE->{argselect});
			shift(@fld) if @fld%2==1;
			while(@fld)
			{
				my $icon=shift @fld;
				my $caption=shift @fld;
				$html.=main::GetTagImgShopIcon($icon).$caption."&nbsp;&nbsp;\n";
			}
			return $html;
		_local_
		func	_local_
			$DT->{icon}=$USE->{arg}{select};
			
			return '�X�܂�'.main::GetTagImgShopIcon($DT->{icon}).$USE->{arg}{select_hash}{$DT->{icon}}.'�ɂ��܂���';
		_local_
	@@use
		time	12h
		name	�X�܊O�ϕύX(���K��)
		info	�X�܂̊O�ς�ύX(�H��)���܂��B
		price	1000000
		arg		select|list|nocount
		argselect	�X�܊O�ϑI��;101;�^�C�v1;102;�^�C�v2;103;�^�C�v3
			use	1	��I���z���L�b�g
		funci	_local_i9
		func	_local_9
	@@use
		time	24h
		name	�X�܊O�ϕύX(��K��)
		info	�X�܂̊O�ς�ύX(�H��)���܂��B
		price	10000000
		arg		select|nocount
		argselect	�X�܊O�ϑI��;201;�^�C�v1;202;�^�C�v2;203;�^�C�v3
			use	1	��I���z���L�b�g
		funci	_local_i9
		func	_local_9

@@if shop_icon_header eq "" @@endskip
		
@@ITEM
	no		65
	type	�{
	code	badgossip
	name	�֒f�̏�
	info	����Ă͂Ȃ�Ȃ������Ȃ��Ă͂Ȃ�Ȃ��Ƃ��Ɂc
	price	150000
	cost	30000
	limit	1/0.2	#�������͓X�ܐ��ŏ�Z��A�؂�̂āB
	pop		0
	plus	1d
	scale	��
	flag	notrash|nosend
	@@use
		time	10h
		exp		10%
		scale	��
		action	�����\�𗬂�
		price	0
		name	�����\�𗬂�
		info	��������Α���̂��X�̐l�C���������܂����A���s���邱�Ƃ��c
		arg		target|nocount|message40	#���g�p���̑I�����w��B|�ŋ�؂��ĕ����w��B
								#  nocount -> �g�p�񐔑I���Ȃ�
								#  target  -> �ΏۓX�ܑI��
								#  message[1~?] -> ���b�Z�[�W����(80byte�ȉ�)����(���l��t����Ɠ��͐������������w��ł��܂�)
		argmessage	�������̔ƍs����������΂ǂ���	#��arg��message��ݒ肵�����̓��̓{�b�N�X��
													#����������ꍇ�͂���argmessage�Őݒ�ł��܂��B
													#���͂��ꂽ���b�Z�[�W��$USE->{arg}->{message}�Ŏ擾�B
													#(SJIS�ɕϊ����A80or�w��byte�ȉ��ɐ؂�l�߁AHTML�^�O������(EscapeHTML)�ς�)
			use		1	�֒f�̏�
		func	_local_
			# �������\�𗬂����
			my $ret;
			
			# ���X�ƃ^�[�Q�b�g�̏��ʊ֌W�Ő�������ϓ�������
			my $rate=$main::id2idx{$DT->{id}}-$main::id2idx{$DTS->{id}};
			$rate=-$rate*2 if $rate<0;
			$rate=1.5 if $rate<1.5;
			my $proba=1000/$rate;
			
			if(rand(1000)<$proba)
			{
				$DTS->{rank}-=int($DTS->{rank}/4);
				$ret=$DTS->{shopname}.'�̈����\�𗬂���킪�������܂���';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DTS->{shopname}.'�̈����\���L�܂�l�C��������܂���');
				WriteLog(2,0,$DT->{shopname}.'����̔ƍs����:�u'.$USE->{arg}{message}.'�v') if $USE->{arg}{message};
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/2);
				$ret=$DTS->{shopname}.'�̈����\�𗬂���킪���s���܂���';
				WriteLog(0,$DT->{id},$ret);
				WriteLog(3,0,$DT->{shopname}."��".$DTS->{shopname}.'�̈����\�𗬂����Ɖ�􂵂Ă����悤�ł�');
			}
			return $ret;
			_local_
	@@use
		time	4h
		exp		10%
		scale	��
		action	����������
		price	0
		name	����������
		info	�����܂Œǂ����܂�Ă�̂Ȃ�A���傤���Ȃ��ˁc
		arg		target|nocount|message40
		argmessage	�������̔ƍs����������΂ǂ���
			use		1	�֒f�̏�
		func	_local_
			# �����������i�������̓C�x���g�Ɠ������b�Z�[�W���o�́j
			
			# ���X�ƃ^�[�Q�b�g�̏��ʊ֌W�Ő�������ϓ�������
			my $rate=$main::id2idx{$DT->{id}}-$main::id2idx{$DTS->{id}};
			$rate=-$rate*2 if $rate<0;
			$rate=1.5 if $rate<1.5;
			my $proba=1000/$rate;
			
			my $ret="�������͎��s���A���X�̐l�C��������܂���";
			if(rand(1000)<$proba)
			{
				if($DTS->{item}[@@ITEMNO"�X�ԃ��{�b�g"-1])
				{
					$DT->{rank}-=int($DT->{rank}/2);
					if(rand(1000)<700)
					{
						$DTS->{item}[@@ITEMNO"�X�ԃ��{�b�g"-1]--;
						WriteLog(3,0,$DT->{shopname}."��".$DTS->{shopname}."�֖������ɓ���$ITEM[@@ITEMNO"�X�ԃ��{�b�g"]->{name}��j�󂵂܂��������Ǖ߂܂�܂���");
					}
					else
					{
						WriteLog(3,0,$DT->{shopname}."��".$DTS->{shopname}."�֖������ɓ���܂�����$ITEM[@@ITEMNO"�X�ԃ��{�b�g"]->{name}�ɕ߂܂�܂���");
					}
				}
				else
				{
					my $manbiki_count=0;
					foreach my $idx (0..$DTS->{showcasecount}-1)
					{
						my $itemno=$DTS->{showcase}[$idx];
						if($itemno)
						{
							my $cnt=int($DTS->{item}[$itemno-1]/4);
							$cnt=$ITEM[$itemno]->{limit}-$DT->{item}[$itemno-1] if $DT->{item}[$itemno-1]+$cnt>$ITEM[$itemno]->{limit};
							$DTS->{item}[$itemno-1]-=$cnt;
							$DT->{item}[$itemno-1]+=$cnt;
							$manbiki_count+=$cnt*$DTS->{price}[$idx];
						}
					}
					$ret="�������͐������܂���";
					WriteLog(2,0,$DTS->{shopname}."�����z\\$manbiki_count�̖�������Q�ɑ����܂���") if $manbiki_count;
					WriteLog(2,0,$DT->{shopname}.'����̔ƍs����:�u'.$USE->{arg}{message}.'�v') if $USE->{arg}{message} && $manbiki_count;
					WriteLog(2,0,$DTS->{shopname}."�ɓ������������Ƃ͉�����炸�ɓ����܂���") if !$manbiki_count;
				}
			}
			else
			{
				$DT->{rank}-=int($DT->{rank}/3);
				WriteLog(3,0,$DT->{shopname}."��".$DTS->{shopname}."�֖������ɓ���܂��������s���܂���");
			}
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
	@@use
		time	4h
		exp		10%
		scale	��
		action	�戵���i�̈����\�𗬂�
		price	0
		name	�Ǝ�̈����\�𗬂�
		info	���X�L���[
		arg		target|nocount|message40
		argmessage	�ƍs����������΂ǂ���
			use		1	�֒f�̏�
		func	_local_
			my %category=qw(4 ken 5 yoroi 6 tate 7 tue); #���ޔԍ��ƃC�x���g�R�[�h�̑Ή�
			
			my $itemno=$DTS->{showcase}->[int rand($DTS->{showcasecount})];
			my $itemtype=$ITEM[$itemno]->{type};
			my $category=$category{$itemtype};
			my $eventkey="kill-$category";
			
			#��I�̏��i��%category�O��������A���ɔ������Ȃ玸�s�B
			return '�\�𗬂��̂Ɏ��s���܂���' if !$category || grep($_ eq $eventkey,keys(%main::DTevent));
			
			#3���Ԏ����ŃC�x���g����
			$main::DTevent{$eventkey}=$main::NOW_TIME+3*60*60;
			
			WriteLog(2,0,$main::ITEMTYPE[$itemtype].'�s��̈����\���L�܂��Ă���悤�ł�');
			WriteLog(2,0,$DT->{shopname}.'����̔ƍs����:�u'.$USE->{arg}{message}.'�v') if $USE->{arg}{message};
			return $main::ITEMTYPE[$itemtype].'�s��̈����\���L�܂����悤�ł�';
		_local_
@@event
	start		-1 #�C�x���g���R��������
	code		kill-ken
	endmsg		�����^�������܂�܂���
	info		�����^�����N�����Ă��܂�
		param	�ؓ�				point=0    #+-0%
		param	�S�̌�				point=-100 #-10%
		param	�|�S�̌�			point=-200 #-20%
		param	�~�X�����̌�		point=-300 #-30%
		param	�I���n���R���̌�	point=-400 #-40%
@@event
	start		-1
	code		kill-yoroi
	endmsg		���Z�^�������܂�܂���
	info		���Z�^�����N�����Ă��܂�
		param	�v�̋�����			point=0
		param	�؂̋�����			point=0
		param	�S�̊Z				point=-100
		param	�|�S�̊Z			point=-200
		param	�~�X�����̊Z		point=-300
		param	�I���n���R���̊Z	point=-400
@@event
	start		-1
	code		kill-tate
	endmsg		�����^�������܂�܂���
	info		�����^�����N�����Ă��܂�
		param	�v�̏�				point=0
		param	�؂̏�				point=0
		param	�S�̏�				point=-100
		param	�|�S�̏�			point=-200
		param	�~�X�����̏�		point=-300
		param	�I���n���R���̏�	point=-400
@@event
	start		-1
	code		kill-tue
	endmsg		����^�������܂�܂���
	info		����^�����N�����Ă��܂�
		param	�؂̏�				point=0
		param	�S�̏�				point=-100
		param	�|�S�̏�			point=-200
		param	�~�X�����̏�		point=-300
		param	�I���n���R���̏�	point=-400

@@ITEM
	no		18
	type	�A�N�Z�T��
	code	skill-kajiya
	name	�b�艮�̋Z�p
	info	�b�艮�̃I���W���`
	price	50000
	cost	1000
	limit	1/0
	pop		7d
	scale	�Z
@@ITEM
	no		19
	type	�A�N�Z�T��
	code	skill-magic
	name	���@�̒m��
	info	���@�̊�b�m���ł�
	price	50000
	cost	1000
	limit	1/0
	pop		7d
	scale	�m��
@@ITEM
	no		24
	type	�A�N�Z�T��
	code	skill-mekiki
	name	�ڗ����̐^��
	info	�Ⴂ��������Ƒ����Ȃ�
	price	50000
	cost	1000
	limit	1/0
	pop		7d
	scale	�^��
@@ITEM
	no		38
	type	�A�N�Z�T��
	code	skill-kaitai
	name	��̉��̍�
	info	�����ɖ���������
	price	50000
	cost	1000
	limit	1/0
	pop		7d
	scale	��


@@ITEM
	no		64
	type	�A�N�Z�T��
	code	defence-manbiki
	name	�X�ԃ��{�b�g
	info	�X���̊Ď������Ă���܂�
	price	500000
	cost	30000
	limit	1/0.1
	pop		0
	plus	1d
	scale	��
	flag	noshowcase

@@ITEM
	no		11
	type	�A�N�Z�T��
	code	loto
	name	�󂭂�
	info	�ꝺ�����������Ȃ��i���I����2����1���<B>�m��</B>�j
	price	2000
	cost	10
	limit	50/20
	plus	10m
	scale	��
	pop		4h

@@ITEM
	no		25
	type	����
	code	mino
	name	�~�m�^�E���X��
	info	������Ƃ������Ȃ��ƒ{
	price	10000
	cost	1000
	limit	20/2
	plus	1d
	scale	��
	pop		1d
	@@use
		time	2h
		exp		1%
		job		���_��	times/job_cow_time_rate
		scale	���
		action	���
		price	0
		name	�������
		info	�~�m���񂩂�������܂�
		param	1
			need		1	�~�m�^�E���X��
		func	_local_
			# ���~�m�^�E���X���
			#   param1 ������x���i�P�`�j
			my $val=$USE->{param1}*$count;
			
			$val*=$DT->{item}[25-1];
			$val=int(rand($val))+1;
			AddItem(26,$val,'�~�m�����𐸐����܂���');
			
			my $useproba=$USE->{param1}*$USE->{param1};
			my $usecount=0;
			foreach(1..$count)
			{
				$usecount++ if rand(1000)<$useproba;
			}
			UseItem(25,$usecount,$ITEM[25]->{name}.'��'.($USE->{param1}==1?'����':'�ߘJ').'�œV�ɏ�����܂���') if $usecount;
			
			my $ret='�~�m������'.$val.'�{�������܂���';
			WriteLog(0,$DT->{id},$ret);
			return $ret;
		_local_
		
	@@use
		time	2h
		exp		1%
		job		���_��	times/job_cow_time_rate
		scale	���
		action	���
		price	0
		name	�n�[�h�ɓ������
		info	�~�m���񂩂�n�[�h�ɓ������܂�
		param	2
		func	_local_1
			need		1	�~�m�^�E���X��

@@ITEM
	no		26
	type	��
	code	mino_milk
	name	�~�m����
	info	���߂Ό��N�A�o�c�����₩
	price	200
	cost	50
	pop		30m
	limit	500/0
	scale	�{
	point	300%
	@@use
		time	3m
		job		���_��	times/job_cow_time_rate
		scale	�{
		action	����
		price	0
		name	����
		info	�~�m����������ł݂܂�
			use		1	�~�m����
		func	_local_
			# ���~�m����������
			my $val=$count;
			my $ret="";
			
			if($count>=30)
			{
				$DT->{rank}-=$count*2;
				$DT->{rank}=0 if $DT->{rank}<0;
				WriteLog(2,0,$DT->{shopname}.'�̓X�傪�~�}�Ԃŉ^�΂�܂���');
				WriteLog(2,0,'�����؂�Ƀ~�m����'.$count.'�{�����ނȂ�Đ��C�̍������Ⴀ��܂���');
				$ret="�c�C���t������a�@�̃x�b�h�̏�ł���";
			}
			elsif($count>=10)
			{
				$ret='�I�i�J���󂵂Ă��܂��܂����@�����؂�Ƀ~�m����'.$count.'�{�͈��݉߂��ł�';
				WriteLog(0,$DT->{id},$ret);
			}
			else
			{
				$DT->{rank}+=int(rand($count+1))+$count;
				$DT->{rank}=10000 if $DT->{rank}>10000;
				$ret='�~�m����������Ō��N�ɂȂ����C�����܂�';
				WriteLog(0,$DT->{id},$ret);
			}
			return $ret;
		_local_
	@@use
		time	72m
		job		���_��	times/job_cow_time_rate
		scale	�Z�b�g
		action	���C�g���y������
		price	0
		name	���C�g���y
		info	�~�m�������y�����y�����Ă݂܂�
			need	5	�~�m�^�E���X��
			use		10	�~�m����
			get		1	�~�m���[�O���g
	@@use
		time	144m
		job		���_��	times/job_cow_time_rate
		scale	�Z�b�g
		action	�w�r�[���y������
		price	0
		name	�w�r�[���y
		info	�~�m���������Ȃ蔭�y�����Ă݂܂�
			need	10	�~�m�^�E���X��
			use		20	�~�m����
			get		1	�~�m�`�[�Y

@@ITEM
	no		35
	type	��
	code	mino_yogurt
	name	�~�m���[�O���g
	info	�~�m�������������������[�O���g�@������ƃ~�m������
	price	3000
	cost	100
	pop		2h
	limit	100/0
	scale	��
	@@use
		time	10m
		job		���_��	times/job_cow_time_rate
		scale	��
		action	�H�ׂ�
		price	0
		name	�H�ׂ�
		info	�~�m���[�O���g��H�ׂĂ݂܂�
		ngmsg	�����̃I�N�`�ɂ͍���Ȃ��悤���c
			use		1	�~�m���[�O���g

@@ITEM
	no		36
	type	��
	code	mino_cheese
	name	�~�m�`�[�Y
	info	�~�m�����������������`�[�Y�@�����[���Ă��炢�~�m������
	price	9000
	cost	300
	pop		3h
	limit	50/0
	scale	��
	@@use
		time	1h
		job		���_��	times/job_cow_time_rate
		scale	��
		action	�H�ׂ�
		price	0
		name	�H�ׂ�
		info	�~�m�`�[�Y��H�ׂĂ݂܂�
		ngmsg	�N�T���ēf�����c
			use		1	�~�m�`�[�Y



@@ITEM
	no		27
	type	��
	code	seven_face
	name	���ʒ��̊ۏĂ�
	info	���j�����Ƃɂ͂������܂����
	price	10000
	cost	0
	limit	1/0
	scale	�C
	pop		1d
	@@use
		time	1h
		scale	�C
		action	�H�ׂ�
		price	0
		name	�H�ׂ�
		info	���j�����܂��傤��
		arg		nocount
			use		1	���ʒ��̊ۏĂ�	100%	�I�i�J��t�ɂȂ�܂���

@@ITEM
	no		28
	type	��
	code	ramusyu
	name	�������̃�����
	info	���̓`���̗E�҂��D���������Ƃ����������ł�
	price	20000
	cost	0
	limit	1/0
	scale	�{
	pop		1d
	@@use
		time	1h
		scale	�{
		action	����
		price	0
		name	����
		info	���j�����܂��傤��
		arg		nocount
			use		1	�������̃�����	100%	�����C���ɂȂ�܂���

@@ITEM
	no		29
	type	�A�N�Z�T��
	code	boots
	name	�������u�[�c
	info	���񂲂��������ȃu�[�c�ł�
	price	20000
	cost	0
	limit	1/0
	scale	��
	pop		1d
	@@use
		time	1h
		scale	��
		action	����
		price	0
		name	�����Ă��o��������
		info	�X�ɂ���o���Ă��j�����܂��傤��
		arg		nocount
			use		1	�������u�[�c	100%	�݂�Ȃ̎�������l��߂ɂ��܂���

@@ITEM
	no		77
	type	����
	code	party
	name	���j���Z�b�g
	info	�p�[�b�Ƃ��������Ƃ��ɂ̓R��
	price	200000
	cost	0
	limit	1/0
	scale	�Z�b�g
	@@use
		time	4h
		action	�p�[�e�B�J�n
		price	0
		name	���j���p�[�e�B
		info	����͖���u�ł�
		func	popup
		param	1000,�p�[�e�B���J���܂���
		arg		nocount
			use		1	���j���Z�b�g	100%	�����ւ̊��͂������Ă��܂���

@@ITEM
	no		78
	type	�{
	code	port-exp
	name	�]�E�̃X�X��
	info	�]�E�������l�̂��߂�
	price	10000
	limit	1
	pop		1d
	scale	�Z�b�g
	plus	1h
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�򉮂֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA��������Z�p���K�����܂�
		okmsg	�򉮂ɂȂꂽ�C�����܂�
		param	15,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,drug
			use		1	�]�E�̃X�X��
		func	_local_
			######################################################################
			# ���n���x�����i�w��A�C�e���ցA���̃A�C�e���̏n���x���ړ�������j
			#   param1 �n���x���v���X�������A�C�e���̔ԍ�(1~)
			#   param2 �n���x���}�C�i�X����A�C�e���̔ԍ�(1~) (:��؂�ŕ����w�艻)
			#   param3 �n���x���ړ�����ۂ̌W���i0~) (0.5���Ɣ����ɂ��Ĉړ�)
			#   ���ӁF�n���x�̍��v�`�F�b�N�͂��Ă��Ȃ��̂ŁA�W����1���傫������̂͂�߂����������ł��B
			######################################################################
			my $ret="";
			
			if($USE->{param1})
			{
				my $exp1=$DT->{exp}{$USE->{param1}};
				my $exp2=0;
				
				foreach my $exps (split(/:/,$USE->{param2}))
				{
					my $exp=$DT->{exp}{$exps};
					next if !$exp || $exps==$exp1;
					$exp2+=$exp;
					delete($DT->{exp}{$exps});
					my $msg=$ITEM[$exps]->{name}."�̏n���x ".int($exp/10)."% �� 0% �ɂȂ�܂���";
					$ret.=$msg."<br>";
					WriteLog(0,$DT->{id},$msg);
				}
				$exp2=int($exp2*$USE->{param3});
				$exp1+=$exp2;
				$exp1=1000 if $exp1>1000;
				my $msg=$ITEM[$USE->{param1}]->{name}."�̏n���x ".int($DT->{exp}{$USE->{param1}}/10)."% �� ".int($exp1/10)."% �ɂȂ�܂���";
				$ret.=$msg."<br>";
				WriteLog(0,$DT->{id},$msg);
				$DT->{exp}{$USE->{param1}}=$exp1;
			}
			$DT->{job}=$USE->{param4},$ret.='�E�Ƃ��u'.$main::JOBTYPE{$USE->{param4}}.'�v�ɂȂ�܂���' if $USE->{param4} && $USE->{param4} ne '_default_';
			$DT->{job}='',$ret.='�E�Ƃ��u�s��v�ɂȂ�܂���' if $USE->{param4} eq '_default_';
			
			return $ret;
		_local_
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�v�׍H���֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�v�׍H�̋Z�p���K�����܂�
		okmsg	�v�׍H���ɂȂꂽ�C�����܂�
		func	_local_1
		param	16,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�؍H�׍H���֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�؍H�׍H�̋Z�p���K�����܂�
		okmsg	�؍H�׍H���ɂȂꂽ�C�����܂�
		func	_local_1
		param	17,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�����׍H���֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�����׍H�̋Z�p���K�����܂�
		okmsg	�����׍H���ɂȂꂽ�C�����܂�
		func	_local_1
		param	66,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,tool
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�����֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�����ɕK�v�ȋZ�p���K�����܂�
		okmsg	�����ɂȂꂽ�C�����܂�
		func	_local_1
		param	20,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,weapon
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�����֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�����ɕK�v�ȋZ�p���K�����܂�
		okmsg	�����ɂȂꂽ�C�����܂�
		func	_local_1
		param	21,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,armor
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�Z���֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�Z���ɕK�v�ȋZ�p���K�����܂�
		okmsg	�Z���ɂȂꂽ�C�����܂�
		func	_local_1
		param	22,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,armor
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�񉮂֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�񉮂ɕK�v�ȋZ�p���K�����܂�
		okmsg	�񉮂ɂȂꂽ�C�����܂�
		func	_local_1
		param	23,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,weapon
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�T�z�v�֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�T�z�v�ɕK�v�ȋZ�p���K�����܂�
		okmsg	�T�z�v�ɂȂꂽ�C�����܂�
		func	_local_1
		param	9,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,material
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�؂���֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�؂���ɕK�v�ȋZ�p���K�����܂�
		okmsg	�؂���ɂȂꂽ�C�����܂�
		func	_local_1
		param	12,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,material
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�{���֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�{���ɕK�v�ȋZ�p���K�����܂�
		okmsg	�{���ɂȂꂽ�C�����܂�
		func	_local_1
		param	10,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,book
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	���_�Ƃ֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA���_�ƂɕK�v�ȋZ�p���K�����܂�
		okmsg	���_�ƂɂȂꂽ�C�����܂�
		func	_local_1
		param	25,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,cow
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�s���l�֓]�E������
		info	���̐E�Ƃ̋Z�p�o����S�Ď̂āA�s���l�ɕK�v�ȋZ�p���K�����܂�
		okmsg	�s���l�ɂȂꂽ�C�����܂�
		func	_local_1
		param	14,9:10:12:14:15:16:17:66:20:21:22:23:25,0.5,peddle
			use		1	�]�E�̃X�X��
	@@USE
		time	6h
		action	�]�E�C�s�J�n
		arg		nocount
		name	�Ŕ����낵����
		info	���Ȃ��̌��ɏd���̂��������Ă��邻�̊Ŕ����낵�܂�
		func	_local_1
		param	0,,0,_default_
			use		1	�]�E�̃X�X��

@@ITEM
	no		79
	type	����
	code	gift
	name	�M�t�g��
	info	�~�������̂���ɓ���悤�I
	price	10000
	cost	10
	limit	500/0
	scale	��
	@@USE
		time	1h
		action	��������
		name	�n�}�Z�b�g�ƈ�������
		info	�����Ȓn�}�̋l�ߍ��킹�ł�
		okmsg	�����p���肪�Ƃ��������܂���
			use		2	�M�t�g��
			get		1	�߂��̎R�ւ̒n�}
			get		1	�߂��̍z�R�ւ̒n�}
			get		1	���s�ւ̒n�}
	@@USE
		time	1h
		action	��������
		name	����{�Z�b�g�ƈ�������
		info	�����Ȗ{�̋l�ߍ��킹�ł�
		okmsg	�����p���肪�Ƃ��������܂���
			use		5	�M�t�g��
			get		1	15
			get		1	16
			get		1	17
	@@USE
		time	1h
		action	��������
		name	�㋉�{�Z�b�g�ƈ�������
		info	�����Ȗ{�̋l�ߍ��킹�ł�
		okmsg	�����p���肪�Ƃ��������܂���
			use		15	�M�t�g��
			get		1	20
			get		1	21
			get		1	22
			get		1	23
	@@USE
		time	1h
		action	��������
		name	�C�s�L�b�g�ƈ�������
		info	�Ȃ𖁂������l��
		okmsg	�����p���肪�Ƃ��������܂���
			use		2	�M�t�g��
			get		1	�C�s�L�b�g
	@@USE
		time	1h
		action	��������
		name	�~�m�^�E���X�ƈ�������
		info	�~�m�^�E���X�����������
		okmsg	�����p���肪�Ƃ��������܂���
			use		1	�M�t�g��
			get		1	25



#�j���C�x���g �ǉ�:ver.2001-11-11f
@@event
	start		20%
	basetime	5h
	plustime	5h
	code		happy
	startmsg	�j���̌����ӂ���Ƃ炵�͂��߂܂���
	endmsg		�j���̌��������܂���
	info		�j���̌����ӂ肻������Ă��܂�(�l�CUP)
	func		_local_
		my $time=$TIMESPAN;
		$time=10*3600 if $time>10*3600; # �ő�10%����
		$time=int($time/36);
		
		foreach(@DT)
		{
			$_->{rank}+=int(rand($time));
			$_->{rank}=10000 if $_->{rank}>10000;
		}
		return 0;
	_local_

@@EVENT				#���C�x���g��`�錾
	start		7%		#���C�x���g�����m��(1��)
	basetime	12h		#���C�x���g�������ԃx�[�X
	plustime	24h		#���C�x���g�������ԃ����_�������B�i�����_����0�`24h�v���X)
	code		boom-posyon	#���R�[�h�i���j�[�N�j
	startmsg	�J�ł͂�����Ƃ����|�[�V�����u�[���ł�	#���C�x���g���������b�Z�[�W
	endmsg		�|�[�V�����u�[�����I������悤�ł�		#���C�x���g�I�������b�Z�[�W
	info		�|�[�V�����֘A���i���l�C�ł�			#���C�x���g���������b�Z�[�W
		param	��			pop/1.5	#���C�x���g���e�i�A�C�e���p�����[�^�����w���j
		param	�|�[�V����		pop/1.5	#  ����:�A�C�e������,�p�����[�^��[+-/*]���l
		param	�n�C�|�[�V����	pop/1.5 #  ���ꂼ��̃A�C�e���̃p�����[�^�𑝌������܂��B
		param	�G�[�e��		pop/1.5 #  �p�����[�^���� customize.txt �� item.cgi �Ŋm�F���Ă��������B
		param	�n�C�G�[�e��	pop/1.5 #  �Ȃ��Apop==popular,money==price,base==pricebase,half==pricehalf
		param	�G����			pop/1.5 #  �Ŏ����ϊ�����܂��B
		param	��			point*2 #  ���ӓ_�Ƃ��āApop ���͒l������(�b��)�Ȃ̂ŁA
		param	�|�[�V����		point*2 #  ����s�������グ�����ꍇ�́A�l�����������邱�ƂɂȂ�܂��B
		param	�n�C�|�[�V����	point*3 #  ���Ȃ݂ɂ��̗�ł́A�򑐌n�̃A�C�e���̔���s������1.5�{�B
		param	�G�[�e��		point*2 #  ���p���̐l�C�㏸����2�`4�{�ɏグ�Ă��܂��B
		param	�n�C�G�[�e��	point*3
		param	�G����			point*4

@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		ken-sale
	startmsg	���̎��v�����܂��Ă���悤�ł�
	endmsg		���̎��v���ʏ탌�x���ɖ߂�܂���
	info		���̎��v�����܂��Ă��܂�
		param	�ؓ�				pop/2
		param	�S�̌�				pop/2
		param	�|�S�̌�			pop/2
		param	�~�X�����̌�		pop/2
		param	�I���n���R���̌�	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		tate-sale
	startmsg	���̎��v�����܂��Ă���悤�ł�
	endmsg		���̎��v���ʏ탌�x���ɖ߂�܂���
	info		���̎��v�����܂��Ă��܂�
		param	�v�̏�				pop/2
		param	�؂̏�				pop/2
		param	�S�̏�				pop/2
		param	�|�S�̏�			pop/2
		param	�~�X�����̏�		pop/2
		param	�I���n���R���̏�	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		yoroi-sale
	startmsg	�Z�̎��v�����܂��Ă���悤�ł�
	endmsg		�Z�̎��v���ʏ탌�x���ɖ߂�܂���
	info		�Z�̎��v�����܂��Ă��܂�
		param	�v�̋�����			pop/2
		param	�؂̋�����			pop/2
		param	�S�̊Z				pop/2
		param	�|�S�̊Z			pop/2
		param	�~�X�����̊Z		pop/2
		param	�I���n���R���̊Z	pop/2
@@EVENT
	start		10%
	basetime	6h
	plustime	24h
	code		tue-sale
	startmsg	��̎��v�����܂��Ă���悤�ł�
	endmsg		��̎��v���ʏ탌�x���ɖ߂�܂���
	info		��̎��v�����܂��Ă��܂�
		param	�؂̏�				pop/2
		param	�S�̏�				pop/2
		param	�|�S�̏�			pop/2
		param	�~�X�����̏�		pop/2
		param	�I���n���R���̏�	pop/2
@@EVENT
	start		50%		#�������m����50%�����A�����͉��́ustartfunc�v����B
	start		-1		#�������Ȃ�
	basetime	12h		#��12h�ŃC�x���g�I�������A���ۏI�����邩�ǂ����͉��́uendfunc�v����B
	plustime	0		#
	code		priceup-yakusou
	startmsg	�򑐂��s�����Ă��܂�
	endmsg		�򑐕s������������܂���
	info		�򑐕s���Ŋ֘A���i�̉��i���������Ă��܂�
	startfunc	stock_le(1,70)		#���C�x���g�����������f�̊֐��Ăяo���B�iinc-event-function.cgi�j
	#endfunc		stock_ge(1,71)		#���C�x���g�I���������f�̊֐��Ăяo���B�iinc-event-function.cgi�j
		param	��			price*2		#���W�����i��2�{�ɂȂ�܂��B
		param	�|�[�V����		price*1.5
		param	�n�C�|�[�V����	price*1.5
		param	�G�[�e��		price*1.5
		param	�n�C�G�[�e��	price*1.5
		param	�G����			price*1.5
		param	��			pop*2		#�����̏ꍇ�͔���s������1/2�ɉ�����܂��B
		param	�|�[�V����		pop*1.5
		param	�n�C�|�[�V����	pop*1.5
		param	�G�[�e��		pop*1.5
		param	�n�C�G�[�e��	pop*1.5
		param	�G����			pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-tetu
	startmsg	�S���s�����Ă��܂�
	endmsg		�S�s������������܂���
	info		�S�s���Ŋ֘A���i�̉��i���������Ă��܂�
	startfunc	stock_le(5,70)
	#endfunc		stock_ge(5,71)
		param	�S��			price*2
		param	�S�̌�			price*1.5
		param	�|�S�̌�		price*1.5
		param	�S�̏�			price*1.5
		param	�|�S�̏�		price*1.5
		param	�S�̊Z			price*1.5
		param	�|�S�̊Z		price*1.5
		param	�S�̏�			price*1.5
		param	�|�S�̏�		price*1.5
		param	�S��			pop*2
		param	�S�̌�			pop*1.5
		param	�|�S�̌�		pop*1.5
		param	�S�̏�			pop*1.5
		param	�|�S�̏�		pop*1.5
		param	�S�̊Z			pop*1.5
		param	�|�S�̊Z		pop*1.5
		param	�S�̏�			pop*1.5
		param	�|�S�̏�		pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-misuriru
	startmsg	�~�X�������s�����Ă��܂�
	endmsg		�~�X�����s������������܂���
	info		�~�X�����s���Ŋ֘A���i�̉��i���������Ă��܂�
	startfunc	stock_le(6,70)
	#endfunc		stock_ge(6,71)
		param	�~�X������			price*2
		param	�~�X�����̌�		price*1.5
		param	�~�X�����̏�		price*1.5
		param	�~�X�����̊Z		price*1.5
		param	�~�X�����̏�		price*1.5
		param	�~�X������			pop*2
		param	�~�X�����̌�		pop*1.5
		param	�~�X�����̏�		pop*1.5
		param	�~�X�����̊Z		pop*1.5
		param	�~�X�����̏�		pop*1.5
@@EVENT
	start		50%
	start		-1
	basetime	12h
	plustime	0
	code		priceup-oriharukon
	startmsg	�I���n���R�����s�����Ă��܂�
	endmsg		�I���n���R���s������������܂���
	info		�I���n���R���s���Ŋ֘A���i�̉��i���������Ă��܂�
	startfunc	stock_le(7,70)
	#endfunc		stock_ge(7,71)
		param	�I���n���R����			price*2
		param	�I���n���R���̌�		price*1.5
		param	�I���n���R���̏�		price*1.5
		param	�I���n���R���̊Z		price*1.5
		param	�I���n���R���̏�		price*1.5
		param	�I���n���R����			pop*2
		param	�I���n���R���̌�		pop*1.5
		param	�I���n���R���̏�		pop*1.5
		param	�I���n���R���̊Z		pop*1.5
		param	�I���n���R���̏�		pop*1.5

@@EVENT
	start		10%
	basetime	48h
	plustime	24h
	code		plusdown-yakusou
	startmsg	�򑐍͔|�Ǝ҂��򑐂̉������ۂ��Ă���悤�ł�
	endmsg		�򑐍͔|�Ǝ҂��򑐂̉����ĊJ���܂���
	info		�s��ւ̖򑐋������~�܂��Ă��܂�
		param	��			plus=-180		#���s�ꌸ��
@@EVENT
	start		10%
	basetime	12h
	plustime	12h
	code		plusup-tetu
	startmsg	�V���ɓS�z����������܂���
	endmsg		�V�����S�z�����R���܂���
	info		�S�̗��ʗʂ��}���ɑ����Ă��܂�
		param	�S��			plus=720		#���s��ւ̓��׃y�[�X��480s�B
@@EVENT
	start		7%
	basetime	9h
	plustime	16h
	code		plusup-misuriru
	startmsg	�V���Ƀ~�X�����z����������܂���
	endmsg		�V�����~�X�����z�����R���܂���
	info		�~�X�����̗��ʗʂ��}���ɑ����Ă��܂�
		param	�~�X������			plus=960
@@EVENT
	start		5%
	basetime	6h
	plustime	18h
	code		plusup-oriharukon
	startmsg	�V���ɃI���n���R���z����������܂���
	endmsg		�V�����I���n���R���z�����R���܂���
	info		�I���n���R���̗��ʗʂ��}���ɑ����Ă��܂�
		param	�I���n���R����			plus=1200


# ��ʗD��Ŗ������C�x���g
@@EVENT
	start		100% #old50%
	basetime	0h		#�������n�̃C�x���g�ł͂Ȃ��̂Ŏ��Ԃ�0�B
	plustime	0h
	code		manbiki
	info		������
	startfunc	_local_(400,200)
		#�����͂��̊֐����C�x���g�̖{�̂ɂȂ��Ă�
		my($hitproba,$breakproba)=@_;
		#�_����m��,���{�b�g�j��m��
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"�X�ԃ��{�b�g"-1])
			{
				return (0,$DT->{shopname}.'�֖�����������܂������j�~����܂���') if rand(1000)>$breakproba;
				
				$DT->{item}[@@ITEMNO"�X�ԃ��{�b�g"-1]--;
				return (0,$DT->{shopname}.'�֖�����������'.$ITEM[@@ITEMNO"�X�ԃ��{�b�g"]->{name}.'���j�󂳂�܂���');
			}
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/10);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'�����z\\'.$count.'�̖�������Q�ɑ����܂���') if $count;
			return (0,$DT->{shopname}.'�ɓ������������Ƃ͉�����炸�ɓ����܂���');
		}
		return 0;
	_local_

@@EVENT
	start		30% #old15%
	basetime	0h
	plustime	0h
	code		goutou
	info		����
	startfunc	_local_(700)
		#�����͂��̊֐����C�x���g�̖{�̂ɂȂ��Ă�
		my($hitproba)=@_;
		#�_����m��
		
		foreach my $DT (@DT)
		{
			next if rand(1000)>$hitproba;
			
			if($DT->{item}[@@ITEMNO"�X�ԃ��{�b�g"-1])
			{
				$DT->{item}[@@ITEMNO"�X�ԃ��{�b�g"-1]--;
				return (0,$DT->{shopname}.'�֋���������'.$ITEM[@@ITEMNO"�X�ԃ��{�b�g"]->{name}.'���j�󂳂�܂���');
			}
			
			$DT->{rank}-=int($DT->{rank}/5);
			
			my $count=0;
			foreach my $idx (0..$DT->{showcasecount}-1)
			{
				my $itemno=$DT->{showcase}[$idx];
				next if !$itemno;
				
				my $cnt=int($DT->{item}[$itemno-1]/4);
				$DT->{item}[$itemno-1]-=$cnt;
				$count+=$cnt*$DT->{price}[$idx];
			}
			return (0,$DT->{shopname}.'�����z\\'.$count.'�̋�����Q�ɑ����܂���') if $count;
			return (0,$DT->{shopname}.'�ɓ����������Ƃ͉�����炸�ɓ����܂���');
		}
		return 0;
	_local_


# �᎑���D��Ŏ��������C�x���g
@@EVENT
	start		30%
	code		getmoney
	info		��������
	startfunc	_local_(100000)
		my($money)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{money}+=$money;
			$_->{money}=$main::MAX_MONEY if $_->{money}>$main::MAX_MONEY;
			return (0,$_->{shopname}.'��\\'.$money.'�̕⏕�����x������܂���');
		}
		return 0;
	_local_

# ���ʗD��Ől�C�A�b�v�C�x���g
@@EVENT
	start		30%
	basetime	0h
	plustime	0h
	code		getpop
	info		�l�C�A�b�v
	startfunc	_local_(1000)
		my($pop)=@_;
		
		foreach(reverse(@DT))
		{
			next if rand(1000)>300;
			
			$_->{rank}+=$pop;
			$_->{rank}=10000 if $_->{rank}>10000;
			return (0,$_->{shopname}.'���G���ŏЉ��l�C���オ�����悤�ł�');
		}
		return 0;
	_local_

# �󂭂��C�x���g
@@EVENT
	start		50%
	basetime	0h
	plustime	0h
	code		loto
	info		�󂭂����I
	startfunc	_local_
		WriteLog(2,0,"�󂭂��̒��I���s���܂���");
		foreach my $DT (@DT)
		{
			my $count=$DT->{item}[11-1];
			$DT->{item}[11-1]=0;
			next if !$count;
			
			foreach(1..$count)
			{
				my $rnd=rand(6096454);
				my $hit=0;
				
				$hit=5 if $rnd<152411;
				$hit=4 if $rnd<10000;
				$hit=3 if $rnd<216;
				$hit=2 if $rnd<6;
				$hit=1 if $rnd<1;
				
				if($hit)
				{
					my $getmoney=(0,1000000000,150000000,5000000,100000,10000)[$hit];
					
					$DT->{moneystock}+=$getmoney;
					$DT->{money}=$main::MAX_MONEY if $DT->{money}>$main::MAX_MONEY;
					WriteLog(($hit<=3?1:2),0,$DT->{shopname}."��$hit��\\$getmoney�𓖂Ă܂����I");
				}
			}
		}
		return 0;
	_local_

@@FUNCINIT
#�ڗ����̐^���������Ă���ꍇ�A�������ɕK�v�Ȏ��Ԃ�3/4�ɂ���B
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/4*3) if $DT->{item}[@@ITEMNO"�ڗ����̐^��"-1];

#�E�Ƃ��u�s���l�v�̏ꍇ�A�������ɕK�v�Ȏ��Ԃ�1/2�ɂ���B
$TIME_SEND_ITEM=int($TIME_SEND_ITEM/2) if $DT->{job} eq 'peddle';

@@FUNCITEM
######################################################################
# ���{or�n�}���{���{���ɂȂ��Ĕj������Ƃ�������
######################################################################
sub lostbook
{
	my $itemno=$USE->{itemno};
	if(rand(1000)<$USE->{param1})
	{
		UseItem($itemno,1,$ITEM[$itemno]->{name}.'���ǂ߂Ȃ����{���{���ɂȂ�܂����̂Ŕj�����܂���');
	}
	return "";
}
######################################################################
# ���l�C�A�b�v(�ėp)
#   param1 �A�b�v�|�C���g
#   param2 �ŋ߂̏o�����p�R�����g �\������:�������X��param2
######################################################################
sub popup
{
	my $up=int($USE->{param1}*(2-$DT->{rank}/5000));
	$DT->{rank}+=$up;
	$DT->{rank}=10000 if $DT->{rank}>10000;
	
	my $ret=$USE->{param2}."�F�l�C".int($up/100)."%�A�b�v";
	WriteLog(0,$DT->{id},$ret);
	WriteLog(3,0,$DT->{shopname}."��".$USE->{param2});
	
	return $ret;
}

@@FUNCUPDATE
sub UpdateResetBefore #���Z���O�̏���(�֐����Œ�)
{
	UpdateTodayPrize();
	
	sub UpdateTodayPrize
	{
		#�ܕi���^
		my @TOP123=(
			[
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 5],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 4],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 3],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 1],			],],
				['���{�b�g',	[[@@ITEMNO "�X�ԃ��{�b�g", 1],		],],
				['���j���O�b�Y',[[@@ITEMNO "���ʒ��̊ۏĂ�", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������̃�����", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������u�[�c", 1],	],],
			],
			[
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 3],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 3],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 1],			],],
				['�֒f�̏�',	[[@@ITEMNO "�֒f�̏�", 1],			],],
				['���j���O�b�Y',[[@@ITEMNO "���ʒ��̊ۏĂ�", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������̃�����", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������u�[�c", 1],	],],
			],
			[
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 1],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 1],			],],
				['�L���p�b�N',	[[@@ITEMNO "�L���p�b�N", 1],		],],
				['���j���O�b�Y',[[@@ITEMNO "���ʒ��̊ۏĂ�", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������̃�����", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������u�[�c", 1],	],],
			],
			[
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 2],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 1],			],],
				['�M�t�g��',	[[@@ITEMNO "�M�t�g��", 1],			],],
				['�L���p�b�N',	[[@@ITEMNO "�L���p�b�N", 1],		],],
				['�L���p�b�N',	[[@@ITEMNO "�L���p�b�N", 1],		],],
				['�L���p�b�N',	[[@@ITEMNO "�L���p�b�N", 1],		],],
				['���j���O�b�Y',[[@@ITEMNO "���ʒ��̊ۏĂ�", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������̃�����", 1],	],],
				['���j���O�b�Y',[[@@ITEMNO "�������u�[�c", 1],	],],
			],
		);
		
		TopGetItem($DT[0],$TOP123[0],"����D����") if defined($DT[0]);
		TopGetItem($DT[1],$TOP123[1],"�ɂ�����2�ʂ�") if defined($DT[1]);
		TopGetItem($DT[2],$TOP123[2],"���肬����܂�") if defined($DT[2]);
	
		for(my $i=9; $i<$#DT; $i+=10)
		{
			TopGetItem($DT[$i],$TOP123[3],"���ʏ܂Ƃ���".($i+1)."�ʂ�") if defined($DT[$i]);
		}
		
		sub TopGetItem
		{
			my($DT,$itemlist,$head)=@_;
			
			my @list=@{$itemlist};
			my @getitem=@{$list[int(rand($#list+1))]};
			
			my $msg=$head.$DT->{shopname}."����ɂ�".$getitem[0]."�������܂���";
			WriteLog(2,0,0,$msg,1);
			foreach (@{$getitem[1]})
			{
				my @itemnocount=@{$_};
				
				my $cnt=AddItem($DT,$itemnocount[0],$itemnocount[1]);
				my $ITEM=$ITEM[$itemnocount[0]];
				WriteLog(0,$DT->{id},0,$head."�ܕi�Ƃ���".$ITEM->{name}."��".$itemnocount[1].$ITEM->{scale}."�l�����܂���",1);
				$cnt=$itemnocount[1]-$cnt;
				WriteLog(0,$DT->{id},0,"�������ő及�����ȏゾ�����̂�".$cnt.$ITEM->{scale}."�j�����܂���",1) if $cnt;
			}
		}
	}
}

sub UpdateResetAfter #���Z����̏���(�֐����Œ�)
{
	UpdateTodayEraseTech();
	
	sub UpdateTodayEraseTech
	{
		foreach my $DT (@DT)
		{
			my $expsum=0;
			foreach(values(%{$DT->{exp}}))
			{
				$expsum+=$_;
			}
			#$expsum=5000 if $expsum>5000;
			
			next if $expsum<=4000;
			$expsum-=4000;
			
			foreach my $itemno (@@ITEMNO"�b�艮�̋Z�p",@@ITEMNO"���@�̒m��",@@ITEMNO"��̉��̍�",@@ITEMNO"�ڗ����̐^��")
			{
				if($DT->{item}[$itemno-1] && rand(14000)<$expsum)
				{
					my $msg="���S��Y��A".$DT->{shopname}."�����".$ITEM[$itemno]->{name}."�������܂���";
					WriteLog(2,0,0,$msg,1);
					WriteLog(0,$DT->{id},0,$ITEM[$itemno]->{name}."�������܂���",1);
					$DT->{item}[$itemno-1]--;
				}
			}
		}
	}
}

@@FUNCNEW

# @@DEFINE Set NewShopMoney NewShopTime NewShopItem �̏���
$DT->{money}=@@VALUE"NewShopMoney" if @@VALUE"NewShopMoney";
$DT->{time}=$NOW_TIME-eval(@@VALUE"NewShopTime") if @@VALUE"NewShopTime";
if(@@VALUE"NewShopItem")
{
	my %item=split /:/,@@VALUE"NewShopItem";
	while(my($key,$val)=each %item)
	{
		foreach my $item (@ITEM)
		{
			 $DT->{item}[$item->{no}-1]+=$val,last if $key eq $item->{code} or $key eq $item->{name};
		}
	}
}

# $DEFINE_FUNCNEW_NOLOG=1 ��ݒ肷��ƁA�V�X�e�����̍ŋ߂̏o�����V���J�X���b�Z�[�W��}�����܂��B
# $DEFINE_FUNCNEW_NOLOG=1;
# WriteLog(1,0,0,$DT->{shopname}."���G���g���[���܂���",1);

# ���̑��A�V���J�X���ɓƎ��̏�����ǉ��ł��܂��B

@@FUNCSHOPIN

SetUserDataEx($DT,'_so_move_in',$NOW_TIME); # �ړ]�������L�^
if($DT->{job} eq 'peddle')
{
	# �s���l(peddle)�ɂ͈ړ]����Ԃ�1/2��Ԋ�
	$DT->{_MoveTownTime}=int($DT->{_MoveTownTime}/2);
	EditTime($DT,$DT->{_MoveTownTime});
	WriteLog(0,$DT->{id},0,'�ړ]���Ԃ�������'.GetTime2HMS($DT->{_MoveTownTime}).'�ōς񂾂悤�ł�',1);
}
if(GetUserDataEx($DT,'_so_present_money'))
{
	WriteLog(0,$DT->{id},0,'�ړ]���̊X�����S�ʂƂ���\\'.GetUserDataEx($DT,'_so_present_money').'�����炢�܂���',1);
	SetUserDataEx($DT,'_so_present_money','');
}

@@FUNCSHOPOUT

if(GetUserDataEx($DT,'_so_move_in'))
{
	my $present_money=int(($NOW_TIME-GetUserDataEx($DT,'_so_move_in'))/86400)*5000;
	EditMoney($DT,$present_money); # �؍݊���1���ɕt��\5000���S�ʂƂ��Ď�����
	SetUserDataEx($DT,'_so_present_money',$present_money);
	SetUserDataEx($DT,'_so_move_in',''); # $DT->{user}{_so_move_in} ���폜
}

@@FUNCBUY
# package item �ł��B
# 
# $item::BUY �𗘗p�ł��܂��B$item::BUY �̍\���̓}�j���A���� @@ITEM funcb ���������������B
# ���i���̏����� @@ITEM funcb �𗘗p���Ă��������B

if($BUY->{whole})
{
	# �s�ꂩ��̎d���̏ꍇ�A\500000�ɕt��1���̃M�t�g����i�悷��B
	my $price=$BUY->{num}*$BUY->{price};
	my $count=int $price/500000;
	
	$count=AddItemSub(@@ITEMNO"�M�t�g��",$count,$BUY->{dt}) if $count;
	WriteLog(0,$BUY->{dt}{id},'�s�ꂩ��M�t�g����'.$count.'�����炢�܂���') if $count;
}

@@END #��`�I���錾(�ȍ~�R�����g����)

------------
���ȒP�Ȑ���
------------

�S�Ă̏��i/�C�x���g�͂��̃t�@�C����ϊ����쐬����܂��B

���̃t�@�C�����J�X�^�}�C�Y���邱�ƂŁA�܂������Ⴄ���E�� SOLD OUT ����
��邱�Ƃ��o���܂��B���ꂱ���A�Q�[���̕����������ς��邱�Ƃ��o����͂�
�ł��B�i�Ⴆ�΁A�����X�^�[�����Q�[���Ƃ��A�f�ՃQ�[���Ƃ��j

�����������I�ȃJ�X�^�}�C�Y���o�Ă�����ʔ������낤���������Ȃ��Ǝv���A
�X�N���v�g�̃t���[���J�ƃJ�X�^�}�C�Y���@��p�ӂ�������ł��B

���̕W���A�C�e���f�[�^�́A�T���v���Ƃ����Ӗ������������ł��B�Ƃ͌�����
���o�����X������1�N�ɂ킽���čs���Ă��܂��̂ł���Ȃ�ɗV�ׂ郌�x������
�v���܂����A�V�X�e���̃|�e���V�������\���Ɉ����o���Ă���Ƃ͌����Ȃ���
������܂���B

�ł��̂ŁA����A�J�X�^�}�C�Y���Ă݂Ă��������B�P���ɏ��i����ς��邾��
�ł��ʔ����ł����A�Ǝ��̏��i/�J�����@/�C�x���g��ǉ����邱�Ƃ���r�I��
�P�ɏo���܂��B���킵�Ă݂Ă��������B

���i�f�[�^�̍X�V�́A�{�t�@�C����ύX���ăA�b�v���[�h��A�Ǘ����j���[��
�u���i�f�[�^����/�X�V�v���s�����Ƃŉ\�ł��B���̍ہA�G���[�Ȃǂ������
�\������܂��B

�f�[�^��`�̏����́A�������̒��̃J�X�^�}�C�Y�h�L�������g�Ǝ��ۂɂ��̃t�@
�C�����Q�Ƃ��A�������Ă݂Ă��������B���ɁA���̃t�@�C���̓T���v���ɂȂ�
�Ǝv���܂��B

�v���O�����ǂ߂�l�� makeitem.cgi ����͂��Ă݂Ă��������B���i�f�[�^��
�ҏW����ɂ������ĕs�ւȓ_�� makeitem.cgi ����������Ɗy�ɂȂ邩������
�܂���B

�Ȃ��ASOLD OUT �͂��ꂩ����i�������Ă�������ł��B���̍ہA��`�f�[�^
�̌݊��������Ȃ���\��������܂��B�������A���̂悤�Ȃ��Ƃ��N����
�Ȃ��悤�ɓw�߂܂����A���������\��������Ƃ������Ƃ��������������B

�ǐL

�J�X�^�}�C�Y�ɋ����������Ă����݂Ȃ���̂������ŁA�����ȃ^�C�v��
SOLD OUT ��ڂɂ���悤�ɂȂ�܂����B��ϊ������v���Ă��܂��B���肪�Ƃ�
�������܂��B
