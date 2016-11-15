def nextSmallestPalindrome(n):
    arr = [int(i) for i in str(n)]
    size = len(arr)
    left = int(size/2)-1
    right = int(size/2) if (size % 2 == 0) else int(size/2)+1
    hasChangedLeft = False
    hasChangedRight = False

    while left >= 0:
        if arr[left] != arr[right]:
            if arr[right] < arr[left]:
                arr[right] = arr[left]
                hasChangedRight = True
            else:
                if hasChangedLeft == True:
                    arr[right] = arr[left]
                else:
                    arr[left] += 1
                    arr[right] = arr[left]
                    hasChangedLeft = True
        left -= 1
        right += 1

    mid = int((left+right)/2)
    if hasChangedLeft == False and hasChangedRight == False:
        arr[mid] += 1
    elif hasChangedLeft == True and hasChangedRight == True:
        if min % 2 == 0:
            arr[mid] = 0
    arr = map(str, arr)
    return ''.join(arr)

if __name__=='__main__':
    T = int(input().strip())
    for _ in range(T):
        N = int(input())
        print(nextSmallestPalindrome(N))
