T = int(input())
trans = [float(x) for x in input().split(" ")]
Q = int(input())

def findMaxTrans(target):
    current_sum = 0
    num = 0

    for i in trans:
        current_sum += i
        num += 1

        if current_sum >= target:
            return num

for _ in range(Q):
    target = int(input())
    print(findMaxTrans(target))
