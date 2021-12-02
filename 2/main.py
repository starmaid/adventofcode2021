with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        w = i.strip('\n')
        move = w.split(' ')[0]
        val = int(w.split(' ')[1])
        data.append([move, val])

depth = 0
hpos = 0

for i in data:
    if i[0] == "forward":
        hpos += i[1]
    elif i[0] == "down":
        depth += i[1]
    elif i[0] == "up":
        depth -= i[1]

#guess 1 3970220
#guess 2 2187380 correct

depth = 0
hpos = 0
aim = 0

for i in data:
    if i[0] == "forward":
        hpos += i[1]
        depth += aim*i[1]
    elif i[0] == "down":
        aim += i[1]
    elif i[0] == "up":
        aim -= i[1]