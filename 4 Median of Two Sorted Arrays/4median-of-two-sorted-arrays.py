class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums1) == 0 and len(nums2) == 0:
            return 
        elif len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[(len(nums2)//2 - 1)] + nums2[(len(nums2)//2)]) / 2.0
            else:
                return nums2[len(nums2)//2]
        elif len(nums2) == 0:
            if len(nums1) % 2 == 0:
                return (nums1[(len(nums1)//2 - 1)] + nums1[(len(nums1)//2)]) / 2.0
            else:
                return nums1[len(nums1)//2]

        low = 0
        high = len(nums1)
        while low <= high:
            i = (low + high) // 2
            j = (len(nums1) + len(nums2) + 1) // 2 - i

            if i == 0:
                L1 = float('-inf')
            else:
                L1 = nums1[i-1]
            if i == len(nums1):
                R1 = float('inf')
            else:
                R1 = nums1[i]

            if j == 0:
                L2 = float('-inf')
            else:
                L2 = nums2[j-1]
            if j == len(nums2):
                R2 = float('inf')
            else:
                R2 = nums2[j]

            if L1 <= R2 and L2 <= R1:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(L1, L2)
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                high = i - 1
            else:
                low = i + 1