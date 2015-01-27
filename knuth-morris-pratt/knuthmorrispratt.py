def knuthMorrisPratt(text, pattern):
    shifts = buildTable(pattern)
    startPos = 0
    matchLen = 0
    for character in text:
        while (matchLen == len(pattern) or matchLen >= 0 and pattern[matchLen] != character):
            startPos += shifts[matchLen]
            matchLen -= shifts[matchLen]
        matchLen += 1
        if matchLen == len(pattern):
            return startPos
            
def buildTable(pattern):
    size = len(pattern)
    shifts = [1] * (size + 1)
    shift = 1
    for pos in range(size):
        while shift <= pos and pattern[pos] != pattern[pos-shift]:
            shift += shifts[pos-shift]
        shifts[pos+1] = shift
    return shifts

text = "abab"*100 + "abba"
pattern = "abba"
print(knuthMorrisPratt(text, pattern))
    
