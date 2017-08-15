# Algorithm:
# First build max heap in time complexity of n
# Then extract K numbers from this heap while heapifying after each retrival

def buildMaxHeap(arr, index, heap_size):
    left = 2*index + 1
    right = 2*index + 2

    largest = index
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if index != largest:
        arr[index], arr[largest] = arr[largest], arr[index]
        buildMaxHeap(arr, largest, heap_size)

if __name__ == '__main__' :
    arr = list(map(int, input().strip().split()))
    K = int(input().strip())

    # Build a max heap
    size = len(arr)
    if size >= K:
        print(arr)
        for i in range(int(size/2 - 1), -1 ,-1):
            buildMaxHeap(arr, i, size)

        for i in range(size-1, size-(K+1), -1):
            arr[i], arr[0] = arr[0], arr[i]
            buildMaxHeap(arr, 0, i)

        print(K, 'largest elements are : ', arr[size-K:])
    else:
        print('K cannot be bigger than array size!')
