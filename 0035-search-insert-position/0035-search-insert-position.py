class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums2 = nums

        # for i in range (len(nums)):
        #     if target not in nums:
        #         nums2 = list.copy(nums)
        #         nums2.append(target)
        #         nums2.sort()
        # for j in range(len(nums2)):
        #     if nums2[j] == target:
        #         return j
        # low = 0 
        # high = len(nums) - 1

        # while low <= high:
        #     mid = (low+high) // 2
        #     if nums[mid] == target :
        #         return mid
        #     elif nums[mid] > target: 
        #         high = mid - 1
        #     else :
        #         low = mid + 1
        # if mid == 0 :
        #     return 0
        # else :
        #     return high-1
        # n = len(nums)
        # ind = -1
        # for i in range (0,n):
        #     if target == 0:
        #         return 0
        #     elif nums [i] == target:
        #         ind  = i
        #     elif nums[i] < target:
        #         ind = i+1
        # return ind
        n = len(nums)
        low = 0
        lb = n
        high = n -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid-1
            else :
                low = mid + 1
        return lb
