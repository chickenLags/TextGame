import random
import Character

class Enemy:
    variations = {
        "Goblins": ["Goblin Infant", "Small Goblin", "Small Armoured Goblin", "Big Goblin", "Big Armoured Goblin",
                    "Goblin General", "Goblin Hero"],
        "Ogres": ["Ogre Infant", "Small Ogre", "Small Armoured Ogre", "Big Ogre", "Big Armoured Ogre", "Ogre General",
                  "Ogre Hero"],
        "Dragons": ["Baby Dragom", "Small Red Dragon", "Small Battle Hardened Dragon", "Big Crimson Dragon"]
        }
    # monsterList = ["Bunny", "Deer", "Small Goblin", "Big Goblin", "Werewolf",
    #               "Ogre", "Armoured Ogre", "Small Dragon", "Dragon", "Dark Wyvern", "Dark Spawn", "Cold One"]


    def __init__(self, location):

        self.level = random.randrange(location.getLevelRange()[0], location.getLevelRange()[1])
        # generate hp
        self.life = self.level * 10
        self.life += random.randrange(-9, 9)
        self.maxHP = self.life
        monsterBase = location.getMonster(random);
        self.name = self.variations[monsterBase][random.randrange(0, len(self.variations[monsterBase]))]
        self.monsterdamage = self.level + random.randrange(0, 4)


    # Check if enemy death
    def isDead(self):
        if self.life <= 0:
            return True
        else:
            return False

    def damage(self, damage):
        self.life -= damage

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