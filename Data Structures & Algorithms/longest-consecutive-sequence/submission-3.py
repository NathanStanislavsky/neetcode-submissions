class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                streak = 1
                curr = nums[i] + 1

                while curr in num_set:
                    streak += 1
                    curr += 1
                
                res = max(res, streak)
            
        return res