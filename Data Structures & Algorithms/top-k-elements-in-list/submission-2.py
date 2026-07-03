class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        heap = [(-v, k) for k, v in freq.items()]

        heapq.heapify(heap)

        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
