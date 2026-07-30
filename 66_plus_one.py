class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # to make 0 if its 9
            digits[i] = 0

        # finally if everything is 9 we need to add 1
        return [1] + digits        