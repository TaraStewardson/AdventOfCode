with open('Day4.txt','r') as f:
    content = f.read()

lines = content.split('\n')

from collections import namedtuple
import re

def get_matches(card_nums, win_nums):
    matches = 0
    for num in card_nums:
        if num and num in win_nums: 
           matches +=1
    return matches

def get_points(matches):
    points = 0
    num = 0
    while num < matches:
        if num:
            points = points * 2
        else:
            points = 1
        num +=1
    return points

pattern = r"Card (\s*\d+): ((?:\s*\d{1,2}\s+){9}\s*\d{1,2}) \| ((?:\s*\d{1,2}\s+){24}\s*\d{1,2})" # 9, 24

Game = namedtuple('Game', ['num', 'multiplier', 'game_nums', 'winning_nums'])

games = []

for line in lines:
   match = re.search(pattern, line)
   if match: 
      game_nums = [x for x in match.group(2).split(' ') if x]
      winning_nums = [x for x in match.group(3).split(' ') if x]
      game = Game(match.group(1).strip(), 1, game_nums, winning_nums)
      games.append(game)

# Part 1
sum = 0

for game in games:
     matches = get_matches(game.game_nums, game.winning_nums)
     score = get_points(matches)
     sum += score

print(sum)


# Part 2 -------------------------------

total_cards = 0

n=0

while n < len(games):
    game = games[n]
    matches = get_matches(game.game_nums, game.winning_nums)
    i = 1 
    while i <= matches:
       newnum = games[n+i].multiplier + (1 * game.multiplier)
       newgame = Game(games[n+i].num, newnum, games[n+i].game_nums, games[n+i].winning_nums)
       games[n+i] = newgame
       i+=1
    n += 1

    total_cards += game.multiplier

print(total_cards)