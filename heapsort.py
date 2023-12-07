from collections import deque
def getLeft(i):
    return (i*2)+1
def getRight(i):
    return (i*2)+2

#tamise un noeud vers le bas
#i: index       n:taille de la liste
def fixHeap(liste,n,plage,swap):
    ncopy = n
    for i in range(plage[0], plage[1]):

        if swap:
            n = ncopy-i-1
            liste[0], liste[n] = liste[n], liste[0]
            i = 0
        else:
            i = n-1-i

        Next = i
        test = True
        while test:
            i = Next
            test = False
        
            #trouve l'index de left
            left = getLeft(i)
            #si la feuille est pas dans la liste, return
            if left  >= n: break

            #trouve l'index de right
            right = getRight(i)
            #si la feuille est pas dans la liste, return
            if right >= n: right = i

            #trouve leur valeur
            right_value = liste[right]
            left_value = liste[left]
            i_value = liste[i]

            #trouve le plus grand enfant
            if left_value > right_value:
                j = left ; k = left_value
            else:
                j = right ; k = right_value

            #si enfant > parent, switch
            #puis repare l'enfant
            if i_value < k:
                liste[i],liste[j] = k, i_value
                Next = j
                test = True

def heapsort(liste):

    n = len(liste)

    #tamise tous les noeuds(pas les feuilles)
    #forme le heap
    fixHeap( liste, n, ( (n//2)-1 , n ) , False )

    #pull le plus grand et le met à la fin
    #puis, répare le heap
    fixHeap(liste, n, (0,n,1), True)
