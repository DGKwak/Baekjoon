import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
res = []

for i in L:
    cnt = 0
    if i < 2: continue
    
    for j in range(2,i):
        if i % j == 0: cnt += 1
    
    if cnt == 0:
        res.append(i)    
            
print(len(res))