class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, num in enumerate(nums):

            nado = target - num

            if nado in seen:
                return [seen[nado], i]

            seen[num] = i