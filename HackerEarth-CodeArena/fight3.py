'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/roy-and-leds-6/

def setLedState(n, L):
    state = [0] * L
    off = 1
    i = 0
    while i < L:
        if off == 1:
            i += n
            off = 0
        else:
            j = 0
            while i < L and j < n:
                state[i] = 1
                j += 1
                i += 1
            off = 1
            
    return state

def getColor(r, g, b):
    if r == 1 and g == 0 and b == 0:
        return 1
    elif r == 0 and g == 1 and b == 0:
        return 2
    elif r == 0 and g == 0 and b == 1:
        return 3
    elif r == 1 and g == 1 and b == 0:
        return 4
    elif r == 0 and g == 1 and b == 1:
        return 5
    elif r == 1 and g == 0 and b == 1:
        return 6
    elif r == 1 and g == 1 and b == 1:
        return 7
    elif r == 0 and g == 0 and b == 0:
        return 8

if __name__ == '__main__':
    T, R, G, B = map(int, input().strip().split())
    
    red = setLedState(R, T)
    green = setLedState(G, T)
    blue = setLedState(B, T)
    
    finalColors = dict()
    for i in range(T):
        res = getColor(red[i], green[i], blue[i])
        if res in finalColors:
            finalColors[res] += 1
        else:
            finalColors[res] = 1
    
    result = []
    n = 8
    for i in range(n):
        if i+1 in finalColors:
            result.append(str(finalColors[i+1]))
        else:
            result.append('0')
        
    print(' '.join(result))
    
    
