class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freq = defaultdict(int)
        most_freq = ''

        res = 0

        l = 0

        for r in range(len(s)):
            window_freq[s[r]] += 1

            print(window_freq)
            
            if window_freq[s[r]] >= window_freq[most_freq]:
                most_freq = s[r]

            while (r - l + 1) - window_freq[most_freq] > k:
                
                window_freq[s[l]] -= 1

                if s[l] == most_freq and window_freq[s[l]] < window_freq[s[r]]:
                    most_freq = s[r]

                l += 1

            res = max(res, r - l + 1)

        return res

                            