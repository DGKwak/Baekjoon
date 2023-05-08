from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))

dp = [L[0]]+([0]*(n-1))

for i in range(1,n):
    dp[i] = max(L[i], dp[i-1]+L[i])
    
print(max(dp))