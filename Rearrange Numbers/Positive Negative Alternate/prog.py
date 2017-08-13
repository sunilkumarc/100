# Rearrange the given array such than positive numbers and negative
# numbers appear alternatively

def rearrange(arr, N):
    flag = 1
    start = 0
    while start < N:
        if flag == 1:
            if arr[start] < 0:
                search = start + 1
                while search < N and arr[search] < 0:
                    search += 1   
                if search < N:
                    arr[start], arr[search] = arr[search], arr[start]
            flag *= -1
        else:
            if arr[start] >= 0:
                search = start + 1
                while search < N and arr[search] >= 0:
                    search += 1
                if search < N:
                    arr[start], arr[search] = arr[search], arr[start]
            flag *= -1
        
        start += 1

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))

    print(arr)
    rearrange(arr, len(arr))
    print(arr)
