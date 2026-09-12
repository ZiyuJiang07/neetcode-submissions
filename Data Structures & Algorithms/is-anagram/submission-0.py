class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = dict()
        s2 = dict()
        #populate char-occurance pair into maps
        for i in range(len(s)):
            if s[i] in s1:
                s1[s[i]] += 1
            else:
                s1[s[i]] = 1
        for j in range(len(t)):
            if t[j] in s2:
                s2[t[j]] += 1
            else:
                s2[t[j]] = 1
        #compare
        for char, occurance in s1.items():
            if char not in s2:
                return False
            if s2[char] != occurance:
                return False
        for char, occurance in s2.items():
            if char not in s1:
                return False
            if s1[char] != occurance:
                return False

        return True
            
