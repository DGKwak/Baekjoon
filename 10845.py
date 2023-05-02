import sys

N = int(sys.stdin.readline())
q = []
size = 0

for _ in range(N):
    order = sys.stdin.readline().split()
    
    if order[0] == 'push':
        q.append(order[1])
        size += 1
    if order[0] == 'pop':
        if size != 0:
            print(q.pop(0))
            size -= 1
        else:
            print(-1)
    if order[0] == 'size':
        print(size)
    if order[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)
    if order[0] == 'front':
        if size != 0:
            print(q[0])
        else:
            print(-1)
    if order[0] == 'back':
        if size != 0:
            print(q[-1])
        else:
            print(-1)