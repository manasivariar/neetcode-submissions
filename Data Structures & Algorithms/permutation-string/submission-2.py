class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1_freq, s2_freq = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_freq[ord(s1[i])-ord('a')]+=1
            s2_freq[ord(s2[i])-ord('a')]+=1

        matches = 0
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches+=1

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2_freq[index] += 1
            if s1_freq[index] == s2_freq[index]:
                matches += 1
            elif s1_freq[index] + 1 == s2_freq[index]:
                matches -= 1
            
            index = ord(s2[r - len(s1)]) - ord('a')
            s2_freq[index] -= 1
            if s1_freq[index] == s2_freq[index]:
                matches += 1
            elif s1_freq[index] - 1 == s2_freq[index]:
                matches -= 1

        return matches == 26
        


        



        
        