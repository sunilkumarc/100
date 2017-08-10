# http://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArray(arr, N, K):
    reverse(arr, 0, K-1)
    reverse(arr, K, N-1)
    reverse(arr, 0, N-1)

if __name__ == '__main__':
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    K = int(input().strip())

    print('======================')
    print('Reversal Agorithm')
    print('======================')
    print('Before : ', arr)
    rotateArray(arr, N, K)
    print('After : ', arr)


