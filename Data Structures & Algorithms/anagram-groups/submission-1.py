class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in ana_map:
                ana_map[key] = []
            ana_map[key].append(s)
        return list(ana_map.values())

