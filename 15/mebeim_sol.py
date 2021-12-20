#hey gamers
#several days passed without me doing advent of code
#was very busy being drunk and going out
#im getting back on the train here and to get me over the
#"i dont feel like coding ANOTHER dijkstra's like we did in class"
#im just using this reddit code from github.com/mebeim
# to try and get my momentum back

#from utils import advent
import heapq
from math import inf as INFINITY
from collections import defaultdict
from itertools import filterfalse

def neighbors4(r, c, h, w):
	for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		rr, cc = (r + dr, c + dc)
		if 0 <= rr < w and 0 <= cc < h:
			yield rr, cc

def dijkstra(grid):
	h, w = len(grid), len(grid[0])
	source = (0, 0)
	destination = (h - 1, w - 1)

	queue = [(0, source)]
	mindist = defaultdict(lambda: INFINITY, {source: 0})
	visited = set()

	while queue:
		dist, node = heapq.heappop(queue)

		if node == destination:
			return dist

		if node in visited:
			continue

		visited.add(node)
		r, c = node

		for neighbor in filterfalse(visited.__contains__, neighbors4(r, c, h, w)):
			nr, nc  = neighbor
			newdist = dist + grid[nr][nc]

			if newdist < mindist[neighbor]:
				mindist[neighbor] = newdist
				heapq.heappush(queue, (newdist, neighbor))

	return INFINITY


#advent.setup(2021, 15)
#fin = advent.get_input()
import os
os.chdir("adventofcode2021/15")
fin = open("input.txt", 'r')


grid    = list(list(map(int, row)) for row in map(str.rstrip, fin))
minrisk = dijkstra(grid)

#advent.print_answer(1, minrisk)
print(minrisk)


tilew = len(grid)
tileh = len(grid[0])

for _ in range(4):
	for row in grid:
		tail = row[-tilew:]
		row.extend((x + 1) if x < 9 else 1 for x in tail)

for _ in range(4):
	for row in grid[-tileh:]:
		row = [(x + 1) if x < 9 else 1 for x in row]
		grid.append(row)

minrisk = dijkstra(grid)
#advent.print_answer(2, minrisk)
print(minrisk)