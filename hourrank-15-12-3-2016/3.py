# https://www.hackerrank.com/contests/hourrank-15/challenges/taras-beautiful-permutations

import itertools
Q = int(input().strip())

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

for _ in range(Q):
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    perms = list(perm_unique(arr))
    count = 0
    for perm in perms:
        flag = False
        perm = list(perm)
        for i in range(len(perm)-1):
            if perm[i] == perm[i+1]:
                flag = True
                break
        if flag == False:
            count += 1

    print(count%1000000007)
