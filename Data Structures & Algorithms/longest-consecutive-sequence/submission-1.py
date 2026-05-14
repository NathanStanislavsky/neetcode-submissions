class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in num_set:
                streak = 1
                current_num = n

                while current_num + 1 in num_set:
                    streak += 1
                    current_num += 1

                longest = max(longest, streak)

        return longest