a = [4, 9, 0, 1, 5, 2]
l = len(a)
print('BUBBLE SORT\n')
print('Before: ', a)
for i in range(0, l-1):
    for j in range(0, l-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print('Inside Loop:', a)

print('After: ', a)
