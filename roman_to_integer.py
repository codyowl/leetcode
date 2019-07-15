class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_letter_list = [i for i in s]
        roman_dict = {}
        roman_dict["I"] = 1
        roman_dict["V"] = 5
        roman_dict["X"] = 10
        roman_dict["L"] = 50
        roman_dict["C"] = 100
        roman_dict["D"] = 500
        roman_dict["M"] = 1000
        roman_to_int=[roman_dict[value] for value in roman_letter_list]
        i = 0
        int = 0
        while i < len(roman_to_int):
        	r1 = roman_to_int[i]
        	if i+1 < len(roman_to_int):
	        	
	        	r2 = roman_to_int[i + 1]
	        	if r1 >= r2:
	        		int += r1
	        		i += 1
	        	else:
	        		int += r2 - r1
	        		i += 2
	        else:
	        	int += r1
	        	i += 1
        return int		
# sample test cases

t = Solution()
# a = "II"
# a = "IV"
# a = "XIX"
a = "MCMXCIV"
print t.romanToInt(a)        	
# print get_sub_pair_index("MCMXCIV")