class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        nums3 = nums1 + nums2
        nums3.sort()

        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        else:
            #print(nums3[len(nums3) // 2],  nums3[len(nums3) // 2 + 1])
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2 ]) / 2  

    