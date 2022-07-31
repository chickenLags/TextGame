from items.equip_type import EquipType
from items.material import Material


class Item:
    def __init__(self):
        pass

    def get_name(self):
        return f"{self.material.name} {self.equipType.name.lower()}"

    def to_row(self):
        return [self.get_name()]


class Equipable(Item):
    def __init__(self, material: Material, equip_type: EquipType):
        super().__init__()
        self.material = material
        self.equipType = equip_type
        self.durability = self.material.durability + self.equipType.durability

    def to_row(self):
        return [self.get_name(), self.durability]


class Weapon(Equipable):
    def __init__(self, material: Material, equip_type: EquipType):
        super(Weapon, self).__init__(material, equip_type)

    def get_damage(self):
        return self.equipType.defDmg + self.material.damage

    def to_row(self):
        return [self.get_name(), self.get_damage(), self.durability]

    def erode(self):
        self.durability -= 1


