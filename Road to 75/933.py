class RecentCounter(object):

    def __init__(self):
        self.L = []
        return

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.L.append(t)
        while self.L[0] < t - 3000: 
            self.L.pop(0)
        return len(self.L)
                


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)