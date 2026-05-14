class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]

        for i in range(1, len(strs)):
            s = strs[i]
            p1, p2 = 0, 0

            while p1 < len(s) and p2 < len(longest) and s[p1] == longest[p2]:
                p1 += 1
                p2 += 1

            longest = longest[:p1]
        
        return longest