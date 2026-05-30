class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] -= 1

        heap = [(val, key) for key, val in freq.items()]
        heapq.heapify(heap)

        res = []
        while heap and k != 0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1

        return res




        