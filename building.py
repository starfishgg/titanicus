from entity import BattlefieldEntity




class Building(BattlefieldEntity):
    def __init__(self, name, owner, position, armour, hp):
        super().__init__(name, owner, position)

        self.armour = armour
        self.hp = hp

    @property
    def destroyed(self):
        return self.hp == 0
    

    def take_damage(self, amount):
        # not taking armour into account yet
        self.hp = max(0, self.hp - amount)