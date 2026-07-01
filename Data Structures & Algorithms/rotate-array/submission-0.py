class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        count = 0
        start = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                next_i = (current + k) % n

                tmp = nums[next_i]
                nums[next_i] = prev
                prev = tmp

                current = next_i
                count += 1

                if current == start:
                    break
            start += 1
