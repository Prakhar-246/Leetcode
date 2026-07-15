class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(0,n):
            ans.append(nums[i])
            
        for i in range(0,n):
            ans.append(nums[i])
        return ans