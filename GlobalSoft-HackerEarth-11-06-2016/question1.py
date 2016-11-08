N, M = map(int, input().strip().split())
latencies = []
newCables = []

for _ in range(M):
    A, B, L = map(int, input().strip().split())
    if A != B:
        latencies.append(L)

Q = int(input())
if Q > 0:
    newCables = list(map(int, input().strip().split()))

for item in newCables:
    latencies.append(item)

latencies.sort()
res = 0
for i in range(N-1):
    res += latencies[i]

print(res)
