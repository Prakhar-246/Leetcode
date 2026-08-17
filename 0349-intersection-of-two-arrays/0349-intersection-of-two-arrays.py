class Solution:

    def list_one(self, nums1, nums2, n, m):
        result = set()

        for i in range(m):
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if nums1[mid] == nums2[i]:
                    result.add(nums2[i])
                    break

                elif nums1[mid] < nums2[i]:
                    left = mid + 1

                else:
                    right = mid - 1

        return list(result)

    def list_two(self, nums1, nums2, n, m):
        result = set()

        for i in range(n):
            left = 0
            right = m - 1

            while left <= right:
                mid = (left + right) // 2

                if nums2[mid] == nums1[i]:
                    result.add(nums1[i])
                    break

                elif nums2[mid] < nums1[i]:
                    left = mid + 1

                else:
                    right = mid - 1

        return list(result)

    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        if n > m:
            return self.list_one(nums1, nums2, n, m)
        else:
            return self.list_two(nums1, nums2, n, m)