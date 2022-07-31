from enum import Enum


# Order of items here determine order of display in equipment/ character.display_stats
class ItemType(Enum):
    WEAPON = 1
    OFFHAND = 7
    SHIELD = 2
    HEAD = 6
    BODY = 5
    HANDS = 3
    LEGS = 4

