from sys import stdin

N = int(stdin.readline())
L = [[0]*10]*101

L[1] = [0]+[1]*9

mod = 1000000000

if N > 1:
    for i in range(2,N+1):
        tmp = [0]*10
        
        for j in range(10):
            if j == 0:
                tmp[0] = L[i-1][1]%mod
            
            if j <= 8 and j >= 1:
                tmp[j] = L[i-1][j-1]%mod + L[i-1][j+1]%mod
                
            if j == 9:
                tmp[9] = L[i-1][8]%mod
        
        L[i] = tmp

print(sum(L[N])%mod)