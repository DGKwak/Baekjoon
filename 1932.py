import sys

n = int(sys.stdin.readline())

triangle = []
result = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    
    triangle.append(tmp)
    result.append([0] * len(tmp))

result[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            result[i][j] = result[i-1][j] + triangle[i][j]
        elif j == len(triangle[i]) - 1:
            result[i][j] = result[i-1][j-1] + triangle[i][j]
        else:
            result[i][j] = max(result[i-1][j-1] + triangle[i][j], result[i-1][j] + triangle[i][j])

print(max(result[n-1]))