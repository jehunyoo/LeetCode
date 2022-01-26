class Solution:
    # python list & set
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

    # binary search: O(nlogn)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        nums2.sort() # O(nlogn)
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1) # O(logn)
            if i2 < len(nums2) and n1 == nums2[i2]:
                result.add(n1)
        
        return result
    
    # two pointers: O(nlogn)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        p1 = p2 = 0
        nums1.sort() # O(nlogn)
        nums2.sort() # O(nlogn)
        
        while p1 < len(nums1) and p2 < len(nums2): # O(2n)
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] == nums2[p2]:
                result.add(nums1[p1])
                p1 += 1
                p2 += 1
        
        return result