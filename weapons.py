class Weapon:
    Name = ''
    Damage = 0
    Rate = 0
    Fire_Rate = ''
    Range = ''
    Magazine = 0
    Prefix = 'a'
 
class Pistol(Weapon):
    Name = 'Pistol'
    Damage = 5
    Rate = 5
    Fire_Rate = 'Semi'
    Range = 'Ranged'
    Magazine = 10
    Prefix = 'a'
 
class Axe(Weapon):
    Name = 'Axe'
    Damage = 10
    Rate = 1
    Fire_Rate = 'Semi'
    Range = 'Melee'
    Magazine = 0
    Prefix = 'an'
 
class Chainsaw(Weapon):
    Name = 'Chainsaw'
    Damage = 2
    Rate = 20
    Fire_Rate = 'Full'
    Range = 'Melee'
    Magazine = 100
    Prefix = 'a'
 
class Sniper(Weapon):
    Name = 'Sniper'
    Damage = 10
    Rate = 1
    Fire_Rate = 'Semi'
    Range = 'Scoped'
    Magazine = 5
    Prefix = 'a'
 
class AK47(Weapon):
    Name = 'AK47'
    Damage = 5
    Rate = 10
    Fire_Rate = 'Full'
    Range = 'Ranged'
    Magazine = 30
    Prefix = 'an'
 
All = [Pistol,Axe,Chainsaw,Sniper,AK47]
