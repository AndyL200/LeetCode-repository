def minDominoRotations(tops, bottoms) -> int:
    # ft = {}
    # fb = {}
    # ht = {}
    # hb = {}
    # d = len(tops)
    # for i in range(d):
    #     if tops[i] not in ft:
    #         ft[tops[i]] = 0
    #         ht[tops[i]] = 0
    #     if bottoms[i] not in fb:
    #         fb[bottoms[i]] = 0
    #         hb[bottoms[i]] = 0
    #     if bottoms[i] == tops[i]:
    #         ft[tops[i]] += 1
    #         hb[bottoms[i]] += 1
    #     else:
    #         ft[tops[i]] += 1
    #         fb[bottoms[i]] += 1
    #         ht[tops[i]] += 1
    #         hb[bottoms[i]] += 1
    #     if ft[tops[i]] == d or hb[bottoms[i]] == d:
    #         return 0

    # m = float('inf')
    # for i in range(1, 7):
    #     if i in ft and i in fb:
    #         if ft[i] + fb[i] >= d:
    #             m = min(m, fb[i])
    #     if i in ht and i in hb:
    #         if ht[i] + hb[i] >= d:
    #             m = min(m, ht[i])

#optimized
    d = len(tops)
    if d == 0:
        return -1

    m = float('inf')
    for target in [tops[0], bottoms[0]]:
        success = True
        missT, missB = 0,0
        for i in range(d):
            if not (tops[i] == target or bottoms[i] == target):
                success = False
                break
            if tops[i] != target:
                missT += 1
            elif bottoms[i] != target:
                missB += 1
        if success:
            m = min(m, missT, missB)
    return m if m != float('inf') else -1

