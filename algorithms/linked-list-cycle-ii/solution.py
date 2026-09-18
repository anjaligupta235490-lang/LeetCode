class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # row = 0
        # available = n
        # required = 1
        # while available >= required:
        #     available -= required
        #     row += 1
        #     required += 1
        # return row
        low = 1
        high = n
        while low <= high:
            mid = (low + high)//2
            required = mid*(mid+1)//2
            if required <= n:
                low = mid + 1
            else:
                high = mid - 1
        return high




        