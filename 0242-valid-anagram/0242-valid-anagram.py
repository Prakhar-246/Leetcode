class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        result = {}
        if n != m:
            return False
        for char in s:
            result[char] = result.get(char, 0) + 1
        for char in t:
            if char not in result:
                return False
            result[char] -= 1
            if result[char] < 0:    
                return False
        return True