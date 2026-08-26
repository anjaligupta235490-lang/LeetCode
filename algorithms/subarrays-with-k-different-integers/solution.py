class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        total = sum(cardPoints)
        window = n-k
        min_sum = sum(cardPoints[:window])
        curr_sum = min_sum
        for i in range(window, n):
            curr_sum = (curr_sum - cardPoints[i-window]) + cardPoints[i]
            min_sum = min(min_sum, curr_sum)
        return total - min_sum
        