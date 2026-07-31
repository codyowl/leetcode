class Solution:
    def addBinary(self, a: str, b: str) -> str:
        left_side = len(a) - 1
        right_side = len(b) - 1
        carry = 0
        result = []

        while left_side >= 0 or right_side >= 0 or carry:
            total = carry

            if left_side >= 0:
                total += int(a[left_side])
                # moving the pointer to left
                left_side -= 1

            if right_side >= 0:
                total += int(b[right_side])  
                right_side -= 1  

            # modulo and floor division rule
            result.append(str(total % 2)) 
            carry = total // 2
        # we are adding from right to left so reversing
        return "".join(reversed(result))       
