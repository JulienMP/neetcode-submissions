class Solution:
    def twoSum(self, nums, target):
        diff_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in diff_map:
                return [diff_map[difference], i]
            diff_map[nums[i]] = i