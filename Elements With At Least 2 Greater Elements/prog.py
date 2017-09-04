# Find all the elements in an array which have at least 2 greater elements
# http://www.geeksforgeeks.org/find-elements-array-least-two-greater-elements/

def findElements(arr):
    one = two = float("-inf")
    for elem in arr:
        if elem > one:
            two = one
            one = elem
        elif elem > two:
            two = elem
    
    res = []
    for elem in arr:
        if elem < two:
            res.append(elem)
    
    return res

if __name__ == '__main__':
    arr = [2, 8, 7, 1, 5]
    res = findElements(arr)
    print(res)