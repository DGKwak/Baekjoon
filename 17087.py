from sys import stdin

N, S = map(int, stdin.readline().split())
Bro = list(map(int, stdin.readline().split()))

def GCD(a: int, b: int) -> int:
    if a < b: a, b = b, a    
    if b == 0: return a
    
    while b != 0:
        a, b = b, a%b
        
    return a

def distance(S: int, L: list) -> int:
    tmp = []
    
    for i in L:
        tmp.append(abs(S-i))
    
    curGCD = 0
    
    for j in tmp:
        curGCD = GCD(j, curGCD)
    
    return curGCD

print(distance(S, Bro))