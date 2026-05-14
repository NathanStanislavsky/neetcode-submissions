class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
 
        for n, cnt in count.items():
            freq[cnt].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                if len(res) < k:
                    res.append(num)

        return res