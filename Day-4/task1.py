import math

def is_prime(x):
    if x < 2: return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def ulam_spiral(n):
    grid = [[0]*n for _ in range(n)]
    x, y = 0, 0
    dx, dy = 0, 1  # start moving right (we'll rotate)
    # to create spiral we will fill from center outward
    cx = cy = n//2
    x, y = cx, cy
    num = 1
    steps = 1
    grid[x][y] = num
    num += 1
    while num <= n*n:
        # move right steps, up steps, left steps, down steps, with steps increment
        for _ in range(2):
            for _ in range(steps):
                if num > n*n: break
                y += dy; x += dx
                # rotate direction (right->up->left->down->right ...)
                grid[x][y] = num
                num += 1
                # rotate direction
                dx, dy = dy, -dx
            # after inner loop keep going
        steps += 1
    # Build visual: replace primes with '*'
    out = []
    for row in grid:
        line = ""
        for val in row:
            line += "*" if is_prime(val) else "."
        out.append(line)
    return out

# Example (odd n)
for line in ulam_spiral(11):
    print(line)
