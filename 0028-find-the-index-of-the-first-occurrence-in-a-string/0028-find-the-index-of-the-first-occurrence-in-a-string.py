class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        ind = -1
        isfound = False
        for i in range(0,n):
            check = ""
            for j in range(i,n):
                check = check + haystack[j]
                if needle == check:
                    ind = i
                    isfound = True
            if isfound:
                break
        return ind


