from p4a.loadout import LoadOut

class ana_base(LoadOut):
	headgear = 'LOP_H_6B27M_ANA'
	items = [
		'ItemWatch',
		'ItemMap',
		'ItemCompass',
	]	

	class Uniform:
		type = 'LOP_U_AA_Fatigue_01'
		items = base.Base.Uniform.items + [
			['ACE_EarPlugs', 1],
		]
	class Vest:
		type = 'LOP_V_CarrierLite_ANA'
		items = [
			['rhs_mag_m67', 2],
			['rhs_mag_an_m8hc', 2],
		]
	class Backpack:
		type = 'TRYK_B_Alicepack'
		items = [
			['ACE_fieldDressing', 2],
			['ACE_packingBandage', 2],
			['ACE_elasticBandage', 2],
			['ACE_tourniquet', 2],
			['ACE_personalAidKit', 2],
			['ACE_quikclot', 2],
			['ACE_EarPlugs', 2],
		]
################  Rifleman

class ana_rifleman(ana_base):
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(ana_base.Vest):
		items = ana_base.Vest.items + [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 6],
		]
	class Backpack(ana_base.Backpack):
		items = ana_base.Backpack.items + [
		]

		
################  Grenadier 

class ana_grenadier(ana_rifleman):
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle_M203'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
			['rhs_mag_M433_HEDP', 1],
		]

	class Secondary:
		weapon = 'tf47_at4_HEDP'
		mags = [
			['tf47_at4_m_HEDP', 1],
		]
	class Vest(ana_rifleman.Vest):
		items = ana_rifleman.Vest.items + [
		]

	class Backpack(ana_rifleman.Backpack):
		items = ana_rifleman.Backpack.items + [
			['rhs_mag_M433_HEDP', 5],
			['rhs_mag_M441_HE', 5],
			['rhs_mag_m714_White', 5],
		]

################  Squad Leader

class ana_tl(ana_rifleman):
	headgear = 'LOP_H_6B27M_ess_ANA'
	items = ana_rifleman.items + ['tf_anprc154']
	binoc = 'Binocular'

	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class Vest(ana_rifleman.Vest):
		items = ana_rifleman.Vest.items + [
		]

	class Uniform(ana_rifleman.Uniform):
		items = ana_rifleman.Uniform.items + [
		]
	class Backpack(ana_rifleman.Backpack):
		items = ana_rifleman.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
		]
		
class ana_sl(ana_tl):
	headgear = 'LOP_H_6B27M_ess_ANA'
	class Backpack(ana_rifleman.Backpack):
		items = ana_rifleman.Backpack.items + [
			['tf_anprc152_2', 1],
		]


################  Medium Machine Gunner
class ana_mg(ana_base):
	binoc = 'Binocular'
	class Primary:
		weapon = 'rhs_weap_pkm'
		mags = [
			['rhs_100Rnd_762x54mmR_green', 100],
		]
	class Vest(ana_base.Vest):
		items = ana_base.Vest.items + [
			['rhs_100Rnd_762x54mmR_green', 1],
		]
	class Backpack(ana_base.Backpack):
		items = ana_base.Backpack.items + [
			['rhs_100Rnd_762x54mmR', 2],
		]
		
class ana_lmg(ana_base):
	binoc = 'Binocular'
	class Primary:
		weapon = 'rhs_weap_m249_pip_L'
		mags = [
			['rhsusf_100Rnd_556x45_soft_pouch', 100],
		]
	class Vest(ana_base.Vest):
		items = ana_base.Vest.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 1],
		]
	class Backpack(ana_base.Backpack):
		items = ana_base.Backpack.items + [
			['rhsusf_100Rnd_556x45_soft_pouch', 2],
		]

################  Medic
class ana_medic(ana_rifleman):
	items = ana_crew.items + [
		'tf_anprc154',
	]
	class Vest(ana_rifleman.Vest):
		items = ana_rifleman.Vest.items + [
		]
	class Backpack(ana_rifleman.Backpack):
		items = ana_base.Backpack.items + [
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


################  Platoon Leader

class ana_pl(ana_rifleman):
	items = ana_rifleman.items + ['tf_anprc154']
	binoc = 'Binocular'
	headgear = 'H_Beret_blk'
	goggles = 'G_Spectacles'
	class Primary:
		weapon = 'rhs_weap_m16a4_carryhandle'
		mags = [
			['rhs_mag_30Rnd_556x45_Mk262_Stanag', 30],
		]
	class HandGun:
		weapon = 'RH_mak'
		mags = [['RH_8Rnd_9x18_Mak', 8]]
		]
	class Uniform(ana_rifleman.Uniform):
		type = 'LOP_U_AA_Fatigue_01_slv'
		items = ana_rifleman.Uniform.items + [
		]
	class Vest(ana_rifleman.Vest):
		items = ana_base.Vest.items + [
			['RH_8Rnd_9x18_Mak', 2],
		]
	class Backpack(ana_base.Backpack):
		items = ana_base.Backpack.items + [
			['rhsusf_ANPVS_14', 1],
			['tf_anprc152', 1],
		]

################  Platoon RTO

class ana_rto(ana_rifleman_light):
	binoc = 'Binocular'
	items = ana_rifleman_light.items + ['tf_anprc154']
	class Backpack:
		type = 'tf_anprc155'
		items = ana_rifleman_light.Backpack.items + [
			['tf_anprc152', 1],
		]