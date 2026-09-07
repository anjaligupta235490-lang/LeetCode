class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        row = 0
        available = n
        required = 1
        while available >= required:
            available -= required
            row += 1
            required += 1
        return row



        