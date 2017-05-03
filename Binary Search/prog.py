a = [1, 3, 5, 6, 8, 10]

def binarySearch(a, start, end, elem):
    mid = int(start + (end-start)/2)
    if start <= end:
        if a[mid] == elem:
            return mid
        elif a[mid] > elem:
            return binarySearch(a, start, mid-1, elem)
        else:
            return binarySearch(a, mid+1, end, elem)
    
    return -1

print(a)

def search(elem):
    print('\nSearching for', elem, '...', '\n')
    index = binarySearch(a, 0, len(a)-1, elem)
    if index == -1:
        print('Not found')
    else:
        print('Found at index :', index+1)

search(1)
search(10)
search(100)
