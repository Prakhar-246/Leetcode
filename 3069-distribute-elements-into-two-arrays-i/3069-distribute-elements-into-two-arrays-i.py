class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = []
        arr1.append(nums[0])
        arr2 = []
        arr2.append(nums[1])
        # print(arr1,arr2)

        for i in range(2,n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        arr1n = len(arr1)
        arr2n = len(arr2)
        result = []

        for i in range (arr1n):
            result.append(arr1[i])

        for i in range (arr2n):
            result.append(arr2[i])
        return result