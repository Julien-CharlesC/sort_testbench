from collections import deque
def mergesort(liste):

    plan = deque()
    tri = deque()

    plan.append(    (0,len(liste))  )
    if len(liste) == 2:
        if liste[0] > liste[1]:
            liste[0],liste[1] = liste[1],liste[0]
    while plan:
        debut,fin = plan.popleft()
        n = fin - debut


        if n <= 2: 
            continue
        else:

            pivot = n//2 + debut
            plan.append( (debut,pivot) )
            plan.append( (pivot,fin)   )

            tri.append( (debut,pivot)  )
            tri.append( (pivot,fin  )  )

    while tri:

        dr,fr = tri.pop()
        nr = fr - dr

        dl,fl = tri.pop()
        nl = fl - dl

        if nl <= 2: 
            if liste[dl] > liste[fl-1]:
                liste[dl],liste[fl-1] = liste[fl-1],liste[dl]
        if nr <= 2:
            if liste[dr] > liste[fr-1]:
                liste[dr],liste[fr-1] = liste[fr-1],liste[dr]

        right = liste[dr:fr]
        left  = liste[dl:fl]


        i = 0 ; j = 0 ; index = dl

        while i!=nl and j !=nr:
            if left[i] > right[j]:
                liste[index] = right[j]
                index += 1 ; j += 1
            else:
                liste[index] = left[i]
                index += 1 ; i += 1
        if i !=nl:
            while i !=nl:
                liste[index] = left[i]
                index += 1 ; i += 1
        else:
            while j !=nr:
                liste[index] = right[j]
                index += 1 ; j += 1


