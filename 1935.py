import sys

N = int(sys.stdin.readline())
cal = sys.stdin.readline().strip()
var = []
stk = []

for i in range(N):
    var.append(int(sys.stdin.readline()))

def calculate(A: int, B:int, C:str) -> int:
    if C == '+': return A+B
    if C == '-': return A-B
    if C == '*': return A*B
    if C == '/': return A/B

for j in cal:
    if j.isalpha():
        stk.append(var[ord(j)-ord('A')])
    else:
        stk.append(calculate(stk.pop(-2),stk.pop(),j))
        
print('{:.2f}'.format(stk[-1]))