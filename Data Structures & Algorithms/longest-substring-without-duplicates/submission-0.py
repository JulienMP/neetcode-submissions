class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        left = 0
        best = 0
        k = 0
        for right, ch in enumerate(s):
            sub[ch] = sub.get(ch, 0) + 1
            k += 1
            while len(sub) < k:
                sub[s[left]] -= 1
                k -= 1
                if sub[s[left]] == 0:
                    del sub[s[left]]
                left += 1
            best = max(best, right-left+1)
        return best

        