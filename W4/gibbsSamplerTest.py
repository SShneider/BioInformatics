# import the random package
import random    
# Copy your GibbsSampler function (along with all required subroutines) below this line
# first, import the random package
import random
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
    count = ProfileWithPseudocounts(Motifs, float("inf"))
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
import random
def WeightedDie(Probabilities):
    kmer = '' # output variable
    val = random.uniform(0,1)

    count = 0
    for item in Probabilities:
        count+=Probabilities[item]
        if count>val:
            return item
def Normalize(Probabilities):
    # your code here
    total = sum(Probabilities.values())
    for item in Probabilities:
        Probabilities[item] /= total
    return Probabilities
def Pr(Text, Profile):
    #if len(Profile['A'])<8: 
      #print('in Pr')
      #print(len(Text))
      #print(len(Profile['A']))
      #print(Profile)
    output = 1
    for i, letter in enumerate(Text):
        if i == len(Text)-1:
            break
        output*=Profile[letter][i]
    return output
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    #print('in progenstr', probabilities)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)
def RandomMotifs(Dna, k, t):
    # place your code here.
    lst = []
    for item in Dna:
        randIdx = random.randint(0, len(Dna[0])-k)
        lst.append(item[randIdx:randIdx+k])
    #print(lst)
    return lst
def ProfileWithPseudocounts(MotIn, toIgnore):
    #print(MotIn)
    t = len(MotIn)+4
    k = len(MotIn[0])
    count = {'A':[1/(t)]*k, 'C': [1/(t)]*k, 'G':[1/(t)]*k, 'T':[1/(t)]*k}
    for i in range(t-4):
        if i == toIgnore:
            continue
        for j in range(k):
            count[MotIn[i][j]][j]+=1/(t)
    return count
# Output: GibbsSampler(Dna, k, t, N)
#GibbsSampler(Dna, k, t, N)
   #     randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    #    ﻿BestMotifs ← Motifs
   #     for j ← 1 to N
        #    i ← randomly generated integer between 1 and t
        #    Profile ← profile matrix formed from all strings in Motifs except for Motifi
        #    Motifi ← Profile-randomly generated k-mer in the i-th string
        #    if Score(Motifs) < Score(BestMotifs)
         #       BestMotifs ← Motifs
       # return BestMotifs
def GibbsSampler(Dna, k, t, N):
    #print(Dna)
    BestMotifs = RandomMotifs(Dna, k, t)
    #print('bestmotifs Init', BestMotifs)
    Motifs = BestMotifs.copy()
    #print('bestm copied', Motifs)
    for i in range(N):
        #print('Mots in loop', Motifs)
        toIgnore = random.randint(0, t-1)
        profile = ProfileWithPseudocounts(Motifs, toIgnore)
        #print(profile)
        Motif_i = ProfileGeneratedString(Dna[toIgnore], profile, k)
        Motifs[toIgnore] = Motif_i
        #print(BestMotifs, Motifs, Score(Motifs), Score(BestMotifs))
        if Score(Motifs)<Score(BestMotifs):
            #print('Hello')
            BestMotifs=Motifs.copy()
    # output variable
    # your code here
    return BestMotifs
# Copy the ten strings occurring in the hyperlinked DosR dataset below.
Dna =["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC", "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG", "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC", "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC", "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG", "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA", "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA", "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG", "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG", "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

# set t equal to the number of strings in Dna, k equal to 15, and N equal to 100
t = len(Dna)
k = 15
N = 100
# Call GibbsSampler(Dna, k, t, N) 20 times and store the best output in a variable called BestMotifs
BestMotifs = GibbsSampler(Dna, k, t, N)
# Print the BestMotifs variable
print(BestMotifs)
# Print Score(BestMotifs)
print(Score(BestMotifs))