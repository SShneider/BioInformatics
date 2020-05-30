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
    output = 1
    for i, letter in enumerate(Text):
        output*=Profile[letter][i]
    return output
# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    print('text', Text)
    n = len(Text)
    probabilities = {} 
    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)