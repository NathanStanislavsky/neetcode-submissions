class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {']': '[', '}': '{', ')': '('}

        stack = []

        for i in range(len(s)):
            char = s[i]

            if char in close_to_open:
                if not stack:
                    return False
                elif stack[-1] != close_to_open[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        if not stack:
            return True
        
        return False