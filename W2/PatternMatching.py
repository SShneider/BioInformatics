# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Text):
    positions = [] # output variable
    # fill in your function here
    for i in range(0, len(Text)):
        if Text[i:i+len(Pattern)]==Pattern:
            positions.append(i)
    return positions