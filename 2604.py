import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

network = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

def bfs():
    q = deque([1])
    visited = [0] * (n+1)
    visited[1] = 1
    
    while q:
        