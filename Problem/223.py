def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """
    :type ax1: int
    :type ay1: int
    :type ax2: int
    :type ay2: int
    :type bx1: int
    :type by1: int
    :type bx2: int
    :type by2: int
    :rtype: int
    """
    aWidth = ax2-ax1
    aLength = ay2-ay1
    bWidth = bx2-bx1
    bLength = by2-by1
    CrossWidth = 0
    CrossLength = 0

    Crossy = ay1 <= by2  and  ay2 >= by1
    Crossx = ax1 <= bx2 and ax2 >= bx1
    if(Crossy and Crossx):
        if(ay2 >= by2):
            CrossLength = min(by2-ay1,by2-by1)
        else:
            CrossLength = min(ay2-by1,ay2-ay1)
        if(ax2 >= bx2):
            CrossWidth = min(bx2-ax1,bx2-bx1)
        else:
            CrossWidth = min(ax2-ax1,ax2-bx1)
        return (aWidth * aLength) + (bWidth * bLength) - (CrossLength * CrossWidth)
    else:
        return (aWidth * aLength) + (bWidth * bLength) 
    
print(computeArea(-2,-2,2,2,-1,4,1,6))