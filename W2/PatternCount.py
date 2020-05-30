def PatternCount(Text, Pattern):
    # fill in your function here
    count = 0
    for i in range(0, len(Text)):
        if Text[i:i+len(Pattern)]==Pattern:
            count+=1
    return count

