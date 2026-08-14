class Solution:
    '''
    1. understand
        input: s and t
        output: boolean, if two strings are anagrams return True, otherwise return False
        core logic:
            go through both strings, then put each char in dict --> O(n) 
            if the dict values is all 2, then the two strings are anagrams --> O(1)
        potential edge cases:
            when strings s and t are not the same length

    2. match
        iterating through both strings, then using a frequency map to keep track of the letters
    
    3. plan
        declare dict

        iterate through both strings --> for let in s, t   # if we cannot do this at the same time
                                                           # then i think there must be two for loops
                                                           # or get a helper function to put in dict
            if let not in dict:
                dict[let] = 1
            else:
                dict[let] += 1
        
        iterate through t
            if let not in dict:
                dict[let] = 1
            else:
                dict[let] += 1
        
        iterate through the key, values of each dict
        if a dict has more keys than the other --> return False
        if both dicts key values are not the same --> return False 
        
        return True


        iterate through one string (s)
            record key in dict
        
        iterate through t
            if char not in dict:
                return False
            
            if 


    '''

    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}

        # iterate through both strings
        self.countFreq(s, freqS)
        self.countFreq(t, freqT)
    
        # determine if both keys and values are the same
        if freqT != freqS:
            return False
        
        return True

    def countFreq(self, word: str, freq: dict):
        for let in word:
            if let not in freq:
                freq[let] = 1
            else:
                freq[let] += 1
        