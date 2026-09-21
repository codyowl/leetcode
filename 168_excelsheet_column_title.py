class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        The idea here is figure out the combinations of the numbers list for appropriate alphabet with the basic math to figure our how many things can be put into how much things
        if there are 17 choclates then 5 choclates can be put into a bag how many bag do we need 
        so 17 % 5 = 3 => three bags can contain the most out of 17
           17 // 5 = 2 => 2 remaining we need to use this for 26 cause there are 26 alphabets
        // → How many complete groups?
        %  → How much remains after making those groups?
        """
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = []
        while columnNumber > 0:
            # we need to reduce column number by one because python treat the index from 0 -25 and we do have 26 alphabets
            columnNumber -= 1
            # we are figuring out how many complete groups
            remainder_index = columnNumber % 26
            result.append(alphabets[remainder_index])
            # figuring out how many remains after the group
            columnNumber //= 26
        #The appending will happen in reverse way so we are reversing the list to presentable way from left to right
        return "".join(reversed(result))