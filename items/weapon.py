
from items.equip_type import EquipType
from items.equipable import Equipable
from items.material import Material


class Weapon(Equipable):
    def __init__(self, material: Material, equip_type: EquipType):
        super(Weapon, self).__init__(material, equip_type)

    def get_damage(self):
        return self.equipType.defDmg + self.material.damage

    def to_row(self):
        return [self.get_name(), self.get_damage(), self.durability]

    def erode(self):
        self.durability -= 1
