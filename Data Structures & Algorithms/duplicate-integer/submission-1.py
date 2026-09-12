class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        hashset = set()
        while i < len(nums):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
            i += 1
        return False

