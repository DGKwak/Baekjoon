import sys

L = [True]*1000001
L[0], L[1] = False, False

for i in range(2, 1001):
    if L[i]:
        for  j in range(i*2, 1000001, i):
            L[j] = False

while 1:
    N = int(sys.stdin.readline())
    
    if N == 0: break
    
    GB = 1
    
    for k in range(3, N, 2):
        if L[k] and L[N-k]:
            print(f'{N} = {k} + {N-k}')
            GB = 0
            break
        
    if GB:
        print("Goldbach's conjecture is wrong.")