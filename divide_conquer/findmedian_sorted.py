class Solution:
    def findMedian(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        mid = (len1+len2) / 2
        if (len1+len2) % 2 == 1:
            return self.findKth(nums1, nums2, mid+1)
        else:
            return self.findKth((nums1, nums2, mid) + self.findKth(nums1, nums2, mid+1))/2
        
    
    def findKth(self, A, B, k):
        len1 = len(A)
        len2 = len(B)
        if len1 > len2:
            return self.finKth(B,A,k)
        if len1 == 0:
            return B[k-1]
        if k == 1:
            return min(A[0], B[0])
        pa = min(len1, k/2)
        pb = k - pa
        if A[pa-1] <= B[pb-1]:
            return self.findKth(A[pa:], B, pb)
        else:
            return self.finKth(A, B[pb:], pa)
