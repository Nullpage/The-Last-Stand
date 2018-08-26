class WeaponRanges:
    MELEE = 0
    RANGED = 5
    SCOPED = 10

class Weapon:
    name = 'none'
    damage = 0
    rate = 0
    distance = 0
    hit_sound = 'none'
    prefix = 'a'

class Pistol(Weapon):
    name = 'Pistol'
    damage = 5
    rate = 15
    distance = WeaponRanges.RANGED
    hit_sound = 'bang'
    prefix = 'a'

class Axe(Weapon):
    name = 'Axe'
    damage = 20
    rate = 10
    distance = WeaponRanges.MELEE
    hit_sound = 'thwack'
    prefix = 'an'

class Chainsaw(Weapon):
    name = 'Chainsaw'
    damage = 10
    rate = 30
    distance = WeaponRanges.MELEE
    hit_sound = 'rrrrr'
    prefix = 'a'

class Sniper(Weapon):
    name = 'Sniper'
    damage = 25
    rate = 5
    distance = WeaponRanges.SCOPED
    hit_sound = 'boom'
    prefix = 'a'

class AK47(Weapon):
    name = 'AK47'
    damage = 5
    rate = 25
    distance = WeaponRanges.RANGED
    hit_sound = 'bang'
    prefix = 'an'

All = [Pistol,Axe,Chainsaw,Sniper,AK47]
