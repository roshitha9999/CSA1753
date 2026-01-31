from heapq import heappush, heappop

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

MOVES = {
    0:[1,3],1:[0,2,4],2:[1,5],
    3:[0,4,6],4:[1,3,5,7],5:[2,4,8],
    6:[3,7],7:[4,6,8],8:[5,7]
}

def manhattan(state):
    d = 0
    for i in range(9):
        if state[i] != 0:
            g = GOAL_STATE.index(state[i])
            d += abs(i//3 - g//3) + abs(i%3 - g%3)
    return d

def neighbors(state):
    n = []
    z = state.index(0)
    for m in MOVES[z]:
        s = list(state)
        s[z], s[m] = s[m], s[z]
        n.append(tuple(s))
    return n

def solve(start):
    pq = []
    heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, cur, path = heappop(pq)
        if cur == GOAL_STATE:
            for p in path + [cur]:
                print(p)
            return
        if cur in visited:
            continue
        visited.add(cur)
        for nb in neighbors(cur):
            heappush(pq, (g+1+manhattan(nb), g+1, nb, path+[cur]))

start_state = (1,2,3,4,0,6,7,5,8)
solve(start_state)
