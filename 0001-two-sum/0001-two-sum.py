class Solution:
    def twoSum(self, nums, target):
        seen_numbers = {}
        
        for index, value in enumerate(nums):
            complement = target - value
            
            if complement in seen_numbers:
                return [seen_numbers[complement], index]
            seen_numbers[value] = index
            
        return []
