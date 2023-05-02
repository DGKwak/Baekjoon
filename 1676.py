from sys import stdin

N = int(stdin.readline())

fac = 1
res = 0

if N > 0:
    for i in range(1, N+1):
        fac = fac * i

fac = str(fac)

for k in fac[::-1]:
    if k != '0':
        break
    
    res += 1
    
print(res)