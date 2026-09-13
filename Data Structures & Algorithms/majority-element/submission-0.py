class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #may assume that the majority element always exists in the array
        count = dict()
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    
            
        for num, freq in count.items():
            if freq > (len(nums)/2):
                return num
        
        return 1