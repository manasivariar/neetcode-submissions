class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq = {}

        # if not nums:
        #     return False

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # if max(freq.values()) == 1:
        #     return False
        # else:
        #     return True

        set_nums = set(nums)
        return not len(nums) == len(set_nums)