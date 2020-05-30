# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[1]*k, 'C': [1]*k, 'G':[1]*k, 'T':[1]*k} # initializing the count dictionary
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            count[Motifs[i][j]][j]+=1
    return count