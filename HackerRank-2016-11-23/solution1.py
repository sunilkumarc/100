mapping = {}
for i in range(1, 27):
    if i < 10:
        mapping[str(i)] = chr(i+96)
    else:
        mapping[str(i)+ '#'] = chr(i+96)

s = '1226#(3)24#(2)4'
# s = '11#'
res = {}
def frequency(s):
    global mapping
    i = 0
    length = int(len(s))
    while i < length:
        if i+2 < length and s[i+2] == '#':
            currStr = s[i] + s[i+1] + '#'
            key = mapping[currStr]
            count = 1
            if i+3 < length and s[i+3] == '(':
                count = s[i+4]
                i += 6
            else:
                i += 3
            if key in res:
                res[key] = res[key]+count
            else:
                res[key] = count

        else:
            key = mapping[s[i]]
            if key in res:
                res[key] = res[key]+1
            else:
                res[key] = 1
            i += 1

frequency(s)
print(res)
