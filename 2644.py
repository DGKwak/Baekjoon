# https://wonyoung2257.tistory.com/56
import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = []

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, num):
    num += 1
    visited[v] = 1
    
    if v == b:
        result.append(num)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)