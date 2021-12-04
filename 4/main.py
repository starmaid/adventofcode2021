with open("input.txt", 'r') as f:
    c = f.readline().split(',')
    calls = []
    for i in c:
        calls.append(int(i))
    l = f.readline()
    boards = []
    while l != '':
        rows = []
        for i in range(0,5):
            row = []
            for j in range(0,5):
                row.append(int(f.read(2)))
                #print(row)
                f.read(1)
            rows.append(row)
        boards.append(rows)
        l = f.readline()

import copy
import numpy as np
boards = np.array(boards)
checks = np.zeros(boards.shape, dtype=int)
t2w = np.zeros(len(boards), dtype=int)

for b in range(0,len(boards)):
    for call in range(0,len(calls)):
        # add it to checks
        n = calls[call]
        for r in range(0,5):
            for c in range(0,5):
                if n == boards[b,r,c]:
                    checks[b,r,c] = 1
        
        win = 0
        for r in range(0,5):
            if np.sum(checks[b,r,:]) == 5:
                win = 1
        
        for c in range(0,5):
            if np.sum(checks[b,:,c]) == 5:
                win = 1
        
        if win == 1:
            t2w[b] = call
            break
        
        # check all rows if the board has won
        # check all cols if board won

print(t2w)

board = np.where(t2w==min(t2w))[0][0]
# board 49
s = 0
for r in range(0,5):
    for c in range(0,5):
        if checks[board,r,c] == 0:
            s += boards[board,r,c]

# sum = 871
score = s * calls[min(t2w)]
print(score)

board = np.where(t2w==max(t2w))[0][0]
# board 49
s = 0
for r in range(0,5):
    for c in range(0,5):
        if checks[board,r,c] == 0:
            s += boards[board,r,c]

# sum = 871
score = s * calls[max(t2w)]
print(score)