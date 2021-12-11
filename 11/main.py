import copy
import numpy as np
import os

os.chdir("adventofcode2021/11")

with open("input.txt", 'r') as f:
    data = []
    r = f.read(1)
    line = []
    while r != '':
        if r == '\n':
            data.append(line)
            line = []
        else:
            line.append(int(r))
        r = f.read(1)

data = np.array(data)
print(data)

flashes = 0
flashed = np.zeros(np.shape(data),dtype=int)

def cval(y,x):
    global data
    global flashes
    global flashed

    if y < 0 or x < 0:
        return
    try:
        v = data[y,x]
    except:
        return

    if flashed[y,x] == 1:
        return
    
    if v >= 9:
        flashes += 1
        flashed[y,x] = 1
        data[y,x] = 0
        for x1 in range(x-1,x+2):
            for y1 in range(y-1,y+2):
                cval(y1,x1)
    else:
        data[y,x] += 1
        


for step in range(0,800):
    flashed[:,:] = 0
    # advance all by 1
    data += 1
    # check for 9
    for y in range(0,len(data)):
        for x in range(0,len(data[y])):
            if data[y,x] > 9 and flashed[y,x] == 0:
                cval(y,x)
    print(step+1)
    print(data)
    if np.all(data == 0):
        print(step+1)
        break
        
    

#print(flashes)
#print(data)
# wrong 1993