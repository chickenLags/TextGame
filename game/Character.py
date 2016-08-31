import random


class Character:
    stats = {"level": 1,
             "title": "Wanderer",
             "strength": 1,
             "experience": 0,
             "hp": 20}

    equipedWeapon = ["Rusty Dagger", 2, 10]
    inventoryDict = []

    def displayInventory(self):
        temp = []
        for banaan in Character.inventoryDict:
            temp.append(banaan[0])
        print(temp)

    def maxExperience(self):
        tempExpCap = self.Character.stats["level"]
        expTillNextLevel = tempExpCap * tempExpCap + 20
        return expTillNextLevel

    def counter(self, enemy1):
        self.Character.stats["hp"] -= enemy1.monsterdamage
        print("the " + enemy1.monster + " beared its claws to you and did " + str(enemy1.monsterdamage) + " damage to you!")
        if self.Character.stats["hp"] <= 0:
            print("As you feel the claws pierce through your flesh you feel your life leaving you.")
            print("\"if only i had not entered this wreched forest\" Regret fills your mind as the light leaves your eyes")
            print("You are dead!")
            quit()

    def experience_gain(self, enemy1):
        expReceived = enemy1.monsterLife * 2 + 4
        totalExp = self.Character.stats["experience"] + expReceived
        expLeft = True

        while expLeft:
            expTillNextLevel = self.Character.maxExperience(self)
            if totalExp < expTillNextLevel:
                self.Character.stats["experience"] += expReceived
                print("You chalk it up to experience ( " + str(expReceived) + " EXP obtained)")
                expLeft = False
            else:
                print("You feel stronger, what a great feeling! And you feel completely Restored!!")
                self.Character.stats["experience"] = 0
                self.Character.stats["level"] += 1
                self.Character.stats["strength"] += random.randrange(1, 3)
                self.Character.stats["hp"] = 10 * self.Character.stats["level"]
                totalExp = expReceived - expTillNextLevel