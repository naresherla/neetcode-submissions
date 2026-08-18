class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for v in nums:
            if v not in seen:
                seen.append(v)
            else:
                return True
        return False
        