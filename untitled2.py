# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 15:14:41 2018

@author: stefa
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 17:48:19 2018

@author: stefa
"""

import numpy as np

def swap(mat, i, j):
    mat[i], mat[j] = mat[j], mat[i]
#eliminare swap

def find_pivot(mat, start, col):
    m = len(mat)  # m è il numero delle righe
    for i in range(start, m):
        if mat[i][col] != 0:
            return i
    return -1


def eliminazione(mat):
    nrighe=len(mat)
    ncolonne=len(mat[0])
    riga_pivot = 0
    col = 0
    minimo=min(nrighe,ncolonne)
    while riga_pivot < minimo:
        p = find_pivot(mat, riga_pivot, col) # p è l'indice di riga del pivot trovato
        while  p==-1 and col<ncolonne-1:
            col += 1
            p = find_pivot(mat, riga_pivot, col)
        if p != -1:
            swap(mat, riga_pivot, p)
            #divide
            for i in range(col,ncolonne):
                mat[riga_pivot][i] /= mat[riga_pivot][col]
            #sottrae
            for i in range(riga_pivot+1,nrighe):
                a=mat[i][col]
                mat[i] =[ x-a*mat[riga_pivot][j] if j>=col else 0  for j,x in enumerate(mat[i])]
        riga_pivot +=1


if __name__ == '__main__':
    a = [[0,3,0,6,0],[0,0,0,8,7],[0,0,0,9,6]]
    print(np.matrix(a))
    print()
    eliminazione(a)
    print(np.matrix(a))
    
    print()
    print()
    print()
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
