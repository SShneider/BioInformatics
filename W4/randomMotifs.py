# import Python's 'random' module here
import random
# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    # place your code here.
    lst = []
    for item in Dna:
        randIdx = random.randint(0, len(Dna[0])-k)
        lst.append(item[randIdx:randIdx+k])
    
    return lst