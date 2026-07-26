class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        lp = 1
        for i in range(len(nums)):
            res[i] = lp
            lp *= nums[i]

        rp = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rp
            rp *= nums[i]

        return res