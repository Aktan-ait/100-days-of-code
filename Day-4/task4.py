import heapq

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    def heuristic(a,b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    open_heap = []
    heapq.heappush(open_heap, (0 + heuristic(start, goal), 0, start, None))
    came_from = {}
    gscore = {start: 0}
    closed = set()
    while open_heap:
        f, g, current, parent = heapq.heappop(open_heap)
        if current in closed:
            continue
        came_from[current] = parent
        if current == goal:
            # reconstruct path
            path = []
            cur = current
            while cur:
                path.append(cur)
                cur = came_from[cur]
            return path[::-1]
        closed.add(current)
        r,c = current
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            nbr = (nr,nc)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = g + 1
                if tentative_g < gscore.get(nbr, float('inf')):
                    gscore[nbr] = tentative_g
                    heapq.heappush(open_heap, (tentative_g + heuristic(nbr, goal), tentative_g, nbr, current))
    return None

# Example
grid = [
 [0,0,0,0,0],
 [1,1,0,1,0],
 [0,0,0,1,0],
 [0,1,0,0,0],
 [0,0,0,1,0]
]
print(astar(grid, (0,0), (4,4)))
