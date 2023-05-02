import sys

num = sys.stdin.readline().split()

num.append(num[0]+num[1])
num.append(num[2]+num[3])

print(int(num.pop())+int(num.pop()))