import sys
import heapq

n, c = map(int, sys.stdin.readline().split())

points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

def get_dist(a, b):
    return (points[a][0] - points[b][0]) ** 2 + (points[a][1] - points[b][1]) ** 2

visited = [0 for _ in range(n)]
min_dist = [float('inf') for _ in range(n)]
min_dist[0] = 0

q = [(0, 0)]
result = 0
cnt = 0

while q:
    d, curr = heapq.heappop(q)
    
    if visited[curr]:
        continue
    
    visited[curr] = 1
    result += d
    cnt += 1
    
    if cnt == n:
        break
    
    for next_node in range(n):
        if not visited[next_node]:
            dist = get_dist(curr, next_node)
            
            if dist >= c and dist < min_dist[next_node]:
                min_dist[next_node] = dist
                heapq.heappush(q, (dist, next_node))

if cnt == n:
    print(result)
else:
    print(-1)