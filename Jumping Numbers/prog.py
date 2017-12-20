# http://www.geeksforgeeks.org/print-all-jumping-numbers-smaller-than-or-equal-to-a-given-value/

def findJumping(num, X):
    queue = []
    queue.append(num)
    
    while len(queue) != 0:
        N = queue.pop(0)
        if N <= X:
            print(N)
            lastDigit = N%10
            
            if lastDigit == 0:
                queue.append(N*10 + 1)
            elif lastDigit == 9:
                queue.append(N*10 + 8)
            else:
                queue.append(N*10 + (lastDigit+1))
                queue.append(N*10 + (lastDigit-1))


if __name__ == '__main__':
    X = int(input('Enter X : ').strip())
    i = 1
    while i <= X and i <= 9:
        findJumping(i, X)
        i += 1