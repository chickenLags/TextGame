import pytest as pytest

from Inventory import Inventory
from exceptions.no_item_found import NoItemFoundException
from items.armour import Armour
from items.item_manager import ItemManager
from items.shield import Shield
from items.weapon import Weapon


class TestInventory:
    def setup(self):
        self.inventory = Inventory()
        im = ItemManager()

        self.rusty_dagger = Weapon(im.get_material('Rusty'), im.get_weapon_type('Dagger'))
        self.iron_longsword = Weapon(im.get_material('Iron'), im.get_weapon_type('Long sword'))

        self.leather_gauntlets = Armour(im.get_material('Leather'), im.get_armour_type('Gauntlets'))
        self.iron_shield = Shield(im.get_material('Iron'), im.get_shield_type('Shield'))
        self.dragon_helmet = Armour(im.get_material('Dragon scales'), im.get_armour_type('Helmet'))

        self.inventory.add(self.rusty_dagger)
        self.inventory.add(self.leather_gauntlets)
        self.inventory.add(self.iron_shield)

    def test_add_and_retrieve_weapons(self):
        weapons = self.inventory.get_weapons()

        assert weapons.__contains__(self.rusty_dagger)  # was added
        assert not weapons.__contains__(self.iron_longsword)  # wasn't added
        assert not weapons.__contains__(self.dragon_helmet)  # Not in inventory, and not a weapon
        assert not weapons.__contains__(self.iron_shield)  # In inventory, but not a weapon

    def test_get_armour(self):
        # when requesting the equipment in inventory.
        armours = self.inventory.get_equips()

        # then the gauntlets and shield are found, but dragon shield and rusty dagger is not.
        assert armours.__contains__(self.iron_shield)
        assert armours.__contains__(self.leather_gauntlets)
        assert not armours.__contains__(self.dragon_helmet)  # was not added
        assert not armours.__contains__(self.rusty_dagger)  # added but not an armour.

    def test_get_misc_items(self):
        pass  # no misc items yet

    def test_find(self):
        dagger = self.inventory.find(self.rusty_dagger.get_name())
        assert dagger == self.rusty_dagger
        assert dagger != self.iron_shield

    def test_find_in_empty_inventory(self):
        inventory = Inventory()
        # should be searchingInEmptyInventoryException
        with pytest.raises(NoItemFoundException):
            inventory.find(self.rusty_dagger.get_name())

    def test_wrong_name_find(self):
        with pytest.raises(NoItemFoundException):
            self.inventory.find('wrong name')

