from p4a.loadout import LoadOut

class det5_base(LoadOut):
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
		mags = [['RH_17Rnd_9x19_g17', 17]]
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
	goggles = 'TRYK_Shemagh_G'
	class Primary:
		weapon = 'SMA_Mk17'
		optic = 'RH_eotech553mag_tan'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'SMA_ANPEQ15_TAN'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 20],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 6],
		]

	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
		]
		
class officer_det5(det5_base):
	goggles = 'TRYK_Shemagh'
	class Primary:
		weapon = 'SMA_Mk17_EGLM'
		optic = 'iansky_specterdrkf_d_2D'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'SMA_ANPEQ15_TOP_TAN_SCAR'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 20],
			['1Rnd_HE_Grenade_shell', 1],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 6],
			['1Rnd_HE_Grenade_shell', 8],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
			['1Rnd_Smoke_Grenade_shell', 2],
			['1Rnd_SmokeGreen_Grenade_shell', 2],
			['1Rnd_SmokeRed_Grenade_shell', 2],
		]

class Intel_det5(det5_base):
	headgear = 'rhsusf_ach_bare_tan_headset_ess'
	goggles = 'TRYK_Shemagh'
	class Primary:
		weapon = 'SMA_Mk17'
		optic = 'RH_shortdot'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'SMA_ANPEQ15_TAN'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 20],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 6],
		]
	class Backpack(det5_base.Backpack):
		items = det5_base.Backpack.items + [
		]
		
class Weapons_det5(det5_base):
	headgear = 'rhsusf_ach_bare_des_headset'
	goggles = 'TRYK_Shemagh'
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
	goggles = 'TRYK_Shemagh_G'
	class Primary:
		weapon = 'SMA_MK14'
		optic = 'RH_ta31rmr_tan'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'SMA_ANPEQ15_TAN'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 20],
		]
	class Secondary:
		weapon = 'rhs_weap_M136_hedp'
		mags = [
			['rhs_m136_hedp_mag', 1],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 6],
		]
	class Backpack(det5_base.Backpack):
		type = 'B_Kitbag_rgr'
		items = det5_base.Backpack.items + [
			['DemoCharge_Remote_Mag', 3],
		]

class Medical_det5(det5_base):
	headgear = 'rhsusf_ach_bare_tan_headset'
	goggles = 'TRYK_Shemagh_G'
	class Primary:
		weapon = 'SMA_MK14'
		optic = 'RH_eotech553_tan'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'SMA_ANPEQ15_TOP_TAN_SCAR'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 20],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 6],
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
	goggles = 'TRYK_Shemagh'
	class Primary:
		weapon = 'SMA_MK14'
		optic = 'RH_ta31rmr_tan'
		suppressor = 'SMA_spSCARtan_762'
		rail = 'SMA_ANPEQ15_TAN'
		mags = [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 20],
		]
	class Vest(det5_base.Vest):
		items = det5_base.Vest.items + [
			['SMA_20Rnd_762x51mm_M80A1_EPR', 6],
		]
	class Backpack:
		type = 'tf_rt1523g_big_rhs'
		items = det5_base.Backpack.items + [
		]
