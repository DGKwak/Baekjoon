import sys

S = sys.stdin.readline().strip()
res = [0]*26

for i in S:
    res[ord(i)-ord('a')] += 1
    
print(' '.join(map(str,res)))