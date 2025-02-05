class Melee:
    def __init__(self, name, damage, type, modifier):
        self.name = name
        self.damage = damage
        self.type = type
        self.modifier = modifier
class Ranged:
    def __init__(self, name, damage, type, modifier):
        self.name = name
        self.damage = damage
        self.type = type
        self.modifier = modifier 


class M_Abillity(Melee):
    def __init__(self, name, damage, type, modifier):
        super().__init__(name, damage, type, modifier)




class R_Abillity(Ranged):
    def __init__(self, name, damage, type, modifier):
        super().__init__(name, damage, type, modifier)






Dev = Melee("",0,"","")
Punch = Melee("Punch",10,"melee","melee")
Kick = Melee("Kick",12,"melee","melee")
Shoot = Ranged("Shoot",32,"ranged","dexterity")
Temp_Ability = R_Abillity("Abil",55,"wisdom","wisdom")