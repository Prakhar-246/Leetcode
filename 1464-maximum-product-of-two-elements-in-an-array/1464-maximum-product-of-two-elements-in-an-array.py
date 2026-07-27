class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        sec = 0
        for num in nums:
            if num > first:
                sec = first
                first = num
            elif num > sec :
                sec = num
        return (first-1)*(sec-1)