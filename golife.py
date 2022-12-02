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
        self.zodiac = self.get_zodiac()

    def __repr__(self):
        return f"{self.hb}\n|Player Info\t\t|\n{self.hb} \
                \n|Name: {self.name}\t\t|\n|Age: {self.calc_age()}\t\t|\
                \n|Zodiac Sign: {self.get_zodiac()}\t|\
                \n{self.hb}\n|Skills\t\t\t|\n{self.hb}\n{self.get_skills()}"

    #converts timedelta to years
    def calc_age(self):
        return math.floor(self.age.days/365)

    def get_zodiac(self):
        zodiac_sign = False
        if self.birthday <= datetime.strptime("04-19", '%m-%d').replace(self.birthday.year) and \
           self.birthday >= datetime.strptime("03-20", '%m-%d').replace(self.birthday.year):
               zodiac_sign = "Aries"

        elif self.birthday >= datetime.strptime("04-20", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("05-20", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Bull"

        elif self.birthday >= datetime.strptime("05-21", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("06-21", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Gemini"

        elif self.birthday >= datetime.strptime("06-22", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("07-22", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Cancer"

        elif self.birthday >= datetime.strptime("07-23", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("08-22", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Leo"

        elif self.birthday >= datetime.strptime("08-23", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("09-22", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Virgo"

        elif self.birthday >= datetime.strptime("09-23", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("10-22", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Libra"

        elif self.birthday >= datetime.strptime("10-24", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("11-21", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Scorpius"

        elif self.birthday >= datetime.strptime("11-22", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("12-21", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Sagittarius"

        elif self.birthday >= datetime.strptime("01-20", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("02-18", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Aquarius"

        elif self.birthday >= datetime.strptime("02-19", '%m-%d').replace(self.birthday.year) and \
             self.birthday <= datetime.strptime("03-20", '%m-%d').replace(self.birthday.year):
                 zodiac_sign = "Pisces"

        else:
             zodiac_sign = "Capricornus"

        return zodiac_sign


    #Return a formated skill string (not implemented)
    def get_skills(self):
        skill_str = ""
        return skill_str

class Skills:
    def __init__(self, skill):
        self.skill = {skill: 0}

class Diary:
    pass
