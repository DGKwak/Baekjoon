import sys

num, jose = map(int, sys.stdin.readline().split())

cnt = 0

tmp = list(map(lambda i: i, range(1,num+1)))
result = []

for _ in range(num):
    cnt += jose - 1
    if cnt >= len(tmp): cnt %= len(tmp)
    
    result.append(str(tmp.pop(cnt)))

print('<'+', '.join(result)+'>')