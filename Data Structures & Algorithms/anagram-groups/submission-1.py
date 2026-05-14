class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            freq_s = [0] * 26

            for ch in s:
                freq_s[ord(ch) - ord('a')] += 1

            res[tuple(freq_s)].append(s)
        
        return list(res.values())