class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_index = {num : i for i, num in enumerate(nums1)}
        result = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] >stack[-1]:
                index = nums1_index[stack.pop()]
                result[index] = nums2[i]
            if nums2[i] in nums1_index:
                stack.append(nums2[i])

        return result