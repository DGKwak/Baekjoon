import sys
from collections import deque

N = int(sys.stdin.readline().strip())

r_map = []
for _ in range(N):
    r_map.append(list(map(int, sys.stdin.readline().split())))

if sum(row.count(r_map[0][0]) for row in r_map) == N * N:
    print(1)
    sys.exit(0)

max_height = max(map(max, r_map))

def bfs(x, y, height, visited):
    q = deque([(x, y)])
    visited[x][y] = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        curr_x, curr_y = q.popleft()
        
        for dx, dy in directions:
            nx, ny = curr_x + dx, curr_y + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and r_map[nx][ny] > height:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

result = 0
for height in range(1, max_height + 1):
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if r_map[i][j] > height and visited[i][j] == 0:
                bfs(i, j, height, visited)
                cnt += 1

    result = max(result, cnt)

print(result)