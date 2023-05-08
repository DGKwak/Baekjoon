from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(max(dp))