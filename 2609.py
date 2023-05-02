import sys

A, B = map(int, sys.stdin.readline().split())

def GCD(x: int, y: int) -> int: 
    while y:
        x, y = y, x%y
    
    return x
    
def LCM(x: int, y: int, r: int) -> int:
    return int(x*y/r)
R = GCD(A,B)
print(R)
print(LCM(A,B,R))