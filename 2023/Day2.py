
with open("Day2.txt", "r") as f:
    text = f.read()
    text = text.split('\n')

# Part 1
sum = 0

def process_line(line):
    i = 0
    number = 0
    while i < len(line):
        if line[i].isnumeric():
            if line[i+1].isnumeric():
                number = int(line[i]+line[i+1])
                color = line[i+3]
            else:
                number = line[i]
                color = line[i+2]
            match color:
                case 'r':
                    if int(number)>12:
                        return False
                case 'g':
                    if int(number)>13:
                        return False
                case 'b': 
                    if int(number)>14:
                        return False
        i += 1
    return True

for line in text:
    game, results = line.split(":")
    valid = process_line(results)
    if valid:
        gamenum = game.split(" ")[1]
        sum += int(gamenum)

print(sum)

# Part 2
sum = 0

dict = {'r':0, 'g':1,'b':2}

def process_line(line):
    rgb = [0,0,0]
    i = 0
    while i < len(line):
        if line[i].isnumeric():
            if line[i+1].isnumeric():
                number = int(line[i]+line[i+1])
                color = line[i+3]
            else:
                number = line[i]
                color = line[i+2]
            if color in "rgb":
                index = dict[color]
                if rgb[index]<int(number):
                    rgb[index] = int(number)
        i += 1
    return rgb


for line in text:
    rgb = process_line(line)
    print(line)
    sumrgb = rgb[0]*rgb[1]*rgb[2]
    print(rgb)
    print(sumrgb)
    sum += sumrgb

print(sum)