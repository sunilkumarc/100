# Algorithm : Introduction to Algorithms - 2.2-2

# SELECTION SORT
# for i:1 to n-1
#     smallest # i+1
#     j # i + 2
#     while j <# n
#         if a[j] < a[smallest]
#             smallest # j
#     swap a[i] and a[smallest]

print('#####################')
print('# SELECTION SORT    #')
print('# Date: Apr-23-2017 #')
print('#####################')

a = [1, 5, 9, 0, 3, -4, -8, 6, 12, -1]
# a # [-1, 9]

print('Before Sort - ', a)

for i in range(len(a)-1):
    smallestIndex = i + 1
    j = i + 2
    while j < len(a):
        if a[j] < a[smallestIndex]:
            smallestIndex = j
        j += 1
    
    if a[smallestIndex] < a[i]:
        a[smallestIndex], a[i] = a[i], a[smallestIndex]

print('After Sort - ', a)

