with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n'))

items = len(data)
record = [0,0,0,0,0,0,0,0,0,0,0,0]
for i in data:
    for a in range(0,12):
        if i[a] == '1':
            record[a] += 1

#most common
#010111100100
eps = int('010111100100',2)
#1508
#101000011011
#2587

#3901196

import copy


com = ''
d1 = copy.deepcopy(data)
record = [0,0,0,0,0,0,0,0,0,0,0,0]

for a in range(0,12):
    l = len(d1)
    for j in d1:
        if j[a] == '1':
            record[a] += 1
    
    if record[a] >= l/2:
        com = '1'
    else:
        com = '0'
    
    i = 0
    while i < l:
        if d1[i][a] != com:
            d1.remove(d1[i])
            l -= 1
        else:
            i += 1
        if l == 1:
            break
    if l == 1:
        break

#010111100100 wrong
#1508 wrong

#011001100100
#1636


com = ''
d2 = copy.deepcopy(data)
record = [0,0,0,0,0,0,0,0,0,0,0,0]

for a in range(0,12):
    l = len(d2)
    for j in d2:
        if j[a] == '1':
            record[a] += 1
    
    if record[a] >= l/2:
        com = '0'
    else:
        com = '1'
    
    i = 0
    while i < l:
        if d2[i][a] != com:
            d2.remove(d2[i])
            l -= 1
        else:
            i += 1
        if l == 1:
            break
    if l == 1:
        break


#101000010001 wrong
#2577 wrong
#101010010111
#2711

#3886116 incorrect
#4435196 incorrect????

