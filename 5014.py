import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
elevator = [-1 for _ in range(F)]

def bfs(x):
    q = deque([x])
    elevator[x-1] = 0
    
    while q:
        curr = q.popleft() - 1
        
        for dx in [U, -D]:
            nx = curr + dx
            
            if 0 <= nx < F:
                if elevator[nx] == -1:
                    elevator[nx] = elevator[curr] + 1
                    q.append(nx + 1)

bfs(S)

if elevator[G-1] == -1:
    print("use the stairs")
else:
    print(elevator[G-1])