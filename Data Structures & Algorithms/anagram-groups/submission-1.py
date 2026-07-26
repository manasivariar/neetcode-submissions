class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        # for s in strs:
        #     key = tuple(sorted(s))
        #     if key not in hash_map:
        #         hash_map[key] = []
        #     hash_map[key].append(s)
        
        # return list(hash_map.values())

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            key = tuple(count)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(s)
        
        return list(hash_map.values())
