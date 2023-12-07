from quicksort import quicksort
from heapsort import heapsort
from wmergesort import mergesort
from random import randrange
from time import time
import math
import sys, os

#paramètre
sorts = (heapsort,quicksort,mergesort)
nbr_test = 10
porter = 100000000000000
machine =   os.path.basename(sys.executable)

if machine == "pypy3":
    nbr_0 = 8
else:
    nbr_0 = 7

print(f"\nn = {10**(nbr_0-1):,}")
print(machine)


def creer_liste(n):
    liste = []
    for _ in range( 10**n ):
        liste.append( randrange(porter) ) 
    return liste




def temps():
    res = ""
    with open(machine+"_res.txt", "w") as fichier:
            fichier.write("début du test\n")

    futur = dict()
    for sorti in sorts:
        futur[sorti.__name__] = 0
    futur["pythonSort"] = 0

    for n in range(4,nbr_0):

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
                    print(f"erreur pour {sorti.__name__}")
                    exit()


        #faire la moyenne
        res += f"\nn = {10**n:,}\n"
        for key in totals:
            totals[key] /= nbr_test
            res += key
            res += "\t"
            res += str(totals[key])
            res += "\tprévu:" + str(futur[key])
            res += "\n"
            futur[key] = totals[key] * ( (10*math.log(10))/math.log(10**n)+10 )

        if n == 4 : res = "" ; continue
        with open(machine+"_res.txt", "a") as fichier:
            fichier.write(res)
            res = ""

temps()
