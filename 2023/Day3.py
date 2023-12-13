with open("Day3.txt", 'r') as f:
    data = f.read()

matrix = data.split('\n')

# rows, columns

matrix_len = 139

# Part 1 ---------------------------------------------------------------------------------------

def is_a_part(symbolloc):
    # pass in a list of tuples, where symbols should be found if this number is an engine part
    symbols = ''
    for c in symbolloc:
        char = matrix[c[0]][c[1]]
        if char in "!@#$%^&*()/+-=":
            return True
        elif char not in "1234567890" and char != '.':
            print(char)
        symbols += char
    return False

def get_surrounds(numberloc):
    symbolloc = [] # a list of coordinates where symbols should be found
    # pass in a list of tuples, ie. [(1,0), (1,1), (1,2)] for the number 565 in row 1, positions 0, 1 & 2
    n = 0
    for c in numberloc:
        if c[1] and c[0]:
            symbolloc.append((c[0]-1, c[1]-1)) # pos 1
        if c[0]:
            symbolloc.append((c[0]-1, c[1])) # pos 2
            if c[1]<matrix_len:
                symbolloc.append((c[0]-1, c[1]+1)) # pos 3
        if c[1]:
            if n == 0:
                symbolloc.append((c[0], c[1]-1)) # pos 4
            if c[0]<matrix_len:
                symbolloc.append((c[0]+1, c[1]-1)) # pos 7
        if c[1]<matrix_len:
            if c[0]<matrix_len:
                symbolloc.append((c[0]+1, c[1]+1)) # pos 9
            if n+1 == len(numberloc):
                symbolloc.append((c[0], c[1]+1)) # pos 6
        if c[0]<matrix_len:
            symbolloc.append((c[0]+1, c[1])) # pos 8
        n += 1
    symbolloc = list(dict.fromkeys(symbolloc)) # removes duplicates
    part = is_a_part(symbolloc)
    return(part)

sum = 0

r = 0
while r < len(matrix):
    c = 0
    while c < len(matrix[r]):
        digit = matrix[r][c]
        number = ''
        numberloc = []
        while digit.isnumeric():
            number += digit
            numberloc.append((r, c))
            c += 1
            if c<len(matrix[r]):
                digit = matrix[r][c]
            else: 
                break
        if numberloc:
            part = get_surrounds(numberloc)
            if part:
                sum += int(number)
        c += 1
    r+=1

print(sum)


# Part 2 --------------------------------------------------------------------

sum = 0

def get_surrounds(numberloc):
    symbolloc = [] # a list of coordinates where symbols should be found
    # pass in a list of tuples, ie. [(1,0), (1,1), (1,2)] for the number 565 in row 1, positions 0, 1 & 2
    n = 0
    for c in numberloc:
        if c[1] and c[0]:
            symbolloc.append((c[0]-1, c[1]-1)) # pos 1
        if c[0]:
            symbolloc.append((c[0]-1, c[1])) # pos 2
            if c[1]<matrix_len:
                symbolloc.append((c[0]-1, c[1]+1)) # pos 3
        if c[1]:
            if n == 0:
                symbolloc.append((c[0], c[1]-1)) # pos 4
            if c[0]<matrix_len:
                symbolloc.append((c[0]+1, c[1]-1)) # pos 7
        if c[1]<matrix_len:
            if c[0]<matrix_len:
                symbolloc.append((c[0]+1, c[1]+1)) # pos 9
            if n+1 == len(numberloc):
                symbolloc.append((c[0], c[1]+1)) # pos 6
        if c[0]<matrix_len:
            symbolloc.append((c[0]+1, c[1])) # pos 8
        n += 1
    symbolloc = list(dict.fromkeys(symbolloc)) # removes duplicates

    gears = [] # coord list for gears
    for c in symbolloc:
        char = matrix[c[0]][c[1]]
        if char == "*":
            gears.append(c)
    return gears

sum = 0
gear_dict = {}

r = 0
while r < len(matrix):
    c = 0
    while c < len(matrix[r]):
        digit = matrix[r][c]
        number = ''
        numberloc = []
        while digit.isnumeric():
            number += digit
            numberloc.append((r, c))
            c += 1
            if c<len(matrix[r]):
                digit = matrix[r][c]
            else: 
                break
        if numberloc:
            gears = get_surrounds(numberloc)
            for gear in gears:
                if gear in gear_dict.keys():
                    gear_dict[gear].append(number)
                else: 
                    gear_dict.update({gear: [number]})
        c += 1
    r+=1

for gear in gear_dict.keys():
    nums = gear_dict[gear]
    if len(nums)==2:
        sum += int(nums[0])*int(nums[1])

print(sum)
