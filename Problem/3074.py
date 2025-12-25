def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
    capacity.sort(reverse=True)
    summa = sum(apple)
    i = 0
    c = 0
    while c < summa:
        c += capacity[i]
        i += 1
    return i