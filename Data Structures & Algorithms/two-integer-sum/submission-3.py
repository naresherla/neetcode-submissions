class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for v in range(len(nums)):
            for j in range(v+1,len(nums)):
                if nums[v]+nums[j] == target:
                    return [v,j]