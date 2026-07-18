class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        pos = []
        neg = []
        for i in range (0,n):
            if nums[i] > 0:
              pos.append(nums[i])
            else:
              neg.append(nums[i])
        for i in range (0,len(pos)):
            nums[2*i] = pos[i]
            nums[(2*i)+1] = neg[i]
        return nums