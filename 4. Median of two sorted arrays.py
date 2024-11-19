class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newnums = nums1 + nums2
        newnums.sort()
        if len(newnums) % 2 == 0:
            hlength = len(newnums) // 2
            x = newnums[hlength]
            y = newnums[hlength-1]
            return (x + y) / 2
        else:
            hlength = len(newnums) // 2
            return newnums[hlength]
            #return hlength
