# To maximize profit using one transaction

def maxProfit(arr, N):
    min_price = arr[0]
    maxProfit = 0
    
    for i in range(1, N):
        if arr[i] < min_price:
            min_price = arr[i]

        maxProfit = max(maxProfit, arr[i] - min_price)
    
    return maxProfit

if __name__ == '__main__':
    arr = list(map(int, input().strip().split()))
    print(arr)
    res = maxProfit(arr, len(arr))
    print('Max Profit : ', res)