class Solution:
    '''
    1. understand
        input: array of integers, numbers sorted in non-decreasing order (with dupes)
        output: return indicies of numbers that can add up to target
        core logic:
            iterate through the list using a two pointer technique --> should be O(n)
                keeping left pointer still until the right is at the end
        
    2. match - two pointer technique, array

    3. plan
        declare both pointers
        left = 0
        right = len(numbers) - 1

        iterate through the list using two pointer technique
        while left elem + right elem != target:
            if right == left + 1:  # fix the next left pointer and restart the process
                left += 1
                right = len(numbers - 1)

            right -= 1

        if left elem + right elem == target:
            return [left, right]
        
        return []             
    '''


    # pitfalls: started off well, but i think i got confused
    # when the problem is asking me for target sum 

    # for a two pointer approach, always put left < right for the while condition.
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # declare both pointers
        left = 0
        right = len(numbers) - 1

        # my approach:
        # # go through the list using two pointer technique
        # while numbers[left] + numbers[right] != target:
        #     if right == left + 1:  # restart process for the next left pointer
        #         left += 1
        #         right = len(numbers) - 1
        #     else:
        #         right -= 1  # continue to the next number

        # if numbers[left] + numbers[right] == target:
        #     return [left+1, right+1]  # due to being 1-indexed
        
        # return []


        # solution that i somewhat understand
        # go through list using two pointer approach
        while left < right:
            currSum = numbers[left] + numbers[right]

            if currSum > target:
                right -= 1
            elif currSum < target:
                left += 1
            else:  # found target
                return [left+1, right+1]
        
        return []  # cannot find target pair

                