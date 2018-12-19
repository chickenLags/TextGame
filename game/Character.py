import random


class Character:





    def __init__(self):
        self.stats = {"level": 1,  "title": "Wanderer",  "strength": 1,  "experience": 0, "hp": 20}
        self.inventory = []

    def equipweapon(self, weapon):
        self.weapon = weapon

    def getInventoryAsList(self):
        temp = []
        for item in self.inventory:
            temp.append(item.name);
        return temp

    def getDamage(self):
        return self.stats['strength'] + self.weapon.getDamage()

    def weaponErosion(self):
        self.weapon.erode()
        if self.weapon.durability <= 0:
            self.weapon = None
            print("Your weapon makes a 'cling' sound as it breaks, too bad I will have to move on without a weapon")


    def maxExperience(self):
        tempExpCap = self.stats["level"]
        expTillNextLevel = tempExpCap * tempExpCap + 20
        return expTillNextLevel

    def damage(self, damage):
        self.stats["hp"] -= damage

    def isAlive(self):
        if self.stats["hp"] <= 0:
            return False
        return True

    def die(self):
        print("\"if only I had not entered this wretched forest\" Regret fills your mind as the light leaves your eyes")
        potato = input("You are dead!")
        quit()


    def experience_gain(self, expReceived):
        totalExp = self.stats["experience"] + expReceived
        expLeft = True

        while expLeft:
            expTillNextLevel = self.maxExperience()
            if totalExp < expTillNextLevel:
                self.stats["experience"] += expReceived
                print("You chalk it up to experience ( " + str(expReceived) + " EXP obtained)")
                expLeft = False
            else:
                print("You feel stronger, what a great feeling! And you feel completely Restored!!")
                self.stats["experience"] = 0
                self.stats["level"] += 1
                self.stats["strength"] += random.randrange(1, 3)
                self.stats["hp"] = 10 * self.stats["level"]
                totalExp = expReceived - expTillNextLevel