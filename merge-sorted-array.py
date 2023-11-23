class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #nums1 index
        i = m-1
        #nums2 index
        j = n-1

        #to store last index in nums1
        k = m+n-1

        while j>=0:
            if i>=0 and nums1[i]> nums2[j]:
                nums1[k]=nums1[i]
                k-=1
                i-=1
            else:
                nums1[k]=nums2[j]
                k-=1
                j-=1
