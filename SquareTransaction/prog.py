from bisect import bisect_left

# modified binary search
'''
binary_search(arr, elem, low = 0, high = None):
    if low > high:
        return -1
    mid = low + (mid-low)/2
    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        binary_search(arr, elem, low, mid-1)
    else:
        binary_search(arr, elem, mid+1, high)
5
1 2 1 3 4
3
4
2
10

1 3 4 7 11
'''

'''
def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return (pos if pos != hi and a[pos] == x else -1)
'''
def binary_search(arr, elem, low, high):
    if low > high:
        return -1

    if low == high:
        if arr[low] != elem:
            return low+1

    mid = int(low + (high-low)/2)
    print(low, high, mid)

    if arr[mid] == elem:
        return mid
    elif arr[mid] > elem:
        return binary_search(arr, elem, low, mid-1)
    else:
        return binary_search(arr, elem, mid+1, high)

a = [1, 4, 5, 7, 8]
print(binary_search(a, 6, 0, len(a)-1))

'''
T = int(input())
trans = [int(x) for x in input().strip().split(" ")]

sums = []
prev_sum = 0
for i in trans:
    prev_sum += i
    sums.append(prev_sum)

Q = int(input())

def findMaxTrans(target):
    length = len(trans)
    for i in range(0, length):
        if sums[i] >= target:
            return i+1
    return -1

for _ in range(Q):
    target = int(input())
    print(binary_search(sums, target)+1)
'''
