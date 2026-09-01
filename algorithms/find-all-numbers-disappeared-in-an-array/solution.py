class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i] -1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        arr = []

        for i in range(n):
            if nums[i] != i+1:
                arr.append(i+1)
        return arr


        