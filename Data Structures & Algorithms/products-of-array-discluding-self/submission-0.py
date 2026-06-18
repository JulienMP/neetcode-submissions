class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        n = len(nums)
        i = 1
        j = n-2
        while i < n:
            prefixes[i] = prefixes[i-1] * nums[i-1]
            i += 1
        while j >= 0:
            suffixes[j] = suffixes[j+1] * nums[j+1]
            j -= 1
        for k in range(n):
            output[k] = prefixes[k] * suffixes[k]
        return output