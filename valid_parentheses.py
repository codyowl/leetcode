class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		p_dict = {}
		stack = []
		p_dict["}"] = "{"
		p_dict["]"] = "["
		p_dict[")"] = "("

		for data in s:
			if data in p_dict.values():
				stack.append(data)
			elif data in p_dict.keys():
				if stack == [] or p_dict[data] != stack.pop():
					return False
			else:
				return False
		return stack == []			



		
		
					


# b = "()"
b = "{{}]"
# b = "([)]"
# b = "(["
s = Solution()
print s.isValid(b)            