import sys
        
N = int(sys.stdin.readline())

for i in range(N):
    line = sys.stdin.readline().split()
    s = ''
        
    for j in line:
        for k in range(len(j)-1,-1,-1):
            s += j[k]
        s += ' '
    
    print(s)