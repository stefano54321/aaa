import numpy as np

def swap(mat, i, j):
    mat[i], mat[j] = mat[j], mat[i]


def find_pivot(mat, start, col):
    m = len(mat)
    for i in range(start, m):
        if col < len(mat[0]) and mat[i][col] != 0:
            return i
    return -1


def eliminazione(mat):
    riga_pivot = 0
    col = 0
    while riga_pivot < len(mat[0]):
        p = find_pivot(mat, riga_pivot, col)
        while  p==-1 and col<len(mat):
            col += 1
            p = find_pivot(mat, riga_pivot, col)
        if p != -1:
            swap(mat, riga_pivot, p)
            #divide
            for i in range(len(mat[0])):
                mat[riga_pivot][i] /= mat[riga_pivot][col]
            #sottrae
            for i in range(riga_pivot+1,len(mat)):
                mat[i] = [x-mat[i][col]*mat[riga_pivot][j] for j,x in enumerate(mat[i])]
        riga_pivot +=1


if __name__ == '__main__':
    a = [[0,1,3],[3,5,6],[7,8,9]]
    b = [[10, 0, 7, 9], [12,23,45, 34], [60, 55, 7, 5], [7,3,65,7]]
    c = [[1,2,3,4],[1,2,3,4],[4,5,6,10],[7,8,9,10]]
    d = [[0,0,0],[0,0,1]]
    eliminazione(a)
    eliminazione(b)
    eliminazione(c)
    eliminazione(d)
    print(np.matrix(a))
    print(np.matrix(b))
    print(np.matrix(c))
    print(np.matrix(d))
