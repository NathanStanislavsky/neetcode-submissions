class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        i = len(temperatures) - 1
        res = [-1] * len(temperatures)

        while i >= 0:
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            
            res[i] = stack[-1] - i if stack else 0

            stack.append(i)

            i -= 1

        return res
