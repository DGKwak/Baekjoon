from sys import stdin

T = int(stdin.readline())

mem = [[0]*3]*100001
mem[1] = [1,0,0]
mem[2] = [0,1,0]
mem[3] = [1,1,1]

for i in range(4,100001):
    tmp0 = mem[i-1][1]%1000000009 + mem[i-1][2]%1000000009
    tmp1 = mem[i-2][0]%1000000009 + mem[i-2][2]%1000000009
    tmp2 = mem[i-3][0]%1000000009 + mem[i-3][1]%1000000009
    
    mem[i] = [tmp0, tmp1, tmp2]

for _ in range(T):
    n = int(stdin.readline())

    print(sum(mem[n])%1000000009)