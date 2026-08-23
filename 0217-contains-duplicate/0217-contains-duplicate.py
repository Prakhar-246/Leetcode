class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        is_Duplicate = False
        for i in range (len(nums)):
            if nums[i] in nums_dict:
                is_Duplicate = True
                break
            else :
                nums_dict[nums[i]] = 1
        return is_Duplicate