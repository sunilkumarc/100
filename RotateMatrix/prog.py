def rotateLayer(matrix, layer, N):
    currentLen = N - 2*layer
    for i in range(currentLen-1):
        temp = matrix[layer][layer+i]

        nextRow = layer + i
        nextCol = layer + currentLen - 1
        temp, matrix[nextRow][nextCol] = matrix[nextRow][nextCol], temp

        nextRow = nextCol
        nextCol = nextCol - i
        temp, matrix[nextRow][nextCol] = matrix[nextRow][nextCol], temp

        nextCol = layer
        nextRow = (N-1) - layer - i
        temp, matrix[nextRow][nextCol] = matrix[nextRow][nextCol], temp

        nextRow = layer
        nextCol = layer + i
        temp, matrix[nextRow][nextCol] = matrix[nextRow][nextCol], temp

def displayArray(arr, N):
    for row in arr:
        print(*row, sep='   ')

def rotateArray(matrix, N):
    for layer in range(int(N/2)):
        rotateLayer(matrix, layer, N)

if __name__ == '__main__':
    N = int(input().strip())
    matrix = []

    for row in range(N):
        matrix.append(list(map(int, input().strip().split())))

    displayArray(matrix, N)
    rotateArray(matrix, N)
    print()
    displayArray(matrix, N)
