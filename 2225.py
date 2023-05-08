from sys import stdin

N, K = map(int, stdin.readline().split())

dp = [[1]*(N+1) for _ in range(K)]

for i in range(1, K):
    for j in range(1, N+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
    
print(dp[-1][-1])