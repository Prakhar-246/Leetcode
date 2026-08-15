class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        xor = 0
        non_zero = False

        for x in nums:
            xor ^= x
            if x != 0:
                non_zero = True

        if xor != 0:
            return n

        if not non_zero:
            return 0

        return n - 1