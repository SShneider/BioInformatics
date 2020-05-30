# Input:  A set of kmers Motifs
# Output: Count(Motifs)
def Count(Motifs):
    k = len(Motifs[0])
    count = {'A':[0]*k, 'C': [0]*k, 'G':[0]*k, 'T':[0]*k} # initializing the count dictionary
    for i in range(len(Motifs)):
        for j in range(len(Motifs[i])):
            count[Motifs[i][j]][j]+=1
    return count