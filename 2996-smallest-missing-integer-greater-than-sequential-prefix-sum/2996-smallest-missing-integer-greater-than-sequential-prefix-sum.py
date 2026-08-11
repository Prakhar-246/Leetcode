class Solution:
    def missingInteger(self, nums):
        
        # Step 1: Find sum of longest sequential prefix
        total = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        
        # Step 2: Put all elements in set
        s = set(nums)
        
        # Step 3: Find first missing number
        while total in s:
            total += 1
        
        return total