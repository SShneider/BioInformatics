def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {'A':[0]*k, 'C': [0]*k, 'G':[0]*k, 'T':[0]*k}
    for i in range(t):
        for j in range(k):
            count[Motifs[i][j]][j]+=1/t

    return count
def Consensus(Motifs):
    consOut = ''
    count = Profile(Motifs)
    k = len(Motifs[0])
    for i in range(k):
        maxFreq = ['', 0]
        for item in count:
            if count[item][i]>0.5:
                consOut+=item
                maxFreq=['', 0]
                break
            else: 
                if count[item][i]>maxFreq[1]:
                    maxFreq[0]=item
                    maxFreq[1] = count[item][i]
        consOut+= maxFreq[0]
    return consOut   
def Score(Motifs):
    # Insert code here
    cons = Consensus(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    count = 0
    for i in range(t):
        for j in range(k):
            if Motifs[i][j]!=cons[j]:
                count+=1
    return count
    