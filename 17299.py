import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(lambda i: int(i), sys.stdin.readline().split()))

c = dict(Counter(A))

stk = []
res = [-1]*N

for i in range(N):
    while stk and c[A[stk[-1]]]<c[A[i]]:
        res[stk.pop()] = A[i]
    stk.append(i)
    
print(*res)