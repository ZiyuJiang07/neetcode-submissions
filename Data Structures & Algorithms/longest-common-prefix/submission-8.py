class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        basecase = strs[0]
        for index in range(0, len(basecase)):
            for word in strs:
                if index == len(word) or word[index] != basecase[index]:
                    return answer
            answer += basecase[index]
        return answer
