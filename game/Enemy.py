import random
import Character

class Enemy:
    life = 0
# keep using monsterlife to generate XP
    monsterLife = life
    monster = ""
    expTillNextLevel = 0
    monsterdamage = 0
    monsterLevel = 0

    # Check if enemy death
    def isDeath(self):
        if self.Enemy.life <= 0:
            return True
        else:
            return False

    # have input for area with default
    def monsterType(self, location1):
        #monsterList = ["Bunny", "Deer", "Small Goblin", "Big Goblin", "Werewolf",
        #               "Ogre", "Armoured Ogre", "Small Dragon", "Dragon", "Dark Wyvern", "Dark Spawn", "Cold One"]
        # have monster families
        monsterFamilyDict = {"Goblins": ["Goblin Infant", "Small Goblin", "Small Armoured Goblin", "Big Goblin", "Big Armoured Goblin", "Goblin General", "Goblin Hero"],
                             "Ogres": ["Ogre Infant", "Small Ogre", "Small Armoured Ogre", "Big Ogre", "Big Armoured Ogre", "Ogre General", "Ogre Hero"],
                             "Dragons": ["Baby Dragom", "Small Red Dragon", "Small Battle Hardened Dragon", "Big Crimson Dragon"]
                            }

# have level generation instead of hp generation
        location = location1.location
        maxLevel = location1.locationProperties[location]["levelRange"]
        generatedMonsterLevel = random.randrange(maxLevel[0], maxLevel[1])
        self.monsterLevel = generatedMonsterLevel

# generate hp
        baseHP = generatedMonsterLevel * 10
        baseHP += random.randrange(-9, 9)
# limit monsters based on area
        #get the list of monsters, count length and throw a random to determine which one it is, then put the winning monster in a var
        acceptedMonstersForThisLocation = location1.locationProperties[location]["monstertypes"]
        numberedMonsterList = len(acceptedMonstersForThisLocation)
        determineWhatMonsterToChooseFromList = random.randrange(0, numberedMonsterList)
        #determine what monster in the family:
        familyname = acceptedMonstersForThisLocation[determineWhatMonsterToChooseFromList]
        numberOfMonstersInFamily = monsterFamilyDict[familyname]
        x = len(numberOfMonstersInFamily)
        # change self.monster into a random monster from the right monster group.
        self.monster = monsterFamilyDict[familyname][random.randrange(0, x)]
        # generate stats for that monster
        self.monsterLife = baseHP
        self.life = baseHP

        self.monsterdamage = self.monsterLevel + random.randrange(0, 4)

    def attack(self):
        print("you make a swing for it and hit the " + self.monster + " perfectly on the spot ")
        print("the " + self.monster + " makes a painful sound!")
        self.life -= Character.Character.stats["strength"] + Character.Character.equipedWeapon[1]
        Character.Character.equipedWeapon[2] -= 1
        if Character.Character.equipedWeapon[2] <= 0:
            Character.Character.equipedWeapon[:] = []
            print("Your weapon makes a 'cling' sound as it breaks, to bad we have to move on without a weapon")

    def checkLife(self):
        if self.life <= 0:
            print("The " + self.monster + " falls down and makes it last wail before it dies")
        else:
            print("the " + self.monster + " has " + str(self.life) + " life left")