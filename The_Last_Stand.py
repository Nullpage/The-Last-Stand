# Import modules and define variables
import random as r
import time
import turtle as t
import weapons
print (weapons.All)()
Weapons = []
# Functions for Survivors
Survivors = 0
def Get_Survivors(SHours,Survivors):
    SNum = 20 * SHours
    while SNum != 0:
        if SNum >= 100:
            Survivors = Survivors + 1
            SNum = SNum - 100
        else:
            RNum = r.randint(1,100)
            if RNum <= SNum:
                Survivors = Survivors + 1
            break
    if Survivors > 0:
        return Survivors
    else:
        return None

# Functions for Weapons
def Get_Weapon(WHours):
    WNum = 15 * WHours
    if WNum >= 100:
        return r.choice(weapons.All)()
    else:
        RNum = r.randint(1,100)
        if RNum <= WNum:
            return r.choice(weapons.All)()
        else:
            return None

# Daytime searching inputs
print ("It is daytime. 7AM")
Go = False
while Go != True:
    try:
        SHours = int(input("How many hours do you want to search for survivors? "))
        if SHours < 0:
            raise ValueError()
    
        WHours = int(input("How many hours do you want to search for weapons? "))
        if WHours < 0:
            raise ValueError()

    except ValueError:
        print ("Please enter a valid number.")
        continue
    if SHours + WHours == 12:
        Go = True
    elif SHours + WHours > 12:
        print ("You only have 12 hours to search!")
        continue
    elif SHours + WHours < 12 and SHours + WHours >= 0:
        print ("You should use all 12 hours of searching time!")
        continue

# Display time passing
for i in range(7,20):
    #time.sleep(1)
    print (str(i) + ':00')

# Display what was found
Survivors = Get_Survivors(SHours,Survivors)
Weapon = Get_Weapon(WHours)
if Survivors is not None:
    print ("Well done! You found {num} survivors!".format(num=Survivors))
else:
    print ("You didn't find any survivors.")
if Weapon is not None:
    print ("Well done! You found " + Weapon.prefix + ' ' + Weapon.name + '!')
    Weapons.append(Weapon.name)
    print (Weapons)
else:
    print ("You didn't find any new weapons.")

# Run daytime inputs
Input = ''
while Input != 'Night':
    Input = input("What would you like to do? ")
    if Input == 'Night':
        print ("Proceeding to night-time.")
    if Input == 'Survivors':
        if Survivors == None:
            print ("You have 0 survivors.")
        else:
            print ("You have {num} survivors.".format(num=Survivors))
    if Input == 'Stats':
        WInput = input("What weapon do you want to know the stats of? ")
        Length = len(weapons.All)
        length = len(Weapons)
        for i in range(2,Length + 2):
            for a in range(0,length):
                if WInput == Weapons[a]:
                    print ("""Name: {name}
Damage: {damage}
Rate of fire: {rate}
Range: {distance}""".format(name=weapon.name,damage=weapon.damage,rate=weapon.rate,distance=weapon.distance))
                    break
        continue

# Setup screen for night
Window = t.Screen()
Window.setup(700,700)
Turtle = t.Turtle()
Turtle.ht()
Turtle.pu()
Turtle.speed(5000)
# Draw barricade
Turtle.setpos(200,-350)
Turtle.seth(90)
Turtle.pd()
for i in range(0,2):
    Turtle.fd(700)
    Turtle.rt(90)
    Turtle.fd(50)
    Turtle.rt(90)
Turtle.pu()
Window.exitonclick()
