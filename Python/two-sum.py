class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} #initialize dictionary to store numbers and indicrd
        for i, num in enumerate(nums): #iterate through the array with index abs value
            complement = target - num #calculate the com[lement needed to reach target]
            if complement in num_map: #check if complement exists in dictionary
                return [num_map[complement], i] #if found, return the index of the complement and current index
            num_map[num] = i #if complement is not found, add the current number and index to dictionary
        return [] #if no solution\, return error