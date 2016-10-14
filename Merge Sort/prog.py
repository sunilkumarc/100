arr = [1, 2, 0, 9, 4, 5, -1, 18, -3, 3]

def merge(arr, low, mid, high):
    temp1 = arr[low:mid+1]
    temp2 = arr[mid+1:high+1]
    i = 0
    j = 0
    k = low
    while (i < len(temp1) and j < len(temp2)):
        if temp1[i] < temp2[j]:
            arr[k] = temp1[i]
            i += 1
        else:
            arr[k] = temp2[j]
            j += 1
        k += 1

    while i < len(temp1):
        arr[k] = temp1[i]
        k += 1
        i += 1

    while j < len(temp2):
        arr[k] = temp2[j]
        k += 1
        j += 1

def mergeSort(arr, low, high):
    if low < high:
        mid = int(low + (high-low)/2)
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)

if __name__ == '__main__':
    print('Before: ', arr)
    low = 0
    high = len(arr) - 1
    mergeSort(arr, low, high)
    print('After:  ', arr)
