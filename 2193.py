from sys import stdin

N = int(stdin.readline())

pn = [[0,0], [0,1], [1,0], [1,1]]+[[0,0]]*87

def cntPN(N: int) -> int:
    if N >= 4:
        for i in range(4,N+1):
            tmp = [0,0]
            
            tmp[0] = pn[i-1][0] + pn[i-1][1]
            tmp[1] = pn[i-1][0]
            
            pn[i] = tmp
    
    return sum(pn[N])

print(cntPN(N))