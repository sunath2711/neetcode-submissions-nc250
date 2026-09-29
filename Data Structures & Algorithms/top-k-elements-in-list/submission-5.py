class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        my_map = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in  my_map:
                my_map[nums[i]] += 1
            else:
                my_map[nums[i]] = 1
        
        buckets = [[] for _ in range(n+1)]

        for num,freq in my_map.items():
            buckets[freq].append(num)

        res = []
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        