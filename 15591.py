# https://steadily-worked.tistory.com/877
# https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-15591%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-MooTubeSilver
import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().split())
U_graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, USADO = map(int, sys.stdin.readline().split())
    U_graph[a].append((b, USADO))
    U_graph[b].append((a, USADO))

def bfs(k, v):
    visited = [0 for _ in range(N+1)]
    visited[v] = 1
    q = deque([(v, float('inf'))])
    result = 0
    
    while q:
        v, USADO = q.popleft()
        
        for next_v, next_USADO in U_graph[v]:
            next_USADO = min(USADO, next_USADO)
            
            if not visited[next_v] and next_USADO >= k:
                visited[next_v] = 1
                result += 1
                q.append((next_v, next_USADO))
    
    return result

for _ in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(bfs(k, v))