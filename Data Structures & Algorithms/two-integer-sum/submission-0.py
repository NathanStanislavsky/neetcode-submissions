class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_set:
                return [num_set[complement], i]
            
            num_set[nums[i]] = i