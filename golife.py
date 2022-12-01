from datetime import datetime
import math

class Player:

    #hb is the horizontal bar
    hb = ""
    for x in range(25):
        hb += "-"

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.age = datetime.now() - self.birthday
        self.skills = []

    def __repr__(self):
        return f"{self.hb}\n|Player Info\t\t|\n{self.hb} \
                \n|Name: {self.name}\t\t|\n|Age:  {self.calc_age()}\t\t|\n{self.hb}\n|Skills\t\t\t|\n{self.hb}\n{self.get_skills()}"
    
    #converts timedelta to years
    def calc_age(self):
        return math.floor(self.age.days/365)

    
    #Return a formated skill string (not implemented)
    def get_skills(self):
        skill_str = ""
        return skill_str

class Skills:
    def __init__(self, skill):
        self.skill = {skill: 0}

class Diary:
    pass

