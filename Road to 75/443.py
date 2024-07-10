def compress(self, chars):
    arr = 0
    for i in range(len(chars)):
        if(chars[i] == chars[i+1]):
            j = i
            while(j < len(chars)):
                if chars[i] == chars[j]:
                    arr += 1
            chars.remove(chars[i])
            for c in str(arr):
                chars.append(c)

print(compress("", ["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    
