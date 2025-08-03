def findMedianSortedArrays(nums1, nums2) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total//2

    if len(A) == total:
        if total % 2:
            return A[half]
        else:
            return (A[half] + A[half-1])/2.0
    elif len(B) == total:
        if total % 2:
            return B[half]
        else:
            return (B[half] + B[half-1])/2.0


    if len(B) < len(A):
        A, B = B, A

    l, r = 0, len(A)-1
    while True:
        i = (l+r)//2
        j = half - i - 2  #off by one error

        ALeft = A[i] if i >= 0 else float("-inf")
        ARight = A[i+1] if (i + 1) < len(A) else float("inf")
        BLeft = B[j] if j >= 0 else float("-inf")
        BRight = B[j+1] if (j + 1) < len(B) else float("inf")

        #partition is correct
        if ALeft <= BRight and BLeft <= ARight:
            if total % 2:
                return min(ARight, BRight)
            return (max(ALeft, BLeft) + min(ARight, BRight))/2.0
        elif ALeft > BRight:
            r = i - 1
        else:
            l = i + 1

print(findMedianSortedArrays([1,3], [2]))