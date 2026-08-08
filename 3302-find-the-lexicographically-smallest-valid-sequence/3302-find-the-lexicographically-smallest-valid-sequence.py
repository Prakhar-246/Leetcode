class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # dp[i] = how many characters from the end of word2
        # can be matched exactly using word1[i:]
        dp = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                dp[i] += 1
                j -= 1

        # Greedily build the answer
        ans = []
        j = 0
        used_mismatch = False

        for i in range(n):

            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one mismatch
            elif not used_mismatch:
                # After choosing i, we need to match
                # word2[j+1:] from word1[i+1:]
                remaining = m - (j + 1)

                if dp[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        if len(ans) == m:
            return ans

        return []