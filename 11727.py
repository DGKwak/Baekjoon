from sys import stdin as st

n = int(st.readline())
mem = [0,1,3]

def cntSqu(n: int) -> int:
    for i in range(3,n+1):
        mem.append(mem[i-1]+(2*mem[i-2]))
    
    return mem[n]

print(cntSqu(n)%10007)