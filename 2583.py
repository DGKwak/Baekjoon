from collections import deque
import sys

m, n, k = map(int, sys.stdin.readline().split())

dist_map = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    start_x, start_y, end_x, end_y = map(int, sys.stdin.readline().split())
    
    for i in range(start_y, end_y):
        for j in range(start_x, end_x):
            dist_map[i][j] = '#'

def bfs(x, y):
    q = deque([(y, x)])
    dist_map[y][x] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cnt = 1
    while q:
        curr_y, curr_x = q.popleft()

        for i in range(4):
            ny = curr_y + dy[i]
            nx = curr_x + dx[i]

            if 0 <= ny < m and 0 <= nx < n:
                if dist_map[ny][nx] == 0:
                    dist_map[ny][nx] = 1
                    q.append((ny, nx))
                    cnt += 1

    return cnt

areas = []
for y in range(m):
    for x in range(n):
        if dist_map[y][x] == 0:
            areas.append(bfs(x, y))

print(len(areas))
print(*sorted(areas))