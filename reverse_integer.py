class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		# check for single int
		if len(str(x))>1:
			if x < 0:
				new_num = ''
				converted_num = list(str(x))[::-1][:-1]
				for n in converted_num:
					new_num+=n
				new_num = -int(new_num) 
				
			else:
				new_num = ''
				converted_num = list(str(x))[::-1]
				# check for 0
				if converted_num[-1] == '0':
					for n in converted_num[:-1]:
						new_num+=n
					new_num = int(new_num) 
				else:
					for n in converted_num:
						new_num+=n
					new_num = int(new_num)
					
			# check if the reversed int is signed 32 bit or not		
			if(abs(new_num) > (2 ** 31 - 1)):
				return 0
			else:
				return new_num	 		
		else:
			return x                

s = Solution()
num = -2147483648
print s.reverse(num)
		