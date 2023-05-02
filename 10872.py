from sys import stdin

N = int(stdin.readline())

res = 1

if N > 0:
    for i in range(1, N+1):
        res = res * i
    
print(res)