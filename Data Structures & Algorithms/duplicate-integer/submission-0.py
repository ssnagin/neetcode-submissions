class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setted = set(nums)

        if len(nums) - len(setted) != 0:
            return True

        return False