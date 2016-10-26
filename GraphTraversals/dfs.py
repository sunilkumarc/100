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

def getNeighbours(adjMatrix, vertex):
    neighbours = []
    for i in range(len(adjMatrix[vertex])):
        if adjMatrix[vertex][i] == 1:
            neighbours.append(i)
    return neighbours

def DFS(adjMatrix, V, startFrom):
    visited = [False for i in range(V)]
    stack = Stack()
    stack.push(startFrom)
    while stack.isEmpty() == False:
        vertex = stack.pop()
        if visited[vertex] == False:
            visited[vertex] = True
            print('Visiting : ', vertex)
            neighbours = getNeighbours(adjMatrix, vertex)
            for neighbour in neighbours:
                stack.push(neighbour)

if __name__ == '__main__':
    V = int(input().strip())
    adjMatrix = []

    for i in range(V):
        adjMatrix.append([int(v) for v in input().split(' ')])

    print(adjMatrix)
    startFrom = 1
    DFS(adjMatrix, V, startFrom)
