class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = {}
        # ls = []
        # for key in nums:
        #     freq[key] = freq.get(key, 0) + 1

        # sorted_dict = sorted(freq.items(), key=lambda index:index[1], reverse=True)
        # print(sorted_dict)

        # for i in range(k):
        #     ls.append(sorted_dict[i][0])
        
        # return ls


        freq = {}
        buckets = [[] for i in range(len(nums)+1)]

        result = []
        for key in nums:
            freq[key] = freq.get(key, 0) + 1

        for key,v in freq.items():
            buckets[v].append(key)

        for i in range(len(buckets)-1, -1, -1):
            for j in buckets[i]:
                result.append(j)
                if len(result) == k:
                    return result
                



        
        