class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for n in nums:
        #     count[n] = 1+ count.get(n,0)
        # buckets = []
        # for k,v in count.items():
        #     buckets.append([v,k])
        return [num for num, count in Counter(nums).most_common(k)]
