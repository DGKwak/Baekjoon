x, y = map(int, input().split())
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = y

if x != 1:
    for i in range(x-1):
        d += date[i]

if d % 7 == 1:
    print('MON')

if d % 7 == 2:
    print('TUE')
    
if d % 7 == 3:
    print('WED')
    
if d % 7 == 4:
    print('THU')
    
if d % 7 == 5:
    print('FRI')
    
if d % 7 == 6:
    print('SAT')
   
if d % 7 == 0:
    print('SUN')