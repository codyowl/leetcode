class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # main formula to do the number for a given alphabe is result = result * 26 + current_value
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = 0
        for character in columnTitle:
            # we are finding index for a given character and adding 1 cause python treats range from 0 
            current_value = alphabet.index(character) + 1
            # main formula
            result = result * 26 + current_value

        return result