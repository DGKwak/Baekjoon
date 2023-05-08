from sys import stdin

T = int(stdin.readline())

dp = [0,1,2,4]+[0]*999998

mod = 1000000009

for i in range(4,1000001):
    dp[i] = dp[i-1]%mod + dp[i-2]%mod + dp[i-3]%mod

for _ in range(T):
    n = int(stdin.readline())
    
    print(dp[n]%mod)