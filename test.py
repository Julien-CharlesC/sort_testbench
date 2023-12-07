from quicksort import quicksort
from heapsort import heapsort
from random import randrange
from time import time

#paramètre
sorts = (heapsort,quicksort)
nbr_test = 3
porter = 100000000000000
nbr_0 = 7

def creer_liste(n):
    liste = []
    for _ in range( 10**n ):
        liste.append( randrange(porter) ) 
    return liste




def temps():
    res = ""
    with open("res.txt", "w") as fichier:
            fichier.write("début du test\n")
    for n in range(nbr_0):

        totals = dict()
        for sorti in sorts:
            totals[sorti.__name__] = 0
        totals["pythonSort"] = 0
        #quantité de test à faire
        for _ in range(nbr_test):

            liste = creer_liste(n)

            python = liste.copy()
            debut = time()
            python.sort()
            totals["pythonSort"] += time() - debut

            #chacun des algos
            for sorti in sorts:
                copy = liste.copy()
                debut = time()
                sorti(copy)
                totals[sorti.__name__] += time() - debut
                if copy != python:
                    print("erreur") ; exit()


        #faire la moyenne
        res += f"\nn = {10**n:,}\n"
        for key in totals:
            totals[key] /= nbr_test
            res += key
            res += ":\t"
            res += str(totals[key])
            res += "\n"
        with open("res.txt", "a") as fichier:
            fichier.write(res)

temps()
