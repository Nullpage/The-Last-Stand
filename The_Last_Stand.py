# Import modules and define variables (if needed)
import random, time, weapons
import pygame

# Functions for Survivors
def Get_Survivors(SHours,Survivors):
    NewSurvivors = 0
    SNum = 15 * SHours
    while SNum != 0:
        if SNum >= 100:
            NewSurvivors = NewSurvivors + 1
            SNum = SNum - 100
        else:
            RNum = random.choice(range(1,100))
            if RNum <= SNum:
                NewSurvivors = NewSurvivors + 1
                return NewSurvivors
    if NewSurvivors == 0:
        return None

# Functions for Weapons
def Get_Weapon(WHours,Weapons):
    WNum = 10 * WHours
    if WNum >= 100:
        return random.choice(weapons.All)
        Weapons.append(Weapon.name)
    else:
        RNum = random.choice(range(1,100))
        if RNum <= WNum:
            return random.choice(weapons.All)
            Weapons.append(Weapon.name)
    return None

pygame.init()
Screen = pygame.display.set_mode((1600,800))
Done = False
while not Done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Done = True

    pygame.display.flip()

pygame.quit()

# Reset variables for start of game
Survivors = 0
Weapons = []

# Daytime inputs
print ("It is daytime. 7AM")
while True:
    try:
        SHours = int(input("How many hours do you want to search for survivors? "))
        WHours = int(input("How many hours do you want to search for weapons? "))
    except ValueError:
        print ("Invalid input.")
        continue
    if SHours > 12 or SHours < 0:
            print ("Invalid input.")
            continue
    if WHours > 12 or WHours < 0:
            print ("Invalid input.")
            continue
    if SHours + WHours == 12:
        break
    elif SHours + WHours > 12:
        print ("You only have 12 hours to search.")
        continue
    elif SHours + WHours < 12:
        print ("You should use all 12 hours of searching time.")
        continue

# Display time passing
for i in range(7,20):
    #time.sleep(1)
    print (str(i) + ':00')

# Display what was found
NewSurvivors = Get_Survivors(SHours,Survivors)
NewWeapon = Get_Weapon(WHours,Weapons)
if NewSurvivors is not None:
    print ("You found {num} survivors.".format(num=NewSurvivors))
    Survivors = Survivors + 1
else:
    print ("You didn't find any survivors.")
if NewWeapon is not None:
    print ("You found " + NewWeapon.Prefix + ' ' + NewWeapon.Name + '.')
    Weapons.append(NewWeapon)
else:
    print ("You didn't find any new weapons.")

# Run daytime inputs
while True:
    Input = input("What would you like to do? ")
    if Input == 'Night':
        print ("Proceeding to night-time.")
        break
    if Input == 'Survivors':
        if Survivors == None:
            print ("You have 0 survivors.")
        else:
            print ("You have {num} survivor(s).".format(num=Survivors))
    if Input == 'Weapons':
        WInput = input("Which weapon do you want to get information about? ")
        Length = len(Weapons)
        Weapon = None
        for i in range(0,Length):
            if Weapons[i].Name == WInput:
                Weapon = Weapons[i]
                break
        if not Weapon:
            print ("Weapon not found. Either you don't own it, or the weapon name does not exist.")
            continue
        WInput = input("What do you want to know about the weapon? ")
        if WInput == 'All':
            print ("""Name: {name}
Damage: {damage}
Rate of fire: {rate}
Fire rate: {fire_rate}
Range: {range}
Magazine size: {magazine}""".format(name=Weapon.Name,damage=Weapon.Damage,rate=Weapon.Rate,fire_rate=Weapon.Fire_Rate,range=Weapon.Range,magazine=Weapon.Magazine))
        elif WInput == 'Name':
            print ("Name: {name}".format(name=Weapon.Name))
        elif WInput == 'Damage':
            print ("Damage: {damage}".format(damage=Weapon.Damage))
        elif WInput == 'Rate of fire':
            print ("Rate of fire: {rate}".format(rate=Weapon.Rate))
        elif WInput == 'Fire rate':
            print ("Fire rate: {fire_rate}".format(fire_rate=Weapon.Fire_Rate))
        elif WInput == 'Range':
            print ("Range: {range}".format(range=Weapon.Range))
        elif WInput == 'Magazine size':
            print ("Magazine size: {magazine}".format(magazine=Weapon.Magazine))
