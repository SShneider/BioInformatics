# first, import the random package
import random
# Input:  A dictionary Probabilities whose keys are k-mers and whose values are the probabilities of these kmers
# Output: A randomly chosen k-mer with respect to the values in Probabilities
def WeightedDie(Probabilities):
    kmer = '' # output variable
    val = random.uniform(0,1)

    count = 0
    for item in Probabilities:
        count+=Probabilities[item]
        if count>val:
            return item