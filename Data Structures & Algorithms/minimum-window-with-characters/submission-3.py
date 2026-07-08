class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        min_substring_length = float("inf")
        res_l, res_r = 0, 0

        t_freq = defaultdict(int)

        for ch in t:
            t_freq[ch] += 1

        window_freq = defaultdict(int)

        need = len(t_freq)
        have = 0

        l = 0

        for r in range(len(s)):
            window_freq[s[r]] += 1

            if s[r] in t_freq and window_freq[s[r]] == t_freq[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < min_substring_length:
                    min_substring_length = r - l + 1
                    res_l = l
                    res_r = r

                window_freq[s[l]] -= 1

                if s[l] in t_freq and window_freq[s[l]] < t_freq[s[l]]:
                    have -= 1

                l += 1

        if min_substring_length == float("inf"):
            return ""
        else:
            return s[res_l:res_r + 1]

                    

