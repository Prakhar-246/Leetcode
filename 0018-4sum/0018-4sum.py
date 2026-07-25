class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        my_set = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in seen:
                        quad = [nums[i], nums[j], nums[k], fourth]
                        quad.sort()
                        my_set.add(tuple(quad))

                    seen.add(nums[k])

        return [list(x) for x in my_set]