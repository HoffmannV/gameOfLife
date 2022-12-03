from datetime import datetime
import math

hb = ""
for x in range(33):
    hb += "-"

def draw_hb(size):
    horizontal_bar = ""
    for x in range(size):
        horizontal_bar += "-"
    return horizontal_bar


class Player:

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.age = datetime.now() - self.birthday
        self.skills = []
        self.zodiac = self.get_zodiac()

    def __repr__(self):
        return f"{hb}\n|Player Info\t\t\t|\n{hb} \
                \n Name:\t\t{self.name}\
                \n Age:\t\t{self.calc_age()}\
                \n Zodiac Sign:\t{self.get_zodiac()}\
                \n{hb}\n|Skills\t\t\t\t|\n{hb}\n{self.get_skills()}"

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

class Skill:
    def __init__(self, skill):
        self.skill = {skill: [0, 0]}
    
    def add_experience(self, skill, time):
        lvl_skill = self.skill[skill]
        lvl_skill[1] += time
        experience = lvl_skill[1]
        lvl_skill[0] = math.floor(experience / 60)

        self.skill[skill] = lvl_skill

        return lvl_skill

class Diary:
    topic = ""
    entry = ""
    details = []

    def __init__(self):
        self.dates = []

    def __repr__(self):
        return f""

    def add_entry(self):
        self.dates.append(datetime.now())
        topic = input("Enter here what activities you did today (One word for each activity separated by a comma)\n")

        skills = topic.split(',')
        skills = [skill.strip().title() for skill in skills]

        for skill in skills:
            self.entry += "{}\n{}\n".format(self.format_title("Activity"), skill)
            time = input(f"How much time did you spend on {skill}(in minutes):")
            new_skill = Skill(skill)
            self.entry += "{}\n{}\n".format(self.format_title("Time spent"), time)
            new_skill.add_experience(skill, int(time))
            subject = input(f"Subject (optional):")
            self.entry += "{}\n{}\n".format(self.format_title("Subject"), subject)
            print(f"You can add additional details\n{hb}\n")
            currLine = " "
            while currLine != "":
                currLine = input()
                if currLine != "":
                    self.details.append(currLine)
            self.entry += "{}\n{}\n\n\nDate: {}\n{}".format(self.format_title("Details"), '\n'.join(self.details), datetime.now().strftime("%A, %d. %B %Y"), draw_hb(40))

        return self.entry

    def format_title(self, title, str_length=40):
        formated_title = ""
        title_len = len(title)
        title_start = math.floor((str_length - title_len)/2)

        counter = 0
        for x in range(str_length):
            if x < title_start or x > title_start + title_len:
                formated_title += "-"

            elif counter < title_len:
                formated_title += title[counter]
                counter += 1

            else:
                formated_title += "-"

        return formated_title


diary = Diary()
print(diary.add_entry())
#print(diary.format_title("Article", 40))
#print(diary.details)
#print(diary.print_skills())
