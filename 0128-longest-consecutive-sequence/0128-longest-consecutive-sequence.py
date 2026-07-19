class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # n = len(nums)
        # max_count = 0
        # for i in range (0,n):
        #     current = nums[i]
        #     count = 1
        #     while current+1 in nums:
        #         count +=1
        #         current = current+1
        #     if count>max_count:
        #         max_count = count
        # return max_count
        num_set = set(nums)    
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest