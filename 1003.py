import sys

cnt = [0, 0]

dp = [[] for _ in range(41)]
dp[0], dp[1] = [1, 0], [0, 1]

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    
    if dp[n]:
        print(f"{dp[n][0]} {dp[n][1]}")
        continue
    
    for i in range(2, n+1):
        dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
    
    print(f"{dp[n][0]} {dp[n][1]}")