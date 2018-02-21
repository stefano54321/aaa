import numpy as np

def next_pivot(mat, i, j):
     m = len(mat)
     n = len(mat[0])

     for jj in range(j+1,n):
         for ii in range(i+1, m):
             if mat[ii][jj] != 0:
                 return ii,jj
     return -1,-1

def swap(mat, i, j):
    mat[i], mat[j] = mat[j], mat[i]

def dividi(mat, r, e):
    for i in range(len(mat[r])):
        mat[r][i] = mat[r][i]/e

def eliminazione(mat):
    criga = 0
    pi, pj = -1,-1
    pi, pj = next_pivot(mat, criga, 0)
    while (pi,pj) != (-1,-1):
        swap(mat, criga, pi)
        dividi(mat, criga, mat[criga][pj])
        sottrai(mat, criga, pj)
        criga += 1
        pi, pj = next_pivot(mat, criga, pj)







def stampa(m):
    for i in m:
        for j in i:
            print("{0:>4.1f} ".format(j), end='')
        print("\n")



def sottrai(m, r, c):
    for i in range(r+1,len(m)):
        m[i] = [x-m[i][c]*m[r][j] for j,x in enumerate(m[i])]




if __name__ == '__main__':
    a = [[0,7,4],[34,39,67], [7,67,90]]
    i,j = f(a)
    swap(a, 0, i)
    dividi(a, 0, a[0][0] )

    print(np.matrix(a))
