import math

class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise Exception('Stack is empty')

    def push(self, elem):
        self.stack.append(elem)

visited = []

def getNeighbours(matrix, building, N, M, J):
    neighbours = []
    x, y = building[0]-1, building[1]-1
    left = y - 1
    if left >= 0 and visited[x][left] == 0 and (matrix[x][y]-matrix[x][left] <= J):
        neighbours.append((x+1, left+1))

    top = x - 1
    if top >= 0 and visited[top][y] == 0 and (matrix[x][y]-matrix[top][y] <= J):
        neighbours.append((top+1, y+1))

    right = y + 1
    if right < M and visited[x][right] == 0 and (matrix[x][y]-matrix[x][right] <= J):
        neighbours.append((x+1, right+1))

    bottom = x + 1
    if bottom < M and visited[bottom][y] == 0 and (matrix[x][y]-matrix[bottom][y] <= J):
        neighbours.append((bottom+1, y+1))

    return neighbours

def canEscape(building, N, M):
    x, y = building
    if x == 1 or x == M or y == 1 or y == N:
        # print('Returning True for : ', building)
        return True
    return False

def findPath(N, M, matrix, Dx, Dy, J):
    global visited
    stack = Stack()
    stack.push((Dx, Dy))
    path = []
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[Dx][Dy] = 1

    while stack.isEmpty() == False:
        building = stack.pop()
        path.append(building)
        if canEscape(building, N, M) == True:
            print('YES')
            return path

        neighbours = getNeighbours(matrix, building, N, M, J)
        for neighbour in neighbours:
            stack.push(neighbour)


if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        N, M = map(int, input().strip().split())
        matrix = []
        for i in range(N):
            row = list(map(int, input().strip().split()))
            matrix.append(row)

        Dx, Dy, J = map(int, input().strip().split())


        # print(getNeighbours(matrix, (4, 4), N, M))
        path = findPath(N, M, matrix, Dx, Dy, J)
        for building in path:
            print(building[0], building[1])
