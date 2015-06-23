import base


#add fuccking lasers for rails
#snipers to box
#add chemlights for pubs

class det5_base(base.Base):
	class NoWrite: pass
	headgear = 'rhsusf_ach_bare_headset'
	binoc = 'ACE_Vector'
	items = base.Base.items + [
		'ItemGPS',
		'tf_microdagr',
		'TRYK_Shemagh',
		'tf_anprc152',
		'ItemMap',
		'ItemCompass',
	]

	class HandGun:
		weapon = 'RH_g17'
		mags = [['RH_17Rnd_9x19_g17', 12]]
		rail = 'RH_M6X'
		suppressor = 'RH_gemtech9'

	class Uniform:
		type = 'Niko_USA_M81'
		items = base.Base.Uniform.items + [
			['RH_17Rnd_9x19_g17', 2],
			['ACE_MapTools', 1],
		]
	class Vest:
		type = 'bink_vest_2'
		items = [
			['rhs_mag_m67', 2],
			['rhs_mag_an_m8hc', 2],
		]
	class Backpack:
		type = 'rhsusf_falconii'
		items = [
			['tf_anprc152', 1],
			['rhsusf_ANPVS_15', 1],
			['alive_tablet', 1],
			['ACE_fieldDressing', 2],
			['ACE_packingBandage', 2],
			['ACE_elasticBandage', 2],
			['ACE_tourniquet', 2],
			['ACE_epinephrine', 2],
			['ACE_personalAidKit', 2],
			['ACE_quikclot', 2],
			['ACE_DAGR', 2],
			['ACE_EarPlugs', 2],
			['ACE_IR_Strobe_Item', 2],
		]
	

class Operation_det5(det5_base):
	headgear = 'rhsusf_ach_bare_wood_headset'
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'RH_eothhs1'
		suppressor = 'rhsusf_acc_nt4_tan'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]

	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
		]
		
class officer_det5(det5_base):
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_M203'
		optic = 'iansky_specterdrkf_d_2D'
		suppressor = 'rhsusf_acc_nt4_tan'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
			['rhs_mag_M433_HEDP', 1],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
			['rhs_mag_M441_HE', 4],
			['rhs_mag_M433_HEDP', 4],

		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['rhs_mag_M585_white', 2],
			['rhs_mag_m661_green', 2],
			['rhs_mag_m662_red', 2],
		]

class Intel_det5(det5_base):
	headgear = 'rhsusf_ach_bare_tan_headset_ess'
	class Primary:
		weapon = 'rhs_weap_mk18_grip2_KAC'
		optic = 'RH_t1'
		suppressor = 'rhsusf_acc_nt4_tan'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
		]
		
class Weapons_det5(det5_base):
	headgear = 'rhsusf_ach_bare_des_headset'
	class Primary:
		weapon = 'rhs_weap_m249_pip_S_vfg'
		optic = 'iansky_specterdr_d_2D'
		rail = 'rhsusf_acc_anpeq15side'
		mags = [
			['rhs_200rnd_556x45_M_SAW', 200],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_200rnd_556x45_M_SAW', 2],
		]
	class Backpack(det5_base.Backpack):
		type = 'B_Kitbag_cbr'
		items = det5_base.Backpack.items + [
		]

class Engineer_det5(det5_base):
	headgear = 'rhsusf_ach_bare_wood_headset_ess'
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'RH_ta31rmr_tan'
		suppressor = 'rhsusf_acc_nt4_tan'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Secondary:
		weapon = 'rhs_weap_M136_hedp'
		mags = [
			['rhs_m136_hedp_mag', 1],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]
	class Backpack(det5_base.Backpack):
		type = 'B_Kitbag_rgr'
		items = det5_base.Backpack.items + [
			['DemoCharge_Remote_Mag', 3],
		]

class Medical_det5(det5_base):
	headgear = 'rhsusf_ach_bare_tan_headset'
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'RH_eotexps3'
		suppressor = 'rhsusf_acc_nt4_tan'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]
	class Backpack(det5_base.Backpack):
		type = 'B_Kitbag_cbr'
		items = det5_base.Backpack.items + [
			['ACE_fieldDressing', 16],
			['ACE_packingBandage', 16],
			['ACE_elasticBandage', 16],
			['ACE_quikclot', 16],
			['ACE_tourniquet', 8],
			['ACE_surgicalKit', 1],
			['ACE_morphine', 4],
			['ACE_atropine', 4],
			['ACE_epinephrine', 4],
			['ACE_salineIV_250', 4],
		]

class Commo_det5(det5_base):
	headgear = 'rhsusf_ach_bare_des_headset_ess'
	class Primary:
		weapon = 'rhs_weap_m4a1_blockII_grip2'
		optic = 'RH_ta31rmr_tan'
		suppressor = 'rhsusf_acc_nt4_tan'
		rail = 'rhsusf_acc_anpeq15'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]
	class Backpack:
		type = 'tf_rt1523g_big_rhs'
		items = det5_base.Backpack.items + [
		]
