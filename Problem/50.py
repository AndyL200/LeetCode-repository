def myPow(self, x: float, n: int) -> float:
    def myPow_tailwise(x, n, acc=1):
        if n == 0:
            return acc
        elif n < 0:
            return myPow_tailwise(1/x, -n, acc)
        elif n % 2 == 0:
            return myPow_tailwise(x*x, n//2, acc)
        else:
            return myPow_tailwise(x*x, n//2, acc*x)

    return myPow_tailwise(x,n)
