# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

# This algorithm works only for array with postive integers
def findSubarray(a, S):
     currSum = 0
     startIndex = 0
     print(a)
     for i in range(len(a)):        
         currSum += a[i]
         # print('currSum : ', currSum)
         if currSum > S:
             while currSum > S and startIndex < i:
                 # print('Removing ', a[startIndex])
                 currSum -= a[startIndex]
                 startIndex += 1
         
         if currSum == S:
             return startIndex, i
     return -1, -1
    
if __name__ == '__main__':
    a = list(map(int, input().strip().split()))
    S = int(input().strip())
    print(findSubarray(a, S))