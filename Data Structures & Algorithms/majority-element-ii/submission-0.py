class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        heap = [(-value, key) for key, value in freq.items()]

        heapq.heapify(heap)

        res = []
        threshold = len(nums) // 3

        while heap:
            freq, num = heapq.heappop(heap)
            real_freq = -freq

            if real_freq > threshold:
                res.append(num)
            else:
                break

        return res


