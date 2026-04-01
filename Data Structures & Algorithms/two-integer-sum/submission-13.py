class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        N=len(nums)
        
        indexList = []

        
        for i in range(0,N):
            for j in range(i+1,N):                
                if nums[i] + nums[j] ==target:
                    indexList.extend([i,j])

        return indexList
        
        