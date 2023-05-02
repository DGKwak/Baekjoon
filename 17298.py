import sys

N = int(sys.stdin.readline())
A = list(map(lambda i: int(i), sys.stdin.readline().split()))

stk = []
res = [-1]*N

for i in range(N):
    while stk and A[stk[-1]]<A[i]:
        res[stk.pop()] = A[i]    
    stk.append(i)

print(*res)