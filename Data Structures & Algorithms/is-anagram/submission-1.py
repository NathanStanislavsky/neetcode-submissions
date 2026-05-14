class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)

        for ch in s:
            freq[ch] += 1
         
        for ch in t:
            freq[ch] -= 1

        for f in freq.values():
            if f != 0:
                return False

        return True