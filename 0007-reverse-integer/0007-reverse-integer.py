class Solution:
    def reverse(self, x: int) -> int:
        xLess = False

        if x < 0:
            xLess = True

        x = abs(x)
        reverse = 0

        while x != 0:
            digit = x % 10
            reverse = (reverse * 10) + digit
            x = x // 10

        if xLess:
            reverse = reverse * -1

        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0

        return reverse