class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(reverse=True)

        stack = []

        for p, s in combined:
            time = (target - p) / s

            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)

        return len(stack)