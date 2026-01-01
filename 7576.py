from collections import deque

m, n = map(int, input().split())

farm = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if farm[i][j] == 1:
            queue.append([i, j])

def bfs(q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if farm[nx][ny]==0:
                    q.append([nx, ny])
                    farm[nx][ny] = farm[x][y] + 1

bfs(queue)

result = 0

for N in farm:
    for M in N:
        if M == 0:
            print(-1)
            exit(0)
        result = max(result, M)

print(result - 1)