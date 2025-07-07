def squareIsWhite(self, coordinates: str) -> bool:
    f = ord(coordinates[0])-ord('b')
    s = int(coordinates[1])
    if f % 2 == s % 2:
        return False
    return True