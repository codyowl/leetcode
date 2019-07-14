class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        index_list = []
        for i in range(len(arr2)):
        	index_list.append([index for index, value in enumerate(arr1) if value==arr2[i]])
        relative_list = []
        for i in range(len(index_list)):
        	for j in index_list[i]:
        		relative_list.append(arr1[j])
        remaining_elements = sorted([a1 for a1 in arr1 if a1 not in arr2])
        return relative_list + remaining_elements				


s = Solution()
arr1 = [2,3,1,3,2,4,6,7,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print s.relativeSortArray(arr1, arr2)