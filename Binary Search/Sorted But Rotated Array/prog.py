# arr = [3, 4, 5, 6, 7, 8, 1, 2]
arr = [ 101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100 ]
# arr = [ 1, 7, 67, 133, 178 ]

'''
Algorith is like below:
=======================

Divide array by a mid point just like in original binary search
if key is present in arr[mid]
    return mid
if left subarray is sorted:
    if key is in range of first subarray, search in first subarray
    else search in second subarray
else the second subarray has to be sorted
    if key is range of second subarray, search in second subarray
    else search in first subarray
'''
def searchElem(arr, target, start, end):
    if start > end:
        return -1
    
    mid = int((start+end)/2)
    
    if arr[mid] == target:
        return mid
    
    if arr[start] <= arr[mid]:
        if target >= arr[start] and target <= arr[mid]:
            return searchElem(arr, target, start, mid-1)
        return searchElem(arr, target, mid+1, end)
    else:
        if target >= arr[mid] and target <= arr[end]:
            return searchElem(arr, target, mid+1, end)
        return searchElem(arr, target, start, mid-1)
        
def binarySearch(nums, target):
    return searchElem(nums, target, 0, len(nums)-1)

if __name__ == '__main__':
    print(arr)
    target = int(input('Enter key to search : ').strip())
    index = binarySearch(arr, target)
    if index == -1:
        print('Key not present in the array')
    else:
        print('Found at : ', index)