class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_minus = float("-inf")
        
        for i in range (0,n-1):
            minus = 0
            for j in range (0,n):
                minus = nums[j] - nums[i]
                if minus > max_minus:
                    if i<j:
                        max_minus = max(minus,max_minus)
                if max_minus<=0:
                    max_minus = -1
                
        return max_minus