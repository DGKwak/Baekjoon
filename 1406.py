import sys

strL = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline())
strR = []

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L' and strL:
        strR.append(strL.pop())
    if order[0] == 'D' and strR:
        strL.append(strR.pop())
    if order[0] == 'B' and strL:
        strL.pop()
    if order[0] == 'P':
        strL.append(order[1])
        
print(''.join(strL+list(reversed(strR))))