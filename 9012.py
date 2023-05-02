import sys
        
N = int(sys.stdin.readline())

for i in range(N):
    line = sys.stdin.readline()
    VPS = []
    br = 0
    
    for j in line:
        if j == '(':
            VPS.append(j)
        elif j == ')':
            if VPS: VPS.pop()
            else:
                print('NO')
                br = 1
                break
    
    if br == 1:
        continue
    else:
        if not VPS:
            print('YES')
        else:
            print('NO')