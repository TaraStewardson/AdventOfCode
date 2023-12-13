numbers = {"zero": 0,"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9}

with open("Day1.txt", 'r') as f:
    text = f.read()

text = text.split('\n')

# Part 1:
sum = 0

for line in text:
    newline = ""
    for char in line:
        if char.isnumeric():
            newline += char
    lineval = str(newline[0]) + str(newline[-1])
    sum += int(lineval)

print(sum)

# Part 2
sum = 0

for line in text:
    newline = ""
    n = 0
    while n < len(line):
        if line[n].isnumeric():
            newline += line[n]
        for key in numbers.keys():
            if line[n:n+len(key)] == key:
                newline += str(numbers[key])
        n += 1
    lineval = str(newline[0]) + str(newline[-1])
    sum += int(lineval)

print(sum)
