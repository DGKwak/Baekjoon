import sys
        
N = int(sys.stdin.readline())
stack = []
result = []
cnt = 1
jud = True

for i in range(N):
    num = int(sys.stdin.readline())
    
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        jud = False
        break
    
if jud:
    for j in result:
        print(j)
else:
    print('NO')