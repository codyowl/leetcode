class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		prefix_first = []
		if len(strs) == 1:
			for data in strs:
				if len(data)>0:
					return strs[0][0]
				else:
					return ""   

		else:
			none_finder = [data for data in strs if len(data)>0]
			if len(none_finder) != len(strs):
				return ""
			else:	
				for data in strs:
					prefix_first.append(data[0])
				#check whether atelast the first letter is same or not  
				if not len(set(prefix_first)) == 1:
					return ""
				else:
					min_length = min([len(d) for d in strs])
					# truncating the list based on minimum length of words
					trun_list = [data[0:min_length+1] for data in strs]
					prefix_list = []
					# to get all the letters from words
					for i in range(min_length):
						prefix_list.append([data[i] for data in trun_list])
					final_str = ""
					for data in prefix_list:
						if len(set(data)) == 1:
							final_str += data[0]
						else:
							break

					return final_str
			

s = Solution()
# tweaked after seeing this input on test case
# print s.longestCommonPrefix(["", ""])
# # tweaked after seeing this input on test case
# print s.longestCommonPrefix([""])
# # tweaked afet seeing this input on test case
# print s.longestCommonPrefix(["", "b"])
print s.longestCommonPrefix(["abab","aba",""])