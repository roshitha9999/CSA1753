import itertools


distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(distance)
cities = range(n)
min_cost = float('inf')
best_path = None

for path in itertools.permutations(cities):
    cost = 0
    for i in range(n - 1):
        cost += distance[path[i]][path[i + 1]]
    cost += distance[path[-1]][path[0]]  

    if cost < min_cost:
        min_cost = cost
        best_path = path

print("Minimum travelling cost:", min_cost)
print("Best path:", best_path)
