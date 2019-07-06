class Solution(object):
    def twoSum(self, nums, target):
        elements_list = []
        if len(nums) ==2:
            return 0, 1
        for i in range(len(nums)):
            elements = [data for data in nums if nums[i] + data == target]
            if elements:
                elements_list.append((nums[i], elements[0]))
        print elements_list        
        
        # # to remove same element
        if len(elements_list)==2:
            if elements_list[0]==elements_list[1]:
                print elements_list
                return [index for index, char in enumerate(nums) if char == elements_list[0][0]]
            else:        
                return nums.index(elements_list[0][0]), nums.index(elements_list[0][1])
        else:
            nums_duplicates_removed=[data for data in elements_list if not data[0]==data[1]]
            return nums.index(nums_duplicates_removed[0][0]), nums.index(nums_duplicates_removed[0][1])        
        
     
                

# nums = [2,7,11,15]
nums = [3,2,4]

target = 6

s = Solution()
print s.twoSum(nums, target)                