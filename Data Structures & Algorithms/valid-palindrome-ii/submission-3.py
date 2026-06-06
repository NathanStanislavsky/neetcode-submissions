class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(l, r):
            while l <= r:
                while l < r and not s[l].isalnum():
                    l += 1

                while l < r and not s[r].isalnum():
                    r -= 1

                if s[l].lower() != s[r].lower():
                    return False

                l += 1
                r -= 1

            return True

        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return is_palindrome_range(l, r - 1) or is_palindrome_range(l + 1, r)
            
            l += 1
            r -= 1
            
        return True

