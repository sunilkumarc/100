# http://www.geeksforgeeks.org/given-a-sorted-and-rotated-array-find-if-there-is-a-pair-with-a-given-sum/

def findPivot(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    
    return -1

def findPair(arr, x):
    pivot = findPivot(arr)
    arrSize = len(arr)
    if pivot != -1:
        start = pivot + 1
        end = pivot
    else:
        start = 0
        end = len(arr) - 1

    while start != end:
            currentSum = arr[start] + arr[end]
            if currentSum == x:
                return [start, end]
            elif currentSum < x:
                start = (start + 1) % arrSize
            else:
                end = (arrSize + end - 1) % arrSize

    return None


if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    x = int(input().strip())

    print('Array : ', arr)
    print('Sum : ', x)
    result = findPair(arr, x)
    if result != None:
        print('Found a pair : ', arr[result[0]], arr[result[1]])
    else:
        print('No such pair found!')