import sys

N = list(sys.stdin.readline().strip())

res = 0
rebar = []

for i in range(len(N)):
    if N[i] == '(':
        rebar.append(N[i])
    
    if N[i] == ')' and N[i-1] == '(':
        rebar.pop()
        res += len(rebar)
        continue
        
    if N[i] == ')':
        rebar.pop()
        res += 1
        
print(res)