from golife import Player
from datetime import datetime

print('Welcome to the GAME OF LIFE')

name = input('What is your name ?\n')
date_str = input('What is your birthday [Format: TT.MM.YYYY]?\n')
birthday = datetime.strptime(date_str, '%d.%m.%Y')

player = Player(name, birthday)
print(player)
