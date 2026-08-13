class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        n = len(numbers)
        left = 0
        right = n-1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                result.append(left+1)
                result.append(right+1)
                break
            elif sum > target:
                right = right - 1
            elif sum < target:
                left = left + 1

        return result