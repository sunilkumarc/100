import collections

T = int(input())

for i in range(0, T):
    N = int(input())
    numbers = [int(x) for x in input().strip().split(" ")]
    numbers = [item for item, count in collections.Counter(numbers).items() if count > 1]

    if len(numbers) > 0:
        numbers.sort(reverse=True)

    if (len(numbers) < 2):
        print(-1)
    else:
        print(numbers[0] * numbers[1])
