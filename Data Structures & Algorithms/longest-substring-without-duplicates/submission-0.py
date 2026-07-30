class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = {}
        left = 0
        best = 0
        for right in range(len(s)):
            if s[right] in res and res[s[right]] >= left:
                left = res[s[right]] + 1
            res[s[right]] = right
            best = max(best, right-left+1)
        return best