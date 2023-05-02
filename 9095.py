from sys import stdin as st

T = int(st.readline())

mem = [1,2,4]+[0]*7

def sum123(n:int) -> int:
    if mem[n-1]: return mem[n-1]
    
    for i in range(3,n):
        if mem[i] == 0:
            mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    
    return mem[n-1]
    
for _ in range(T):
    n = int(st.readline())
    
    print(sum123(n))