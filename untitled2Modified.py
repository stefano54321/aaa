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

#import numpy as np


def swap(mat, i, j):
    mat[i], mat[j] = mat[j], mat[i]


def find_pivot(mat, start, col):
    m = len(mat)  # m è il numero delle righe
    for i in range(start, m):
        if mat[i][col] != 0:
            return i
    return -1

def stampa(mat,li=[]):
    nrighe=len(mat)
    for i in range(nrighe):
        pre=post=''
        if i in li:
            pre='\x1b[1;35;40m'
            post='\x1b[0m'
        
        print( pre+" ".join("{:>4.1f}".format(x) for x in mat[i][0:-1])+post , end=' | ' )
        print( pre+"{:>4.1f}".format(mat[i][-1])+post )
    print()
    

    


def eliminazione(mat):
    
    flag=input("Press any key to proceed step by step ('q' to run to the end) ... ")
    
    nrighe=len(mat)
    ncolonne=len(mat[0])
    riga_pivot = 0
    col = 0
    minimo=min(nrighe,ncolonne-1) # non cerco il pivot sulla colonna dei termini noti
    while riga_pivot < minimo:
        p = find_pivot(mat, riga_pivot, col) # p è l'indice di riga del pivot trovato
        while  p==-1 and col<ncolonne-1:
            col += 1
            p = find_pivot(mat, riga_pivot, col)
        if p != -1:
            swap(mat, riga_pivot, p)
            stampa(mat,[riga_pivot,p])
            if flag!='q': flag=input("...")
            #divide
            val=mat[riga_pivot][col]
            for i in range(col,ncolonne):
                mat[riga_pivot][i] /= val
            stampa(mat,[riga_pivot])
            if flag!='q': flag=input("...")
            #sottrae
            for i in range(riga_pivot+1,nrighe):
                a=mat[i][col]
                mat[i] =[ x-a*mat[riga_pivot][j] if j>=col else 0  for j,x in enumerate(mat[i])]
                stampa(mat,[i])
                if flag!='q': flag=input("...")
        riga_pivot +=1
        

if __name__ == '__main__':
    A = [[0,3,4],   #matrice dei coefficienti
         [3,4,0],
         [0,0,0],
         [0,3,0]]
         
    b = [2,2,2,2] # vettore dei termini noti
    
    Ab = [ A[i]+[b[i]] for i in range(len(A)) ]  # matrice completa
    stampa(Ab,[])
    print()
    eliminazione(Ab)
    
    
    
#    print()
#    print()
#    print()
#    b = [[10, 0, 7, 9], [12,23,45, 34], [60, 55, 7, 5], [7,3,65,7]]
#    c = [[1,2,3,4],[1,2,3,4],[4,5,6,10],[7,8,9,10]]
#    d = [[0,0,0],[0,0,1]]
#    eliminazione(a)
#    eliminazione(b)
#    eliminazione(c)
#    eliminazione(d)
#    print(np.matrix(a))
#    print(np.matrix(b))
#    print(np.matrix(c))
#    print(np.matrix(d))
