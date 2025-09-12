def numberOfPairs(points) -> int:
    count = 0
    def compare(A, B):
        if A[0] <= B[0] and A[1] >= B[1]:
            for p in points:
                if p != A and p != B and p[0] >= A[0] and p[0] <= B[0] and p[1] <= A[1] and p[1] >= B[1]:
                    return 0
            return 1
        return 0
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            A = points[i]
            B = points[j]

            count += compare(A,B)
            count += compare(B,A)
            
    return count