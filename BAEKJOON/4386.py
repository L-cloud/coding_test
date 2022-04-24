import sys

N = int(sys.stdin.readline())
stars = [list(map(float,sys.stdin.readline().split())) for _ in range(N)]
cost, cost_starts = 0, []
node = stars.pop()
min_dist,min_index = float('inf'), 0
for index,star in enumerate(stars):
    dist = ((node[0] - star[0]) ** 2 + (node[1] - star[1]) ** 2)**(1/2)
    if dist < min_dist:
        min_dist = dist
        min_index = index
    cost_starts.append([dist, star[0], star[1]])

for _ in range(N-1):
    node = cost_starts[min_index][:]
    cost += node[0]
    del cost_starts[min_index]
    min_dist,min_index = float('inf'), 0
    for index, star in enumerate(cost_starts):
        star[0] = min(((node[1] - star[1]) ** 2 + (node[2] - star[2]) ** 2)**(1/2),star[0])
        if star[0] < min_dist:
            min_dist = star[0]
            min_index = index

print(round(cost,2))

