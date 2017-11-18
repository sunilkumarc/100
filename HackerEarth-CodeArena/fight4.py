# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/mixing-strings-1/
# INCOMPLETE - 4/10 passing

def append(one, two, L1, L2):
    l = L1
    if l > L2:
        l = L2
    
    i = L1-l
    j = 0
    res = one[:i]
    while i < L1 and j < L2:
        if one[i:] == two[:(l-j)]:
            return one[:i] + two
        else:
            i += 1
            j += 1
    
    return one + two


if __name__ == '__main__':
    N = int(input().strip())
    
    strings = []
    for _ in range(N):
        strings.append(input().strip())
    
    print('Strings : ', strings)
    if len(strings) > 0:
        res = strings[0]
        for i in range(1, len(strings)):
            res = append(res, strings[i], len(res), len(strings[i]))

        print(res, len(res))
        
    
