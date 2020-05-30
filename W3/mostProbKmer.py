def Pr(Text, Profile):
    output = 1
    for i, letter in enumerate(Text):
        output*=Profile[letter][i]
    return output
def ProfileMostProbableKmer(text, k, profile):
    t=len(text)
    candidate = [0, 0]
    for i in range(t-k+1):
        probable = Pr(text[i:i+k], profile)
        if probable>candidate[1]:
            candidate[1] = probable
            candidate[0] = i
    return text[candidate[0]:candidate[0]+k]