class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for n in nums:
            if n - 1 not in num_set:
                streak = 1
                curr = n + 1

                while curr in num_set:
                    streak += 1
                    curr += 1
                
                longest = max(longest, streak)
        
        return longest
