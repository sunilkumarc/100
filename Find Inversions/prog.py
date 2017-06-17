# arr = [1, 2, 0, 9, 4, 5, -1, 18, -3, 3]
arr = [4, 3, 2, 1]

no_of_inversions = 0

def merge(arr, low, mid, high):
    global no_of_inversions
    temp1 = arr[low:mid+1]
    temp2 = arr[mid+1:high+1]
    i = j = 0
    k = low
    while i < len(temp1) and j < len(temp2):
        if temp1[i] < temp2[j]:
            arr[k] = temp1[i]
            k += 1
            i += 1
        elif temp1[i] > temp2[j]:
            print('Comparing ', temp1[i], temp2[j])
            no_of_inversions += 1
            arr[k] = temp2[j]
            k += 1
            j += 1
        
    while i < len(temp1):
        arr[k] = temp1[i]
        i += 1
        k += 1
    
    while j < len(temp2):
        arr[k] = temp2[j]
        j += 1
        k += 1
    
def mergeSort(arr, start, end):
    if start < end:
        mid = int(start + (end-start)/2)
        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)
    
print(arr)
mergeSort(arr, 0, len(arr)-1)
print('No of inversions :', no_of_inversions)
