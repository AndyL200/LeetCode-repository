def longestProperPrefixClean(str):
    lps = [0]*len(str)
    lenProp = 0
    lps[0] = 0
    i = 1

    while i < len(str):
        if str[i] == str[lenProp]:
            lenProp += 1
            lps[i] = lenProp
            i += 1
        else:
            if lenProp != 0:
                lenProp = lps[lenProp-1]
            else:
                lps[i] = 0
                i += 1

    j = 0
    count = 0
    while j < len(str):
        if lps[j] != 0:
            count += 1
        j += 1 
    
    str = str[:(len(str)-count)]

    return str


def gcdOfStrings(self, str1, str2):
    longestString = ""
    usingstring = ""
    shareString = ""
    if min(len(str1),len(str2)) == len(str1):
        usingstring = str1
        longestString = str2
    else:
        usingstring = str2
        longestString = str1

    for i in range(len(usingstring)):
        if str1[i] == str2[i]:
            shareString = shareString + str1[i]
        else :
            break
    truthy = True
    properpre = longestProperPrefixClean(shareString)

    for s in range(len(longestString)):
        if longestString[s] != properpre[s%len(properpre)]:
            truthy = False
    if truthy:
        return properpre
    else:
        return ""



print(gcdOfStrings("", "ABC", "ABCABC"))