class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        candidates = self.store[key]

        l, r = 0, len(candidates) - 1

        res = ""

        while l <= r:
            m = l + (r - l) // 2

            time = candidates[m][0]

            if time <= timestamp:
                res = candidates[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res

