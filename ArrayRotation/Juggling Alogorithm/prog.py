# http://www.geeksforgeeks.org/array-rotation/
# https://www.youtube.com/watch?v=utE_1ppU5DY&t=295s
# https://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def rotateArray(arr, N, K):
    sets = gcd(N, K)
    for i in range(sets):
        temp = arr[i]
        j = i
        while True:
            # d = (j + K) % N
            # below statements are preferred than % in above statement since 
            # + and then - operations are cheaper.
            d = j + K
            if d >= N:
                d = d - N

            if d == i:
                break
            arr[j] = arr[d]
            j = d
        arr[j] = temp

if __name__ == '__main__':
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    K = int(input().strip())

    print('======================')
    print('Juggling Agorithm')
    print('======================')
    print('Before : ', arr)
    rotateArray(arr, N, K)
    print('After : ', arr)


