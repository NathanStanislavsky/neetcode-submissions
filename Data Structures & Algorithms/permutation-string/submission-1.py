class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = defaultdict(int)

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1

        window_freq = defaultdict(int)

        l, r = 0, 0

        while r < len(s1):
            window_freq[ord(s2[r]) - ord('a')] += 1
            r += 1

        r -= 1

        while r < len(s2):
            if s1_freq == window_freq:
                return True

            window_freq[ord(s2[l]) - ord('a')] -= 1

            if window_freq[ord(s2[l]) - ord('a')] == 0:
                del window_freq[ord(s2[l]) - ord('a')]

            l += 1
            r += 1

            if r < len(s2):
                window_freq[ord(s2[r]) - ord('a')] += 1

        return False