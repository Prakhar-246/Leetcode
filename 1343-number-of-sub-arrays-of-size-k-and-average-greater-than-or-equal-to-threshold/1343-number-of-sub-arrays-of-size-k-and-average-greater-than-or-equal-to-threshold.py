class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        left = 0
        current = 0

        for right in range (len(arr)):
            current += arr[right]
            if right - left + 1 == k:
                average = current / k
                if average >= threshold:
                    count+=1
                current -= arr[left]
                left += 1

        return count