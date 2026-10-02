class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2
        
        i,j = m-1,n-1
        k= (m+n)-1

        while i > -1 and j > -1:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                k-=1 
                j-=1
            else:
                nums1[k] = nums1[i]
                k-=1
                i-=1
        if j!= -1:
            for ar in range(j+1):
                nums1[ar]=nums2[ar]
        

        



        