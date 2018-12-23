import random
from Items import itemType
class Enemy:
    # monsterList = ["Bunny", "Deer", "Small Goblin", "Big Goblin", "Werewolf",
    #               "Ogre", "Armoured Ogre", "Small Dragon", "Dragon", "Dark Wyvern", "Dark Spawn", "Cold One"]
    sizes = ["fat", "small", "big", "average", "thin", "poor"]
    variations = ["infant", "armoured", "adult", 'old', 'crimson', "battle hardened", "red", "baby"]


    def __init__(self, location):

        self.level = random.randrange(location.levelRange[0], location.levelRange[1])
        self.life = self.level * 10
        self.life += random.randrange(-9, 9)
        self.maxHP = self.life
        self.size = Enemy.sizes[random.randint(0, len(Enemy.sizes) - 1 )]
        self.variation = Enemy.variations[random.randint(0, len(Enemy.variations) - 1 )]
        self.type = location.enemies[random.randint( 0, len( location.enemies ) - 1 )]

        self.name = str(self.size) + " " + str(self.variation) + " " + str(self.type)
        self.monsterdamage = self.level + random.randrange(0, 4)


    # Check if enemy death
    def isDead(self):
        if self.life <= 0:
            return True
        else:
            return False

    def attack(self, character, instance):
            # attempt to damage the monster
        if random.randint(0, 100) < 70:
            self.life -= character.getDamage()
            print("you swing your " + str(character.equipment.getName(itemType.WEAPON)) + " and hit the " + self.name + " for " + str(character.getDamage()) + ".")
            print("enemy has " + str(self.life) + " left.")
            character.weaponErosion()
        else:
            print("The " + self.name + " avoided the hit")

            # if monster is dead
        if self.isDead():
            print("The " + self.name + " falls down and makes it last wail before it dies")
            character.experience_gain(self.getExperience())
            if random.randint(0, 100) < 20:
                character.inventory.add(instance.itemManager.generateWeapon())
            instance.leaveInstance()
        else:
            character.attack(self)


    def getDamage(self):
        print("the " + self.name + " beared its claws and did " + str(self.monsterdamage) + " damage to you!")
        return self.monsterdamage

    def getDeathMessage(self):
        return "As you feel the claws pierce through your flesh you feel your life leaving you."

    def getExperience(self):
        return self.maxHP * 2 + 4
        pass

    def checkLife(self):
        if self.life <= 0:
            print("The " + self.name + " falls down and makes it last wail before it dies")
        else:
            print("the " + self.name + " has " + str(self.life) + " life left")