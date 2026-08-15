class Solution:
    '''
    1. understand
        input: string s
        output: boolean, if it is palindrome --> True, otherwise False
        note: case-insensitive, the function only considers numbers and letters
            but ignores all non-alphanumeric chars, so string s can have these chars
        core logic:
            make string s contain no non-alphanumeric chars
            use two pointers technique (left and right)
                if left and right is not equal, return False
                while loop ends when left >= right? 
    
    2. match 
        two pointers

    3. plan
        iterate through s to determine if s has non-alphanumeric char
        ext_s = ""
        for char in s:
            if char.isalnum():
                extracted_s += char 

        declare left and right pointers
        left = 0
        right = len(ext_s)-1

        iterate through s until reaching to the halfway point --> while left >= right
            if ext_s[left] != ext_s[right]:
                return True
            
            left += 1
            right -= 1
    '''

    # Hints needed:
        # asked Gemini for the isalnum() function to get rid of non-alphanumeric chars
        # obtained 2 hints --> for the while loop condition (forgotten about this, and did the opposite)
        #                      for the .lower() because my brain thought insensitive meant SENSITIVE

    # overall:
        # needed help for a function
        # need to practice more two pointers (which i am!)
        # and little more comprehending skills

    def isPalindrome(self, s: str) -> bool:
        # iterate through s to determine if s has non-alphanumeric char
        ext_s = ""
        for char in s:
            if char.isalnum():
                ext_s += char.lower() 

        # declare left and right pointers
        left = 0
        right = len(ext_s)-1

        # iterate through s until reaching to the halfway poin
        while left < right:
            if ext_s[left] != ext_s[right]:
                return False
            
            left += 1
            right -= 1
    
        return True
        