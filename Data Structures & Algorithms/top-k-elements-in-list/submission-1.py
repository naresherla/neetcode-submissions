class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for v in nums:
            count[v] = count.get(v,0)+1
        sorted_frequency = sorted(count.items(),key=lambda x:x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_frequency[i][0])
        return result