def multiply(self, num1: str, num2: str) -> str:
        def toInt(char):
            match char:
                case '0': return 0
                case '1': return 1
                case '2': return 2
                case '3': return 3
                case '4': return 4
                case '5': return 5
                case '6': return 6
                case '7': return 7
                case '8': return 8
                case '9': return 9
                case _: return -1
        n1 = 0
        d = 0
        for i in range(len(num1)-1, -1, -1):
            n1 += toInt(num1[i]) * 10**d
            d += 1
        n2 = 0
        d = 0
        for i in range(len(num2)-1,-1,-1):
            n2 += toInt(num2[i]) * 10**d
            d += 1

        return str(n1 * n2)