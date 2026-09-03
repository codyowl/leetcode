class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # the idea here is to created a dictionary with the numbers as key and its occurence as its value
        occurence_dict = dict()
        for number in nums:
            # re iterating the dict again , if its not there the cound will be 1 else it will keep on adding eventuall the key with value 1 will be treated as unique
            occurence_dict[number] = occurence_dict.get(number,0) + 1
        
        for number, value in occurence_dict.items():
            if value == 1:
                return number