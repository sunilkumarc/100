# https://leetcode.com/problems/longest-palindromic-substring/description/

def findLPS(s, N):
    maxSize = 1
    start = end = 0
    mat = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        mat[i][i] = 1
    
    for i in range(N-1):
        if s[i] == s[i+1]:
            mat[i][i+1] = 2
            if mat[i][i+1] > maxSize:
                maxSize = mat[i][i+1]
                start = i
                end = start + 1
    
    for size in range(3, N+1):
        for i in range(N-size+1):
            j = i + size - 1
            if s[i] == s[j] and mat[i+1][j-1] != 0:
                mat[i][j] = 2 + mat[i+1][j-1]
                if mat[i][j] > maxSize:
                    maxSize = mat[i][j]
                    start = i
                    end = j
            j += 1
    
    print('Start %s, End %s, Size %s' %(start, end, maxSize))
    return s[start:end+1]

if __name__ == '__main__':
    s = input().strip()
    N = len(s)
    print(findLPS(s, N))