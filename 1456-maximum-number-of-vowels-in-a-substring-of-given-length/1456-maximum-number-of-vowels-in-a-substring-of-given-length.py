class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0 
        vowels = 'aeiou'
        count = 0
        maximum = 0
        for right in range (len(s)):
            if s[right] in vowels:
                count += 1
            if right - left +1 == k:
                maximum = max(count,maximum)
                if s[left] in vowels:
                    count -= 1
                left += 1
        return maximum