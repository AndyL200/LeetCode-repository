def validateCoupons(code, businessLine, isActive):
    def isalphanmeric(s):
        for char in s:
            if not (char.isalpha() or char.isdigit() or char == '_'):
                return False
        return True
    res = []
    priority = {"restaurant": 4, "pharmacy": 3, "grocery": 2, "electronics": 1}
    for i in range(len(code)):
        codeValid = False
        busValid = False
        if isalphanmeric(code[i]):
            codeValid = True
        if businessLine[i] in priority:
            busValid = True
        if codeValid and busValid and isActive[i]:
            res.append([code[i], businessLine[i]])


    res = sorted(res, key=lambda x: (priority[x[1]], x[0]))
    
    res2 = []
    for r in res:
        res2.append(r[0])
    return res2


validateCoupons(["SAVE20","","PHARMA5","SAVE@20"], ["restaurant","grocery","pharmacy","restaurant"], [True,True,True,True])
