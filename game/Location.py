class Location:
    name = "Dark Forest"

    # properties of location:
    # name, what monsters, level range
    # option for future additions.

    properties = {"Default":
                      {"monstertypes":["Goblins", "Ogres", "Dragons"],
                       "levelRange": [1, 100]},
                  "Forest":
                      {"monstertypes": ["Goblins"],
                       "levelRange": [10, 20]},
                  "Dark Forest":
                      {"monstertypes": ["Goblins"],
                       "levelRange": [1, 2]}
                  }

    def getMonster(self, random):
        monsterType = self.properties[self.name]['monstertypes'][random.randrange(0, len(self.properties[self.name]["monstertypes"]))]
        return monsterType

    def getLevelRange(self):
        return self.properties[self.name]["levelRange"]