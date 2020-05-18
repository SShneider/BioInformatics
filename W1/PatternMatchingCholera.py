# Copy your PatternMatching function below this line.

# The following lines will automatically read in the Vibrio cholerae genome for you and store it in a variable named v_cholerae
import sys                              # needed to read the genome
input = sys.stdin.read().splitlines()   #
v_cholerae = input[1]                   # store the genome as 'v_cholerae'


# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Text):
    positions = [] # output variable
    # fill in your function here
    for i in range(0, len(Text)):
        if Text[i:i+len(Pattern)]==Pattern:
            positions.append(i)
    return positions
print(PatternMatching("CTTGATCAT", v_cholerae))
# print the positions variable