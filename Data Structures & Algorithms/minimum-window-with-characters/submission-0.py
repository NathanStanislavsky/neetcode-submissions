class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        t_map = defaultdict(int)
        for char in t:
            t_map[char] += 1

        window_map = defaultdict(int)
        l, r = 0, 0
        formed = 0
        required_chars = len(t_map)
        min_substring = ""
        min_len = float("Inf")

        while r < len(s):
            char_r = s[r]
            window_map[char_r] += 1

            if char_r in t_map and window_map[char_r] == t_map[char_r]:
                formed += 1

            while l <= r and formed == required_chars:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    min_substring = s[l:r+1]

                char_l = s[l]
                window_map[char_l] -= 1
                if char_l in t_map and window_map[char_l] < t_map[char_l]:
                    formed -= 1
                
                l += 1
            r += 1

        return min_substring