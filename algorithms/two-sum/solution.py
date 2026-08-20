class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in dict:
                return [dict[needed], i]
            else:
                dict[nums[i]] = i

        