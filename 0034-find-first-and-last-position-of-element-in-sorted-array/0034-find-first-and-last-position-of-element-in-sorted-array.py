class Solution:
    def lower_bound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        lb = n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb

    def upper_bound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ub = n

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lower_bound(nums, target)
        ub = self.upper_bound(nums, target)

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        return [lb, ub - 1]