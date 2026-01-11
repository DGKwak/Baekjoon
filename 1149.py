from sys import stdin

N = int(stdin.readline())

HC = []

for _ in range(N):
    HC.append(list(map(int, stdin.readline().split())))

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = HC[0].copy()

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + HC[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + HC[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + HC[i][2]

print(min(dp[N-1]))