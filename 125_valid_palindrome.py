class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        the idea here is simple , iterate all the characters check if it alphanumeric and save it in a varialbe with lowercase eventually reverse it with typical [::-1]
        """
        # here we have used a list instead of straight away string variable which was led to time complexity
        characters = [] 
        for character in s:
            if character.isalnum():
                characters.append(character.lower())
        final_word = "".join(characters)        

        return final_word == final_word[::-1]      