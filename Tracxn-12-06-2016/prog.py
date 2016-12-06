# Bomber aglorithm bombs same continuous characters of minimum length 3
# and returns the resulting string
# 
# Ex: abcdddcbfgf -> abccbfgf 

def bomber_algo(s):
    s = list(s)
    l = len(s)

    if l <= 2:
        return

    i = 0
    while i < l-2:
        if s[i] == s[i+1] and s[i] == s[i+2]:
            del s[i]
            del s[i]
            del s[i]
            while i > 0 and s[i] == s[i-1]:
                i -= 1
            l -= 3
        else:
            i += 1
    
    res = ''.join(s)
    if res == '':
        return 'Empty String'
    else:
        return res

print(bomber_algo(input('Enter Input: ')))