from sys import stdin

n, m = map(int, stdin.readline().split())

def count2(n: int) -> int:
    if n < 2: return 0
    
    cnt = 0
    while n >= 2:
        n //= 2
        cnt += n
        
    return cnt

def count5(n: int) -> int:
    if n < 5: return 0
    
    cnt = 0
    while n >= 5:
        n //= 5
        cnt += n
        
    return cnt

cnt2 = count2(n) - count2(m) - count2(n-m)
cnt5 = count5(n) - count5(m) - count5(n-m)
    
print(min(cnt2, cnt5))