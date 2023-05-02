import sys

S = sys.stdin.readline().strip()
res = [-1]*26

for i in range(len(S)):
    if res[ord(S[i])-ord('a')] == -1:
        res[ord(S[i])-ord('a')] = i
    
print(' '.join(map(str,res)))