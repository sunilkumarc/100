a = [3, 8, 0, 1, 9, 6, -7]

def insertionSort(arr, start, end):
    if end > 0:
        arr = insertionSort(arr, 0, end-1)
    
    key = arr[end]
    j = end-1
    while j >= 0 and arr[j] > key:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = key
    return arr

arr = insertionSort(a, 0, len(a)-1)
print(arr)