class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, j in enumerate(nums):
            if (target-j) in hash_map:
                return [hash_map[(target-j)], i]
            hash_map[j] = i