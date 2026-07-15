class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sum = 0
        running_sum = []
        for i in range (0,n) :
            sum += nums[i]
            running_sum.append(sum)
        return running_sum