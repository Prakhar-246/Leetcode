class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()                      # Two pointer ke liye sorting zaruri hai
        ans = []
        n = len(nums)

        for i in range(n):
        
            # Duplicate first element skip karo
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]

                if total_sum < 0:
                    j += 1

                elif total_sum > 0:
                    k -= 1

                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Duplicate second element skip karo
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Duplicate third element skip karo
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans
        # n = len(nums)
        # result = set()
        # for i in range (0,n):
        #     my_set = set()
        #     for j in range (i+1,n):
        #         third = -(nums[i]+nums[j])
        #         if third in my_set:
        #             temp = [nums[i],nums[j],third]
        #             temp.sort()
        #             result.add(tuple(temp))
        #         my_set.add(nums[j])
        # p = [list(ans) for ans in result]
        # return p
