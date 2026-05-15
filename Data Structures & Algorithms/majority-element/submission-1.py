class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1
        
        for k in freq:
            if freq[k] > len(nums)/2:
                return k