class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = sorted(nums1)
        list2 = sorted(nums2)
        list3 = []
        
        for i in list2:
            if i in list1:
                list3.append(i)
                list1.remove(i)
        return list3
