import copy
import numpy as np
import os

os.chdir("adventofcode2021/10")

with open("input.txt", 'r') as f:
    d = f.readlines()
    data = []
    for i in d:
        data.append(i.strip('\n'))

errors = {')':0, ']':0, '}':0, '>':0}

closes = {'(':')', '[':']', '{':'}', '<':'>'}
conts = []
    
for l in data:
    stack = []
    err = False
    for c in range(0,len(l)):
        char = l[c]
        if char in closes.keys():
            stack.append(char)
        else:
            try:
                start = stack.pop()
                if char == closes[start]:
                    continue
                else:
                    errors[char] += 1
                    err = True
                    break
            except:
                errors[char] += 1
                err = True
                break
    if not err and len(stack) > 0:
        conts.append(stack)
            
score = errors[')'] * 3 + errors[']'] * 57 + errors['}'] * 1197 + errors['>'] * 25137

print(errors)
print(score)

scores = np.zeros(len(conts))

scodes = {'(':1, '[':2, '{':3, '<':4}

for s in range(0,len(conts)):
    while len(conts[s]) > 0:
        scores[s] *= 5
        scores[s] += scodes[conts[s].pop()]

print(scores)

print(np.sort(scores)[int(len(scores)/2)])

#165561627