from items.Item import Item
from items.equip_type import EquipType
from items.material import Material


class Equipable(Item):
    def __init__(self, material: Material, equip_type: EquipType):
        super().__init__()
        self.material = material
        self.equipType = equip_type
        self.durability = self.material.durability + self.equipType.durability

    def to_row(self):
        return [self.get_name(), self.durability]

    def get_name(self):
        return f"{self.material.name} {self.equipType.name.lower()}"

    def __eq__(self, other):
        return(
            type(self) == type(other)
            and self.get_name() == other.get_name()
            and self.equipType == other.equipType
            and self.durability == other.durability
        )
