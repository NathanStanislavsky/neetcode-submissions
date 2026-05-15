class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        m = len(nums) // 2
        left = self.sortArray(nums[:m])
        right = self.sortArray(nums[m:])

        return self.merge(left, right)

    def merge(self, left, right):
        res = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
            
        res = res + left[i:] + right[j:]

        return res