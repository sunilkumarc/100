# Rearragen all the numbers in an array such that all positive numbers
# appear first and all negative numbers appear next

def rearrange(arr, N):
    start = 0
    while start < N:
        if arr[start] < 0:
            search = start + 1
            while search < N and arr[search] < 0:
                search += 1
            if search < N:
                arr[start], arr[search] = arr[search], arr[start]
        
        start += 1

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    print(arr)
    rearrange(arr, len(arr))
    print(arr)