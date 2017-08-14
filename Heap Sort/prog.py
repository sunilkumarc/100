def heapify(arr, i, heap_size):
    left = 2*i + 1
    right = 2*i + 2
    largest = i

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    elif right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heap_size)

def heapSort(arr, size):
    # 1. Build a max heap
    for i in range(int(size/2)-1, -1, -1):
        heapify(arr, i, size)

    # 2. Extract elements one by one
    for i in range(size-1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    print(arr)
    heapSort(arr, len(arr))
    print(arr)
