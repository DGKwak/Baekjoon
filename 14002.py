from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

cnt = max(dp)
print(cnt)

res = []
for j in range(N-1, -1, -1):
    if dp[j] == cnt:
        res.append(A[j])
        cnt -= 1
        
res.reverse()
for k in res:
    print(k, end=' ')