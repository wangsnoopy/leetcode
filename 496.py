class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #find index, num[i] == num[j]
        #find next greater of num[j], if not return -1
        result = []
        l = len(nums2)
        for i in nums1:
            # find i in which index in nums2
            num_index = nums2.index(i)
            # iterate ele after num_index
            for j in range(num_index, l):
                # there is next great ele, break
                if nums2[j] > i:
                    result.append(nums2[j])
                    break
            # after iterate all ele, no great, add -1
            else:
                    result.append(-1)
        return result