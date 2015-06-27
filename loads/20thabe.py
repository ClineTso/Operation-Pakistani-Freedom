from p4a.loadout import LoadOut

class army_base(LoadOut):
	class NoWrite: pass
	headgear = 'rhsusf_ach_helmet_ocp'
	items = base.Base.items + [
		'tf_rf7800str',
		'ItemMap',
		'ItemCompass',
	]

	class Primary:
		optic = 'rhsusf_acc_ACOG'
		rail = 'rhsusf_acc_anpeq15side'
	
	class Uniform:
		type = 'rhs_uniform_cu_ocp'
		items = base.Base.Uniform.items + [
			['ACE_MapTools', 1],
			['ACE_EarPlugs', 2],
		]
	class Vest:
		type = 'rhsusf_iotv_ocp_Rifleman'
		items = [
			['rhs_mag_m67', 2],
			['rhs_mag_an_m8hc', 2],
		]
	class Backpack:
		type = 'rhsusf_assault_eagleaiii_ocp'
		items = [
			['rhsusf_ANPVS_15', 1],
			['ACE_fieldDressing', 2],
			['ACE_packingBandage', 2],
			['ACE_elasticBandage', 2],
			['ACE_tourniquet', 2],
			['ACE_epinephrine', 2],
			['ACE_personalAidKit', 2],
			['ACE_quikclot', 2],
		]

class army_rifleman(army_base):
	class Primary(army_base.Primary):
		weapon = 'rhs_weap_m4a1_carryhandle_grip'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(army_base.Vest):
		items = army_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]
	class Backpack(army_base.Backpack):
		items = army_base.Backpack.items + [
		]

class army_tl(army_rifleman):
	headgear = 'rhsusf_ach_helmet_headset_ocp'
	binoc = 'Binocular'
	items = army_rifleman.items + [
	class Primary(army_base.Primary):
		weapon = 'rhs_weap_m4a1_carryhandle_grip'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Uniform(army_base.Uniform):
		items = army_base.Uniform.items + [
			['tf_anprc152', 1],
		]
	class Vest(army_base.Vest):
		type = 'rhsusf_iotv_ocp_Teamleader'
		items = army_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],

		]

	class Backpack(army_rifleman.Backpack):
		items = army_rifleman.Backpack.items + [
			['ACE_IR_Strobe_Item', 2],
		]

class army_sl(army_tl):
	headgear = 'rhsusf_ach_helmet_headset_ocp'
	binoc = 'Binocular'
	class Backpack(army_tl.Backpack):
		items = army_tl.Backpack.items + [
			['tf_anprc152', 1],
			['ACE_IR_Strobe_Item', 2],
		]
	class Primary(army_tl.Primary):
		weapon = 'rhs_weap_m4a1_carryhandle_grip'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(army_base.Uniform):
		items = army_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]
		]
	class Vest(army_base.Vest):
		type = 'rhsusf_iotv_ocp_Squadleader'
		items = army_tl.Vest.items + [

		]

class army_ar(army_base):
	class Primary(army_base.Primary):
		weapon = 'rhs_weap_m249_pip_L'
		optic = 'rhsusf_acc_ELCAN'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]

	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(army_base.Uniform):
		items = army_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(army_base.Vest):
		type = 'rhsusf_iotv_ocp_SAW'
		items = army_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 2],
		]
	class Backpack(army_base.Backpack):
		items = army_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 3],
			['tf_anprc152', 1],
		]

class army_gl(army_rifleman):
	binoc = 'Binocular'
	items = army_rifleman.items + [
	class Primary(army_base.Primary):
		weapon = 'rhs_weap_m4a1_m320'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
			['rhs_mag_M433_HEDP', 1],
		]
	class Uniform(army_base.Uniform):
		items = army_base.Uniform.items + [
			['', 1],
		]
	class Vest(army_base.Vest):
		type = 'rhsusf_iotv_ocp_Grenadier'
		items = army_base.Vest.items + [
			['rhs_mag_M433_HEDP', 3],
			['rhs_mag_M714_white', 3],
		]

class army_mg(army_base):
	class Primary(army_base):
		weapon = 'rhs_weap_m240B'
		optic = 'RH_ta648'
		mags = [['rhsusf_100Rnd_762x51', 100]]
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(army_base.Uniform):
		items = army_base.Uniform.items + [['RH_15Rnd_9x19_M9', 2]]

	class Vest(army_base.Vest):
		type = 'rhsusf_iotv_ocp_SAW'
		items = army_base.Vest.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

	class Backpack(army_base.Backpack):
		items = army_base.Backpack.items + [
			['rhsusf_100Rnd_762x51', 2],
		]

class army_amg(army_rifleman):
	items = army_rifleman.items + [
	binoc = 'Binocular'
	class Vest(army_base.Vest):
		items = army_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 6],
		]
	class Backpack(army_rifleman.Backpack):
		items = army_rifleman.Backpack.items + [
			['rhs_mag_30Rnd_556x45_M855A1_Stanag_Tracer_Red', 2],
			['rhsusf_100Rnd_762x51', 3],
		]

class army_at(army_rifleman):
	class Secondary:
		weapon = 'rhs_weap_fgm148'
		mags = [
			['rhs_fgm148_magazine_AT', 1],
		]

	class Backpack(army_rifleman.Backpack):
		items = army_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 1],
		]

class army_aat(army_rifleman):
	items = army_rifleman.items + [
	binoc = 'ACE_Vector'
	class Backpack(army_rifleman.Backpack):
		items = army_rifleman.Backpack.items + [
			['rhs_fgm148_magazine_AT', 2],
		]

class army_pl(army_rifleman):
	headgear = 'rhsusf_ach_helmet_headset_ocp'
	items = army_rifleman.items + ['
	binoc = 'ACE_Vector'

	class Primary(army_tl.Primary):
		weapon = 'rhs_weap_m4a1_carryhandle'
	class HandGun:
		weapon = 'RH_m9'
		mags = [['RH_15Rnd_9x19_M9', 15]]
	class Uniform(army_base.Uniform):
		items = army_base.Uniform.items + [
			['RH_15Rnd_9x19_M9', 2],
		]

	class Backpack(army_rifleman.Backpack):
		items = army_rifleman.Backpack.items + [
			['tf_anprc152', 2],
			['alive_tablet', 1],
			['ACE_IR_Strobe_Item', 2],
		]
	
class army_rto(army_rifleman):
	headgear = 'rhsusf_ach_helmet_headset_ocp'
	items = army_rifleman.items + [
	binoc = 'Binocular'
	class Backpack(army_rifleman.Backpack):
		type = "tf_rt1523g_big"
		items = army_rifleman.Backpack.items + [
			['alive_tablet', 1],
			['tf_anprc152', 2],
		]

class army_medic(army_rifleman):
	headgear = 'rhsusf_ach_helmet_headset_ocp'
	items = army_rifleman.items + [
	class Backpack(army_base.Backpack):
		items = army_base.Backpack.items + [
			['tf_anprc152', 1],
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
	class Vest(army_base.Vest):
		type = 'rhsusf_iotv_ocp_Medic'
		items = army_base.Vest.items + [
		
		]

