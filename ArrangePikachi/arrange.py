T = int(input())

for i in range(0, T):
    N = int(input())
    numbers = [int(x) for x in input().strip().split(" ")]
    if len(numbers) > 0:
        numbers.sort()

    print(','.join(map(str,numbers)))
