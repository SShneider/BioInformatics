# Insert your Count(Motifs) function here from the last Code Challenge.

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[0]*k, 'C': [0]*k, 'G':[0]*k, 'T':[0]*k}
    profile = {}
    for i in range(t):
        for j in range(k):
            count[Motifs[i][j]][j]+=1/t

    return count