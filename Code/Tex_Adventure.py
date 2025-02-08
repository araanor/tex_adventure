import pickle
import time
import random
import os
from Classes import enemey, player
from Weapons import Melee, Ranged, Dev, Punch, Kick, Shoot, Temp_Ability

global checker
checker = 0

def clear():
    os.system('cls')


def Tutorial():
    clear()
    Q = int(input("Do you want  to do the tutorial. 1 for yes, 2 for no"))
    if Q == 1:
        clear()
        print("From here on out 1 is for yes, 2 is for no, attack can be used in battle, inv can be used to open your inventory anywhere.")
        enem1 = enemey("Rein",50,11,11,11,11,11,11,11)
        tut_p = player("player 1",100,20,20,20,20,20,20,20)
        time.sleep(1)
        print("You are now face to face with an enemy")
        Hit(enem1, tut_p,Dev,True)
        Fight(enem1, tut_p)

    else:
        pass

def Fight(enem1, tut_p):
    global checker
    checker = 1
    q1 = input("type 'attack' to attack or 'inv' to open inventory")
    if q1 == "attack":
        atk_inp = int(input("Attacks: \n1. Punch \n2. Kick \n3. shoot \n4. Temp_Abbility"))
        if atk_inp == 1:
            clear()
            enem1.health -= Punch.damage
            Hit(enem1,tut_p,Punch,False)
        elif atk_inp == 2:
            clear()
            enem1.health -= Kick.damage
            Hit(enem1,tut_p,Kick,False)
        elif atk_inp == 3:
            clear()
            enem1.health -= Shoot.damage
            Hit(enem1,tut_p,Shoot,False)
        elif atk_inp== 4:
            clear()
            enem1.health -= Temp_Ability.damage
            Hit(enem1,tut_p,Temp_Ability,False)
        else:
            print("Incorrect selection")

def Hit(enem1, tut_p, attk, start):
    print(f"{'Stat name':<30}{'Opponent':^30}{'Attack':^30}{'Player':>30}")
    print(f"{'Name':<30}{enem1.name:^30}{'':^30}{tut_p.name:>30}")
    print(f"{'Health':<30}{enem1.health:^30}{'':^30}{tut_p.health:>30}")
    if start == False:
        if attk.type == "melee":
            print(f"{'Melee':<30}{enem1.melee:^30}{attk.name:^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")
        elif attk.type == "ranged":
            print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{attk.name:^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")
        elif attk.type == "intelligence":
            print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{attk.name:^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")
        elif attk.type == "wisdom":
            print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{attk.name:^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")
        elif attk.type == "durrability":
            print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{attk.name:^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")
        elif attk.type == "dexterity":
            print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{attk.name:^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")
        elif attk.type == "navigation":
            print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
            print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
            print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
            print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
            print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
            print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
            print(f"{'Navigation':<30}{enem1.navigation:^30}{attk.name:^30}{tut_p.navigation:>30}")
    else:
        print(f"{'Melee':<30}{enem1.melee:^30}{'':^30}{tut_p.melee:>30}")
        print(f"{'Ranged':<30}{enem1.ranged:^30}{'':^30}{tut_p.ranged:>30}")
        print(f"{'Intelligence':<30}{enem1.intelligence:^30}{'':^30}{tut_p.intelligence:>30}")
        print(f"{'Wisdom':<30}{enem1.wisdom:^30}{'':^30}{tut_p.wisdom:>30}")
        print(f"{'Durrability':<30}{enem1.durrability:^30}{'':^30}{tut_p.durrability:>30}")
        print(f"{'Dexterity':<30}{enem1.dexterity:^30}{'':^30}{tut_p.dexterity:>30}")
        print(f"{'Navigation':<30}{enem1.navigation:^30}{'':^30}{tut_p.navigation:>30}")

    if enem1.health >= 0:
        if checker == 1:
            enemey_fight(enem1,tut_p)
        else:
            Fight(enem1,tut_p)
    else:
        Win()

def enemey_fight(enem1,tut_p):
    global checker
    checker = 0
    wpn = random.randint(1,4)
    wpns = [Punch,Kick,Shoot,Temp_Ability]
    if wpn == 1:
        clear()
        tut_p.health -= Punch.damage
        Hit(enem1,tut_p,Punch,False)
    elif wpn == 2:
        clear()
        tut_p.health -= Kick.damage
        Hit(enem1,tut_p,Kick,False)
    elif wpn == 3:
        clear()
        tut_p.health -= Shoot.damage
        Hit(enem1,tut_p,Shoot,False)
    elif wpn== 4:
        clear()
        tut_p.health -= Temp_Ability.damage
        Hit(enem1,tut_p,Temp_Ability,False)
    
    Hit(enem1,tut_p,wpns[wpn-1],False)


def selection():
    select_class = int(input("Selct your class. \n1."))



def Win():
    print("You Win. You defated your opponent")
    selection()
    
















Tutorial()