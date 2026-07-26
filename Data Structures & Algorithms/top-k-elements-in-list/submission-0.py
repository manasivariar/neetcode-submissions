class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ls = []
        for key in nums:
            freq[key] = freq.get(key, 0) + 1

        sorted_dict = sorted(freq.items(), key=lambda index:index[1], reverse=True)
        print(sorted_dict)

        for i in range(k):
            ls.append(sorted_dict[i][0])
        
        return ls

        