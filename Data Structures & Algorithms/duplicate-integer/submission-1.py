class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums = sorted(nums)
        
        ptr = 0

        for i in range(len(nums) - 1):
            
            j = i + 1

            if nums[j] == nums[i]:
                return True
        
        return False