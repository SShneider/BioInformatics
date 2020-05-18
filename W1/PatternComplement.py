# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
def Complement(Pattern):
    # your code here
    dict = {'C':'G', 'A':'T', 'T':'A', 'G':'C'}
    stringout = ''
    for letter in Pattern:
        stringout+=dict[letter]    
    return stringout
        

