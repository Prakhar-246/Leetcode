class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        current = 0
        maxi = float('-inf')

        for right in range (len(nums)):
            current += nums[right]
            # current = current // k
            if right - left + 1 == k:
                maxi = max(maxi,current)
                max_average = maxi/k
                current -= nums[left]
                left += 1
        return max_average