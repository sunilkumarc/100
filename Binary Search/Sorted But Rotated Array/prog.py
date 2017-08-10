arr = [3, 4, 5, 6, 7, 8, 1, 2]

'''
Algorith is like below:
=======================

Divide array by a mid point just like in original binary search
if key is present in arr[mid]
    return mid
else if array is either (greater than both a[start] and a[mid+1]) or (lesser than both a[start] and a[mid+1])
    then search in array starting with bigger element
else element is greater than first element of either of the sub arrays
    search element in the array with smaller starting element

'''
def binarySearch(arr, key, start, end):
    if start > end:
        return -1

    mid = int((start + end) / 2)
    if arr[mid] == key:
        return mid

    elif (key > arr[start] and key > arr[mid+1]) or (key < arr[start] and key < arr[mid+1]):
        if arr[start] > arr[mid+1]:
            return binarySearch(arr, key, start, mid-1)
        else:
            return binarySearch(arr, key, mid+1, end)
    elif arr[start] < arr[mid+1]:
        return binarySearch(arr, key, start, mid-1)
    elif arr[mid+1] < arr[start]:
        return binarySearch(arr, key, mid+1, end)

if __name__ == '__main__':
    print(arr)
    key = int(input('Enter key to search : ').strip())
    index = binarySearch(arr, key, 0, len(arr)-1)
    if index == -1:
        print('Key not present in the array')
    else:
        print('Found at : ', index)