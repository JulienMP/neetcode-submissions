from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Step 3: Fill buckets
        for num, count in freq.items():
            buckets[count].append(num)

        # Step 4: Traverse from high frequency to low
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result