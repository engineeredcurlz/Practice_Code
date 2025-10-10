class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} #initialize dictionary to store numbers and indices. dictionsry will store number in nums as a key and index as the value
        for i, num in enumerate(nums): #iterate through the array with index and value. loop iterates through nums list, providing index i and value num 
            complement = target - num #calculate the com[lement needed to reach target. for each num, the complement needed to reach the target is calculated
            if complement in num_map: #check if complement exists in dictionary. check if complement exists in key num_map. if it does, we found the two numbers tghat sum to target
                return [num_map[complement], i] #if found, return the index of the complement and current index
            num_map[num] = i #if complement is not found, add the current number and index to dictionary. prepares for future lookups
        return [] #if no solution, return error