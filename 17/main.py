import copy
import numpy as np
import os
import math as m

os.chdir("adventofcode2021/17")

#lets just shoot at the area and see what hits
#max downward v is 61

# to find x just use the arithmetic sum backwards
# this just has to hit the target, and will ideally
# get there much earlier than the y
vx0 = (-1 + m.sqrt(1 + 4 * 2 * 155)) / 2
vx0 = 20
#18-20

def step(pos,vel):
    pos1 = [pos[0] + vel[0], pos[1] + vel[1]]
    vel1 = [0,0]
    if vel[0] != 0:
        vel1[0] = vel[0] - (vel[0]/abs(vel[0]))
    vel1[1] = vel[1] - 1
    return pos1,vel1

'''
#max vy0 = 132
maxy = 0
for vy0 in range(100,200):
    print(vy0)
    pos = [0,0]
    vel = [vx0,vy0]    
    while pos[1] > -72:
        pos,vel = step(pos,vel)
        if pos[1] > maxy:
            maxy = pos[1]
    print(pos)
    print(vel)
    #print(maxy)
    if pos[1] < -132:
        break
'''


#alright i dont give a fuck lets brute force this
c = 0
for vx0 in range(18,400):
    for vy0 in range(-400,132):
        pos = [0,0]
        vel = [vx0,vy0]    
        while True:
            pos1,vel1 = step(pos,vel)
            if pos1[0] > 215 or pos1[1] < -132:
                if pos[0] >= 155 and pos[1] <= -72:
                    c += 1
                    print([vx0,vy0])
                    break
                else:
                    break
            pos = pos1
            vel = vel1

print(c)