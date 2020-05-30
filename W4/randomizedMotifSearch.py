# import the random package here
import random
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)

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
def Consensus(Motifs):
    consOut = ''
    count = ProfileWithPseudocounts(Motifs)
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
def RandomMotifs(Dna, k, t):
    # place your code here.
    lst = []
    for item in Dna:
        randIdx = random.randint(0, t-k)
        lst.append(item[randIdx:randIdx+k])
    #print(lst)
    return lst
def Pr(Text, Profile):
    output = 1
    for i, letter in enumerate(Text):
        output*=Profile[letter][i]
    return output
def MotifsT(pf,dna):

    k = len(pf['A'])
    D = []
    for i in range(0,len(dna)):
        km = []
        sc = []
        for kk in range(len(dna[i])-k+1):
            km += [dna[i][kk:kk+k]]
        for i in km:
            sc += [Pr(i,pf)]
        D += [km[sc.index(max(sc))]]

    return D
# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
# def ProfileWithPseudocounts(Motifs):
#    t = len(Motifs)+4
#    k = len(Motifs[0])
#    count = {'A':[1/(t)]*k, 'C': [1/(t)]*k, 'G':[1/(t)]*k, 'T':[1/(t)]*k}
#    for i in range(t-4):
#        for j in range(k):
#            count[Motifs[i][j]][j]+=1/(t)
#    return count
def ProfileWithPseudocounts(MotIn):
    #print(MotIn)
    t = len(MotIn)+4
    k = len(MotIn[0])
    count = {'A':[1/(t)]*k, 'C': [1/(t)]*k, 'G':[1/(t)]*k, 'T':[1/(t)]*k}
    for i in range(t-4):
        for j in range(k):
            count[MotIn[i][j]][j]+=1/(t)
    return count
def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, len(Dna[0]))
    BestMotifs = M
    while True:
        #print(M)
        Profile = ProfileWithPseudocounts(M)
        #print(Profile)
        M = MotifsT(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 