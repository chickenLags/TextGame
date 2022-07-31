from items.equipable import Equipable


class DefensiveGear(Equipable):
    def getDefence(self):
        return self.material.defence + self.equipType.defDmg

    def to_row(self):
        return [self.get_name(), self.getDefence(), self.durability]
