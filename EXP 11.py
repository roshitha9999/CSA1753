states = ['A', 'B', 'C', 'D']

adjacency = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue', 'Yellow']

result = {}

def map_coloring(index):
    if index == len(states):
        print(result)
        return True   

    state = states[index]
    for color in colors:
        if all(result.get(neigh) != color for neigh in adjacency[state]):
            result[state] = color
            if map_coloring(index + 1):
                return True
            del result[state]

map_coloring(0)
