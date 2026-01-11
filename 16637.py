# https://kimhaemin.tistory.com/entry/%EB%B0%B1%EC%A4%80-16637-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B4%84%ED%98%B8-%EC%B6%94%EA%B0%80%ED%95%98
import sys

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
def dfs(idx, curr_val):
    global max_value
    
    if idx == n:
        max_value = max(max_value, curr_val)
        return
    
    # 괄호 없는 경우
    next_val = calculate(curr_val, eq[idx+1], eq[idx])
    dfs(idx+2, next_val)
    
    # 괄호가 있는 경우
    if idx+4 <= n:
        bracket_val = calculate(eq[idx+1], eq[idx+3], eq[idx+2])
        next_val = calculate(curr_val, bracket_val, eq[idx])
        dfs(idx+4, next_val)

n = int(sys.stdin.readline())
eq = [int(x) if x != '+' and x != '-' and x != '*' else x for x in sys.stdin.readline().strip()]
max_value = -2**31

dfs(1, eq[0])
print(max_value)