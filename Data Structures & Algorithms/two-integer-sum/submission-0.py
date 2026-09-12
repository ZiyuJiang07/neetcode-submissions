class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        hashMap = {}
        while i < len(nums):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            hashMap[nums[i]] = i
            i += 1
        


