# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    # your code here
    return Reverse(Complement(Pattern))
# Copy your Reverse() function here.
def Reverse(Pattern):
    return Pattern[::-1]
def Complement(Pattern):
    # your code here
    dict = {'C':'G', 'A':'T', 'T':'A', 'G':'C'}
    stringout = ''
    for letter in Pattern:
        stringout+=dict[letter]    
    return stringout
        
