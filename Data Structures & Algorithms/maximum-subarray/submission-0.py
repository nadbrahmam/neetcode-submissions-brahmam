class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        N=len(nums)
        sumvalue=0
        maxvalue=float('-inf')
        start = 0
        l_index = -1
        r_index = -1
        for i in range(N):
            if sumvalue > 0:
                sumvalue += nums[i]

            else:
                sumvalue = nums[i]
                start = i
            
            if sumvalue > maxvalue:
                maxvalue = sumvalue
                l_index = start
                r_index = i
        
        return maxvalue