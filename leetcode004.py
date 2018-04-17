# coding: utf-8

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(A), len(B)
        if (m > n):
            return Solution().findMedianSortedArrays(B, A)
        iMin, iMax, halfLen = 0, m, int((m + n + 1) / 2)
        while iMin <= iMax:
            i = int((iMax + iMin) / 2)
            j = int(halfLen - i)
            if i < m and j > 0 and B[j - 1] > A[i]:
                iMin = iMin + 1
            elif i > 0 and j < n and A[i - 1] > B[j]:
                iMax = iMax - 1
            else:
                if i == 0:
                    maxLeft = B[j - 1]
                elif j == 0:
                    maxLeft = A[i - 1]
                else:
                    maxLeft = max(A[i - 1], B[j - 1])
                if (m + n) % 2 == 1:
                    return maxLeft

                if i == m:
                    minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(A[i], B[j])
                return (maxLeft + minRight) / 2.0


def test():
    s = Solution()
    num1 = [1,2,2,3]
    num2 = [4,5,6,7,8,9]
    
    rs = s.findMedianSortedArrays(num1,num2)
    print rs

test()