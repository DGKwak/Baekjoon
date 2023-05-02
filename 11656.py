import sys

S = sys.stdin.readline().strip('\n')
suf = []

for i in range(len(S)):
    suf.append(S[i:])
    
suf.sort()

while suf:
    print(suf.pop(0))