class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, current_sum, total):
            if total == target:
                res.append(current_sum.copy())
                return
            if i >= len(nums) or total > target:
                return

            current_sum.append(nums[i])
            backtrack(i, current_sum, total + nums[i])
            current_sum.pop()
            backtrack(i + 1, current_sum, total)

        backtrack(0, [], 0)
        return res
