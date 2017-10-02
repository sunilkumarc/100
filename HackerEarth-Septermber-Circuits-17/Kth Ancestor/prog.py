# https://www.hackerearth.com/challenge/competitive/september-circuits-17/algorithm/little-shino-and-k-ancestor-57fdef57/
# 88/100 points

if __name__ == '__main__':
    N, K = map(int, input().strip().split())
    colors = list(map(int, input().strip().split()))

    mapping = dict()
    for _ in range(N-1):
        fromNode, toNode = map(int, input().strip().split())
        if fromNode > toNode:
            fromNode, toNode = toNode, fromNode
        
        if toNode not in mapping:
            mapping[toNode] = fromNode
        
    res = []
    for node in range(1, len(colors)+1):
        ktemp = K
        ancestorNode = node
        while ktemp > 0:
            if ancestorNode not in mapping:
                break
            ancestorNode = mapping[ancestorNode]
            ktemp -= 1
            
        if ktemp == 0 and colors[node-1] == colors[ancestorNode-1]:
            res.append(1)
        else:
            res.append(-1)
        

    print(*res)
