class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map ={}
        for el in nums:
            freq_map[el] = freq_map.get(el, 0) + 1
        sorted_by_value = dict(sorted(freq_map.items(), key=lambda x: -x[1])[:k])
        output = []
        for element in sorted_by_value:
            output.append(element)
            
        return output