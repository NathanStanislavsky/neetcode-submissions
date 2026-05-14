class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[nums[i]] = i