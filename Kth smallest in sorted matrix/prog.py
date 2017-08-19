class Node():
    def __init__(self, value, row, column):
        self.value = value
        self.row = row
        self.column = column

def heapify(heap, index, heapSize):
    left = 2 * index + 1
    right = 2 * index + 2
    smallest = index

    if left < heapSize and heap[left].value < heap[smallest].value:
        smallest = left

    if right < heapSize and heap[right].value < heap[smallest].value:
        smallest = right

    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        heapify(heap, smallest, heapSize)

def findKthSmallest(mat, rows, cols, K):
    MAX_INT = mat[rows-1][cols-1] + 1
    matrix = []
    for row in range(rows):
        eachRow = []
        for col in range(cols):
            eachRow.append(Node(mat[row][col], row, col))
        matrix.append(eachRow)

    minHeap = matrix[0]
    result = []
    for i in range(K):
        root = minHeap[0]
        result.append(root.value)
        if root.row + 1 < rows and root.column < cols:
            minHeap[0] = matrix[root.row + 1][root.column]
        else:
            minHeap[0] = Node(MAX_INT, root.row + 1, root.column)

        heapify(minHeap, 0, len(minHeap))

    print(result[len(result)-1])

if __name__ == '__main__':
    K = int(input().strip())
    rows, cols = list(map(int, input().strip().split()))
    matrix = []

    if K <= rows*cols:
        for i in range(rows):
            row = list(map(int, input().strip().split()))
            matrix.append(row)

        findKthSmallest(matrix, rows, cols, K)
    else:
        print('K cannot be bigger than number of elements in the matrix')
