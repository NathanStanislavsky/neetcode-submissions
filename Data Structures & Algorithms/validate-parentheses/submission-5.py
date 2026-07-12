class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')' : '(', '}' : '{', ']' : '['}

        stack = []

        for i in range(len(s)):
            if s[i] in close_to_open:
                if not stack or stack[-1] != close_to_open[s[i]]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])
        
        return not stack