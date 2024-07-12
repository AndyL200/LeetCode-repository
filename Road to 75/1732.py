class Solution(object):
    def largestAltitude(self, gain):
        maxi = 0
        s = 0
        for i in gain:
            s += i
            if s > maxi:
                maxi = s
        return maxi
        