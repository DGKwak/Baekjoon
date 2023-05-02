import sys

N = int(sys.stdin.readline())
deq = []

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push_front':
        deq.insert(0, order[1])
    
    if order[0] == 'push_back':
        deq.append(order[1])
        
    if order[0] == 'pop_front':
        if deq: print(deq.pop(0))
        else: print(-1)
    
    if order[0] == 'pop_back':
        if deq: print(deq.pop())
        else: print(-1)
        
    if order[0] == 'size':
       print(len(deq)) 
        
    if order[0] == 'empty':
       if deq: print(0)
       else: print(1)
        
    if order[0] == 'front':
       if deq: print(deq[0])
       else: print(-1)
        
    if order[0] == 'back':
        if deq: print(deq[-1])
        else: print(-1)