from collections import deque

m, n, k = map(int, input().split())

graph = []
q = deque()
for h in range(k):
    layer = []
    
    for i in range(n):
        tmp = list(map(int, input().split()))
        
        for j in range(m):
            if tmp[j] == 1:
                q.append([h, i, j])

        layer.append(tmp)
    
    graph.append(layer)

def bfs():    
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    
    while q:
        z, x, y = q.popleft()
        
        for i in zip(dz, dx, dy):
            nz = z + i[0]
            nx = x + i[1]
            ny = y + i[2]
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < k:
                if graph[nz][nx][ny] == 0:
                    q.append([nz, nx, ny])
                    graph[nz][nx][ny] = graph[z][x][y] + 1

bfs()
result = 0

for layer in graph:
    for row in layer:
        for value in row:
            if value == 0:
                print(-1)
                exit(0)

            result = max(result, value)

print(result - 1)