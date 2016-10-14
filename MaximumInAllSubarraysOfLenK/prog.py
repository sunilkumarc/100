'''
Problem : http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/
'''

# a = [4, 1, 0, 6, 7, 8, 12, 24, 19, 16, 3, 5, 1, 13]
a = [int(item) for item in input().strip().split(' ')]

def printSubArrays(K):
    arrLen = len(a)
    i = 0
    while i <= arrLen-K:
        subArr = a[i:(i+K)]
        print(max(subArr))
        i += 1

if __name__ == '__main__':
    print(a)
    K = int(input('Enter K : '))
    printSubArrays(K)
