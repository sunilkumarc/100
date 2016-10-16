arr = list(map(int, input().strip().split(' ')))
print('Before :', arr)

def partition(arr, low, high):
    i = low - 1
    j = low
    pivot = high
    while j < high:
        if arr[j] <= arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i+1], arr[pivot] = arr[pivot], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        print('Partitioned : ', arr)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)

if __name__ == '__main__':
    l = len(arr)
    quickSort(arr, 0, l-1)
    print('After : ', arr)
