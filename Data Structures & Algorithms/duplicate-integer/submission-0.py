class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists=set(nums)
        if len(nums) > len(exists):
            return True
        else:
            return False