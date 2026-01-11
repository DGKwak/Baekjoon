import sys

n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

tmp = 0
sum_list = [0]
for i in num_list:
    tmp += i
    sum_list.append(tmp)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    
    print(sum_list[j] - sum_list[i-1])