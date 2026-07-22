class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums2 = nums

        for i in range (len(nums)):
            if target not in nums:
                nums2 = list.copy(nums)
                nums2.append(target)
                nums2.sort()
        for j in range(len(nums2)):
            if nums2[j] == target:
                return j