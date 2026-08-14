class Solution:
    '''
    1. understand
        input: array of integers nums and integer target
        output: a list of the indicies of two numbers that equals to the target AND that i != j
        core logic: iterate through the array using two pointers   
            left: the first index
            right: iterates one element each time until right = length of list
        edge cases: if last elem isn't the pair
    
    2. match
        two pointers, iterating through array
    
    3. plan
        declare left and right
        left = 0
        right = 1

        iterate through the list
        while left + right != target :
            right += 1

            if right == len - 1:  # if the iteration reached to the last elem, then we haven't found a pair
                left += 1
                right = left + 1
        
        return [left, right]
            
                
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # declare left and right
        left = 0
        right = 1

        # iterate through the list
        while nums[left] + nums[right] != target:
            # otherwise, iterate 
            right += 1
            # print("Before: " + "[" + str(left) + "," + str(right) + "]")
            
            # if the iteration reached to the last elem, 
            # then we haven't found a pair
            if right == len(nums) - 1 and nums[left] + nums[right] != target:
                left += 1
                right = left + 1
                # print("After: " + "[" + str(left) + "," + str(right) + "]")

        
        return [left, right]
        