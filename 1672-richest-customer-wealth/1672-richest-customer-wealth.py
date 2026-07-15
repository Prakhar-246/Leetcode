class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0

        for i in accounts :
            total = 0
            for money in i:
                total += money
            if total > maxSum:
                maxSum = total
            
        return maxSum