class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        len1, len2 = len(word1), len(word2)
        res = ""

        while l < len1 and r < len2:
            res += word1[l] + word2[r]
            l += 1
            r += 1

        if l < len1:
            res += word1[l:]

        if r < len2:
            res += word2[r:]

        return res