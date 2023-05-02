import sys

while 1:
    S = sys.stdin.readline().strip()
    
    if len(S) == 0:
        break
    
    print(len(S))