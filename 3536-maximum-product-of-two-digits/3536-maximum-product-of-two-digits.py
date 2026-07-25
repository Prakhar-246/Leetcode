class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        sec_largest = 0

        while n > 0:    
            digit = n % 10
            if digit > largest:
                sec_largest = largest
                largest = digit
            elif digit > sec_largest:
                sec_largest = digit
            n = n // 10
        return largest*sec_largest