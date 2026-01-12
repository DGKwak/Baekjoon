import sys
from collections import deque

n = int(sys.stdin.readline())

a_map = []
for _ in range(n):
    tmp = list(map(int, list(sys.stdin.readline().strip())))
    a_map.append([-1 if x == 0 else 0 for x in tmp])

def bfs(x, y, dist):
    q = deque([(x, y)])
    a_map[y][x] += dist
    
    cnt = 1
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in move:
            nx = curr_x + dx
            ny = curr_y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                if a_map[ny][nx] == 0:
                    a_map[ny][nx] += dist
                    q.append((nx, ny))
                    cnt += 1

    return cnt

result = []
dist = 1
for y in range(n):
    for x in range(n):
        if a_map[y][x] == 0:
            result.append(bfs(x, y, dist))
            dist += 1

print(len(result))
print(*sorted(result))