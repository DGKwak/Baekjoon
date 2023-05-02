from sys import stdin as st

n = int(st.readline())

mem = [1,1]

def cntFillSqu(n: int) -> int:    
    for i in range(2,n+1):        
        mem.append(mem[i-1]+mem[i-2])
        
    return mem[n]

print(cntFillSqu(n)%10007)