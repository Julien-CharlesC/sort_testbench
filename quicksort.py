from collections import deque
import random
def quicksort(liste):
    fil = deque()
    n = len(liste)
    fil.append( (0,n) )

    while len(fil) > 0 :

        #original
        Odebut, Ofin = fil.popleft()
        #val qui vont bouger
        debut, fin = Odebut, Ofin

        n = fin - debut

        if n < 2: continue


        val_pivot = liste[random.randrange(Odebut,Ofin)]

        premier_index = None
        while debut != fin:         #fixer ça

            elem = liste[debut]
            #plus grand
            if elem > val_pivot:
                liste[fin-1],liste[debut] = elem, liste[fin-1]
                fin -= 1
            elif elem < val_pivot:
                debut += 1
            else:
                if premier_index is None:
                    premier_index = debut
                    debut += 1
                else:
                    liste[fin-1],liste[debut] = elem, liste[fin-1]
                    fin -= 1

        pivot = debut-1
        liste[pivot] , liste[premier_index] = liste[premier_index], liste[pivot]

        #plus petit
        fil.append( ( Odebut,pivot ) )

        #plus grand
        fil.append( ( pivot+1, Ofin) )
