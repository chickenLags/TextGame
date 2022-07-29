from Enemy import Enemy
from locations.location_base import LocationBase


class LocationCombatInstance(LocationBase):
    def __init__(self, instance, character):
        super(LocationCombatInstance, self).__init__(instance, character)
        self.enemy = Enemy(instance.getParentInstance())    # location should be changed to allow for enemy creation
        self.character = character
        self.instance = instance
        self.entryMessages.append("You encountered a lvl." + str(self.enemy.level) + " " + str(self.enemy.name) + ".")
        self.inputMessage = 'you can attack, run or examine the enemy with scan\n'

        self.name = "combat"


        attackLambda = lambda : self.enemy.attack(self.character, self.instance)
        self.actions.append( LocationBase.Action("Attack", LocationBase.Action.attack, [], [attackLambda], []))
        self.actions.append( LocationBase.Action("Run", LocationBase.Action.run, [], [self.run], []) )
        self.actions.append(LocationBase.Action("Examine", LocationBase.Action.examine, [], [self.enemy.check_life], []))


    def run(self):
        if self.RNG_under_ten() <= 5:
            print("you failed to escape from the " + self.enemy.name)
            self.character.attack(self.enemy)
        else:
            print("As fast as you can you leave the " + self.enemy.name + " behind...")
            self.instance.leaveInstance()


    def attemptAttack(self, argument):
        if self.RNG_under_ten() >= 3:  # determines whether i hit the enemy
            self.enemy.attack(self.character, self.instance)
