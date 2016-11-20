def gcd(a, b): return a if b == 0 else gcd(b, a%b)
# def lcm(a, b): return a / gcd(a, b) * b

def findJ(arr, N):
    result = []
    for i in range(N):
        found = False
        left = i - 1
        right = i + 1
        js = []
        while left >= 0 and right < N:
            js.append(left)
            js.append(right)
            left -= 1
            right += 1

        while left >= 0:
            js.append(left)
            left -= 1

        while right < N:
            js.append(right)
            right += 1

        for j in js:
            res = gcd(arr[i], arr[j])
            if res > 1:
                result.append(j+1)
                found = True
                break

        if found == False:
            result.append(-1)

    print(' '.join(map(str,result)))

if __name__ == '__main__':
    N = int(input().strip())
    arr = [int(elem) for elem in input().strip().split()]
    findJ(arr, N)
