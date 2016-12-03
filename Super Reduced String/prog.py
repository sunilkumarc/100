# https://www.hackerrank.com/challenges/reduced-string

def reduceString(s, N):
    s = list(s)
    i = 0
    while i < N-1:
        if s[i] == s[i+1]:
            del s[i]
            del s[i]
            if i > 0:
                i -= 1
            N -= 2
        else:
            i += 1

    res = ''.join(s)
    if res == '':
        return 'Empty String'
    else:
        return res

if __name__=='__main__':
    s = input().strip()
    s = reduceString(s, len(s))
    print(s)
