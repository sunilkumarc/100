def gcd(a, b): return a if b == 0 else gcd(b, a%b)
# def lcm(a, b): return a / gcd(a, b) * b
# 2 3 4 9 17

def findJ(arr, N):
    result = []
    store = dict()

    def exists(left, right):
        if str(arr[left])+'+'+str(arr[right]) in store:
            return True
        return False

    def getGcd(left, right):
        return store[str(arr[left])+'+'+str(arr[right])]

    def insert(left, right, res):
        store[str(arr[left])+'+'+str(arr[right])] = res

    for i in range(N):
        found = False
        left = i - 1
        right = i + 1
        js = []
        while found == False and left >= 0 and right < N:
            if exists(left, i):
                res = getGcd(left, i)
            else:
                res = gcd(arr[left], arr[i])
                insert(left, i, res)
            if res > 1:
                result.append(left+1)
                found = True

            if found == False:
                if exists(i, right):
                    res = getGcd(i, right)
                else:
                    res = gcd(arr[i], arr[right])
                    insert(i, right, res)
                if res > 1:
                    result.append(right+1)
                    found = True

            left -= 1
            right += 1

        while found == False and left >= 0:
            if exists(left, i):
                res = getGcd(left, i)
            else:
                res = gcd(arr[left], arr[i])
                insert(left, i, res)
            if res > 1:
                result.append(left+1)
                found = True
            left -= 1

        while found == False and right < N:
            if exists(i, right):
                res = getGcd(i, right)
            else:
                res = gcd(arr[i], arr[right])
                insert(i, right, res)
            if res > 1:
                result.append(right+1)
                found = True
            right += 1

        if found == False:
            result.append(-1)

    print(' '.join(map(str,result)))

if __name__ == '__main__':
    N = int(input().strip())
    arr = [int(elem) for elem in input().strip().split()]
    findJ(arr, N)
