
def mergeAlternately(word1, word2):
    wordCombo = ''
    biggestWord = word1 if len(word1) > len(word2) else word2
    smallestWord = word2 if word1 == biggestWord else word1
    for i in range(0, len(biggestWord)):
        if i < len(smallestWord):
            wordCombo = wordCombo + word1[i] + word2[i]
        else :
            wordCombo = wordCombo + word1[i]
    return wordCombo

print(mergeAlternately('abcd','efg'))