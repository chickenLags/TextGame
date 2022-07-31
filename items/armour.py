from items.defensive_gear import DefensiveGear
from items.equip_type import EquipType
from items.material import Material


class Armour(DefensiveGear):
    def __init__(self, material: Material, equip_type: EquipType):
        super(Armour, self).__init__(material, equip_type)
