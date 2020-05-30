# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)+4
    k = len(Motifs[0])
    count = {'A':[1/(t)]*k, 'C': [1/(t)]*k, 'G':[1/(t)]*k, 'T':[1/(t)]*k}
    
    profile = {}
    for i in range(t-4):
        for j in range(k):
            count[Motifs[i][j]][j]+=1/(t)

    return count
