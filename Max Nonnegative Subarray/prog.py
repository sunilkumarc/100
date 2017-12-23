def maxset(A):
    globalSum = 0
    localSum = 0
    i = 0
    N = len(A)
    
    while i < N and A[i] < 0:
        i += 1
        
    startIndex = i
    
    localSum = A[startIndex]
    resultSize = 0
    result = []
    res = [A[startIndex]]
    
    for i in range(startIndex+1, N):
        if A[i] >= 0:
            localSum += A[i]
            res.append(A[i])
        else:
            if globalSum < localSum:
                globalSum = localSum
                resultSize = i - startIndex
                result = res
                
            elif globalSum == localSum:
                if resultSize < (i - startIndex):
                    result = res
                    resultSize = i - startIndex
            
            while i < N and A[i] < 0:
                i += 1
            
            startIndex = i
            localSum = 0
            res = []
    
    if globalSum < localSum:
        result = res
        
    return result
	        
print(maxset([ -1, 2, -1, 1 ]))
	        
	        
	        