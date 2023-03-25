#i shoudl be using complete links for my dendogram
#this alrgorith uses the Damerau–Levenshtein distance
#   note: this does not calculate distance with adjacent transpositions
#https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance 
#this modeule retuns an int representing the distance between 2 strings
#Big O of (2*n), big oof


def DistanceMetric(S1, S2):
    alphieSize = 26
    d = {}
    S1Length = len(S1)
    S2Length = len(S2)

    for i in range(-1, S1Length):
        d[(i, -1)] =  i + 1
    for j in range(-1, S2Length):
        d[(-1,j)] = j + 1
    
    for i in range(0, S1Length):
        for j in range(0, S2Length):
            if S1[i] == S2[j]:
                cost = 0
            else:
                cost = 1
            d[i,j] = min(
                d[(i-1, j)] + 1,
                d[(i, j-1)] + 1,
                d[(i-1, j-1)] + cost,
            )
            if i > 0 and j > 0 and S1[i] == S2[j-1] and S1[i-1] == S2[j]:
                d[(i, j)] = min(
                    d[(i-2, j-2)] + 1,
                    d[(i, j)]
                )
    return d[(S1Length - 1, S2Length - 1)]


    
    
#the below code is meant for testing functionality uncomment to test
#string1 = input("sting 1:")
#string2 = input("sting 2:")
#print(distanceMetric(string1, string2))



