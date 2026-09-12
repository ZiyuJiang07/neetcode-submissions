class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)#为了在后面可以append
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1#把每个字母变成0-25的index，存进count里
            res[tuple(count)].append(s)#list是mutable，不能当map的key，需要先变成tuple；由于是defaultdict，本身每个value都是[]
        return list(res.values())