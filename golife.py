class Player:

    #hb is the horizontal bar
    hb = ""
    for x in range(25):
        hb += "-"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = []

    def __repr__(self):
        return f"{self.hb}\n|Player Info\t\t|\n{self.hb} \
                \n|Name: {self.name}\t\t|\n|Age:  {self.age}\t\t|\n{self.hb}\n|Skills\t\t\t|\n{self.hb}\n{self.get_skills()}"

    
    #Return a formated skill string (not implemented)
    def get_skills(self):
        skill_str = ""
        return skill_str

class Skills:
    def __init__(self, skill):
        self.skill = {skill: 0}

class Diary:
    pass

player = Player("Vladimir", 30)
print(player)
