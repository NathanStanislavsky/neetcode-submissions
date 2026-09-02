class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def recurse(curr_list, curr_sum, i):
            if curr_sum == target:
                res.append(curr_list)
                return
            
            if curr_sum > target:
                return

            if i == len(nums):
                return

            recurse(curr_list, curr_sum, i + 1)

            new_list = curr_list.copy()
            new_list.append(nums[i])

            recurse(new_list, curr_sum + nums[i], i)
        
        recurse([], 0, 0)
        return res
        

            
            