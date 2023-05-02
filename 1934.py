import sys

N = int(sys.stdin.readline())

def LCM(x: int, y: int) -> int:
    tmp1, tmp2 = x, y
    
    while tmp2:
        tmp1, tmp2 = tmp2, tmp1%tmp2
        
    return int(x*y/tmp1)

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    
    print(LCM(A,B))