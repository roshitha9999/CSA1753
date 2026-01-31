import heapq

def a_star(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            return g, path

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(
                    open_list,
                    (g + cost + heuristic[neighbor], g + cost, neighbor, path + [neighbor])
                )


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': []
}


heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}


cost, path = a_star(graph, heuristic, 'A', 'D')
print("Shortest path cost:", cost)
print("Shortest path:", " -> ".join(path))
