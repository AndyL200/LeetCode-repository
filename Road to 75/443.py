def compress(self, chars):
    i=0
    while i < len(chars):
        arr = 1
        if(i < len(chars)-1 and chars[i] == chars[i+1]):
            j=len(chars)-1
            while chars.count(chars[i]) > 1:
                if chars[j] == chars[i]:
                    arr += 1
                    chars.pop(j)
                j -= 1

            count = 1
            for c in str(arr):
                chars.insert(i + count, c)
                count += 1
        i += 1
    return chars
        
            

print(compress("", ["a","b","b","b","b","b","b",'c','c','t','t','y']))
    
