def mergesort(liste):
    n = len(liste)

    if n == 2:
        return [ min(liste), max(liste) ]
    if n == 1:
        return liste
    else:
        left  = mergesort(liste[:n//2])
        right = mergesort(liste[n//2:])

        i = 0
        j = 0
        res = []
        while i != len(left) and j != len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i != len(left):
            while i != len(left):
                res.append(left[i])
                i+=1
        else: 
            while j != len(right):
                res.append(right[j])
                j+=1
        return res


                
