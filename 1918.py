import sys

N = sys.stdin.readline().strip()

stk = []
oper = []
prior = {'(':3, '*':2, '/':2, '+':1, '-':1}

for i in N:
    if i == '(':
        stk.append(i)
        continue
    
    if i == ')':
        while stk and stk[-1] != '(':
            oper.append(stk.pop())
        stk.pop()
        continue
        
    if i == '*' or i == '/' or i == '+' or i == '-':
        while stk and prior[i] <= prior[stk[-1]] and stk[-1] != '(':
            oper.append(stk.pop())
        stk.append(i)
        continue
    
    oper.append(i)
    
while stk:
    oper.append(stk.pop())
    
print(''.join(oper))