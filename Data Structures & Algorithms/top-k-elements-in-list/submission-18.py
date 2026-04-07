class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        buckets = [[] for _ in range(len(nums))]
        for key, v in frequencies.items():
            buckets[v - 1].append(key)
        res = []
        for freq_group in buckets[::-1]:
            for num in freq_group:
                res.append(num)
                if len(res) == k:
                    return res




        

