class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        condition = True
        while condition:
            i = 0
            for word in strs:
                if index >= len(word):
                    condition = False
                    break
                char = strs[0][index]
                if word[index] != char:
                    condition = False
                    break
                i += 1 
                if i == len(strs):
                    index +=1 
        return strs[0][0:index]
        


            
