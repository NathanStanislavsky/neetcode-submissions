class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = 0, 0, len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                self.swap(i, l, nums)
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                self.swap(i, r, nums)
                r -= 1
            
    def swap(self, i, j, nums):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
