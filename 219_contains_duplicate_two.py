class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # the idea here is to create a dictionary and update it with the key as the nums list item and value as its index, we are iterating the elements and when an index found in the dicitonary we are checking the thumb rule i - j <=k else we are updating the dictionar with number as key and theindex as its value 
        seen_dict = dict()
        for current_index in range(len(nums)):
            # taking one element from the list
            number = nums[current_index]
            # checking if the number present in our seen dict 
            if number in seen_dict:
                # considering that as last occurence
                previous_index = seen_dict[number]
                # checking the thumb rule i - j <=k
                if current_index - previous_index <= k:
                    return True
            # just updating the dictionary with the number and its index as key and value for next iteration 
            seen_dict[number] = current_index
        # when no number got into seen_dict matching condition
        return False