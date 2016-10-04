n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
length = len(arr)

for i in range(0, int(length/2)):
    arr[i], arr[length-i-1] = arr[length-i-1], arr[i]

print(' '.join(map(str,arr)))
