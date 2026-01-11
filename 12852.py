# https://star7sss.tistory.com/248
import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
result = [[] for _ in range(n+1)]

result[1] = [1]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    result[i] = result[i-1] + [i]
    
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        result[i] = result[i//2] + [i]
    
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1
        result[i] = result[i//3] + [i]

print(dp[n])
print(' '.join(map(str, result[n][::-1])))