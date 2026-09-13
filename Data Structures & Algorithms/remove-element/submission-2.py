class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = len(nums) - 1
        index = 0
        while index <= last:
            if nums[index] == val:
                nums[index] = nums[last]
                nums[last] = val
                index -= 1
                last -= 1
            index += 1
        return last + 1

                