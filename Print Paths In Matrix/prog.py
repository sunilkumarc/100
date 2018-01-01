# https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

class Grid:
    def __init__(self, m, n):
        self.rowsCount = m
        self.colsCount = n

    def printPaths(self, row, col, path):
        if row == self.rowsCount - 1:
            for i in range(col, self.colsCount):
                path += ' -> (' + str(row) + ',' + str(i) + ')'
            print(path)
            return
        
        if col == self.colsCount - 1:
            for i in range(row, self.rowsCount):
                path += ' -> (' + str(i) + ',' + str(col) + ')'
            print(path)
            return
        
        path += ' -> (' + str(row) + ',' + str(col) + ')'
        self.printPaths(row + 1, col, path)
        self.printPaths(row, col + 1, path)

if __name__ == '__main__':
    m, n = list(map(int, input().strip().split()))
    grid = Grid(m, n)
    grid.printPaths(0, 0, '')