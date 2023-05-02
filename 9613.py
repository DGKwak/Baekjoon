from sys import stdin

n = int(stdin.readline())

def gcd(a: int, b: int) -> int:
    if a < b: a, b = b, a    
    if b == 0: return a
    
    while b != 0:
        a, b = b, a%b
        
    return a

for _ in range(n):
    L = list(map(int, stdin.readline().split()))
    
    res = 0
    l = L.pop(0)
    
    for i in range(l-1):
        for j in range(i+1, l):
            res += gcd(L[i], L[j])
            
    print(res)