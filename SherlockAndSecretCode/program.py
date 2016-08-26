main_string = input()
N = int(input())
res = []

for i in range(N):
    each_string = input()
    index = main_string.find(each_string)
    if index != -1:
        res.append(index)

if len(res) > 0:
    res.sort()
    print(*res)
else:
    print(-1)
