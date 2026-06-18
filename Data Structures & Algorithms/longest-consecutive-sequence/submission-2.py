class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        for num in nums:
            lengths.setdefault(num, 1)
        for num in lengths:
            if num - 1 not in lengths:
                consecutive = num + 1
                while consecutive in lengths:
                    lengths[num] += 1
                    consecutive += 1
        return max(lengths.values(), default = 0)
        