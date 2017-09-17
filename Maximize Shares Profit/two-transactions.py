# http://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/
'''
A detailed description for the above code as some parts have not been explained.
After the first for loop, the initial profit array consists of the profit that 
can be obtained by a single buy and a single sell from i to n-1.
The second for loop( understanding this is important):
In the code profit[i] on the left hand side is the max profit given the first selling 
is made on a day <= i. So now profit[i] can either be when the first sell was made earlier, 
i.e on a day < i which is stored in profit[i-1] or when the first sell was made on day i, 
so when the first sell is made on day i then the maximum profit that can be made from this 
first sell is by maintaining a variable min_ which stores the minimum value of element 
encountered so far, so the buy value is now min_ the sell value being price[i]. So since 
the first sell has already been made, now we can start our buying and selling process once 
again starting from the same day i(buy and sell on same day is possible). So now the 
maximum profit from the second sell is already pre-computed in the same array profit which 
has not yet been updated for indices >=i . So the profit from sell 1 and sell 2 in this 
case would be , profit[i] + price[i] - min_.So now we should consider the maximum of the 
above computed profits arising from the two different cases for each index and return profit[n].
Cheers :)
'''

def findMaxProfit(arr, N):
    profit = [0] * N
    
    maxPrice = arr[N-1]
    for i in range(N-2, -1, -1):
        if arr[i] > maxPrice:
            maxPrice = arr[i]
        
        profit[i] = max(profit[i+1], maxPrice-arr[i])
    
    minPrice = arr[0]
    for i in range(1, N):
        if arr[i] < minPrice:
            minPrice = arr[i]
        
        profit[i] = max(profit[i-1], profit[i] + (arr[i]-minPrice))

    return profit[N-1]

if __name__ == '__main__':
    T = int(input().strip())
    
    for _ in range(T):
        arr = list(map(int, input().strip().split()))
        print(arr)
        profit = findMaxProfit(arr, len(arr))
        print('Maximum profit with 2 transactions : ', profit, '\n')
    

