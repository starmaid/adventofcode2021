import copy
import numpy as np
import os

os.chdir("adventofcode2021/9")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n'))

#print(data)

def getval(data,x,y):
    if x < 0 or y < 0:
        return 9
    try:
        return data[y][x]
    except:
        return 9

lowsum = 0
lowpoints = []
lows = np.zeros((len(data),len(data[0])),dtype=int)

for r in range(0,len(data)):
    for c in range(0,len(data[r])):
        val = data[r][c]
        sides = []
        #left
        sides.append(getval(data,c-1,r))
        sides.append(getval(data,c+1,r))
        sides.append(getval(data,c,r-1))
        sides.append(getval(data,c,r+1))

        ans = True
        for i in sides:
            if int(val) >= int(i):
                ans = False
                break
        if ans:
            lowsum += 1 + int(data[r][c])
            lows[r,c] = 1
            lowpoints.append([c,r])

print(lowsum)

traversed = np.zeros((len(data),len(data[0])),dtype=int)
areas = np.zeros(len(lowpoints),dtype=int)

# part 2
# start at each low point
# have a radius from that low point
# for each 
# check each side
# check the slope
# if slope 

def trav(x,y,a):
    if x < 0 or y < 0:
        return
    try:
        v = data[y][x]
    except:
        return

    global traversed
    global areas

    if traversed[y,x] == 1:
        # weve already been here
        return
    else:
        sides = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        v = data[y][x]
        if int(v) != 9:
            # we are in this basin
            areas[a] += 1
            traversed[y,x] = 1
        else:
            return
        
        for s in sides:
            trav(s[0],s[1],a)


for lowp in range(0,len(lowpoints)):
    trav(lowpoints[lowp][0],lowpoints[lowp][1],lowp)
    
print(areas)
sareas = np.sort(areas)
print(sareas[-1]*sareas[-2]*sareas[-3])