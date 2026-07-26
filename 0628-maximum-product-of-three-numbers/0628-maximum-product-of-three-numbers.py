class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # first = float('-inf')
        # sec = float('-inf')
        # third = float('-inf')

        # for i in range (0,len(nums)):
        #     if nums[i] >= first:
        #         third = sec
        #         sec = first
        #         first = nums[i]
        # if first == 0 or sec == 0 or third == 0:
        #     return 0    
        # else : return first*sec*third
        
        nums.sort()
        return max(
            nums[0]*nums[1]*nums[-1],
            nums[-1]*nums[-2]*nums[-3]
        )