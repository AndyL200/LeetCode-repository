def needHay(self, haystack, needle):
    count = 0
    temp = [0]*len(haystack)
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            temp[count] = i
            count+=1

   
    for i in range(count):
        count2 = 0
        for j in range(temp[i],len(haystack)):
            if haystack[j] == needle[count2]:
                count2+=1
                if count2 == len(needle):
                    return temp[i]
            else:
                break
    return -1

print(needHay("","stackhay","hay"))