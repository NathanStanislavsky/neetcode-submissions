class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()

        l = 0

        res = 0
        curr = 0

        for r in range(len(s)):
            if s[r] not in window:
                print("grow")
                window.add(s[r])
                curr += 1
                print(l, r, window, curr)
            else:
                res = max(res, curr)
                print("shrink")
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                    curr -= 1

                    print(l, r, window, curr)

                window.add(s[r])
                curr += 1

        return max(res, curr)


