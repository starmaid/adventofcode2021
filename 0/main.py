import copy
import numpy as np
import os
import math as m

os.chdir("adventofcode2021/6")

with open("input.txt", 'r') as f:
    d = f.readline().split(',')
    data = []
    for i in d:
        data.append(int(i))