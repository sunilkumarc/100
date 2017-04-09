# https://www.codingame.com/ide/puzzle/power-of-thor

lx, ly, tx, ty = [int(i) for i in input().split()]
while 1:
    if ty != ly:
        print('N', end='') if ty > ly else print('S', end='')
        ty = ty-1 if ty > ly else ty+1
    if tx != lx:
        print('W', end='') if tx > lx else print('E', end='')
        tx = tx-1 if tx > lx else tx+1
    print()
