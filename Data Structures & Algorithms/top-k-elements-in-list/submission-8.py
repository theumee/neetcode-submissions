class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1+ count.get(n,0)
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key,value in count.items():
            buckets[value].append(key)

        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                res.append(val)
                if len(res) == k: return res
        return res
         
