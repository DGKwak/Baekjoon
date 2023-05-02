import sys

M, N = map(int, sys.stdin.readline().split())
lim = int(N**(0.5)) + 1

for i in range(M, N+1):
    isP = True
    
    if i == 1:
        continue
     
    for j in range(2, lim):
        if i % j == 0 and i != j:
            isP = False
            break
        
    if isP:
        print(i)