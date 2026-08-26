class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # same formula for pascal triangle 1
        # oth index will be 1 so initiating that as previos row
        previous_row = [1]

        # now iterating till the give rowindex plus 1
        for row_number in range(1, rowIndex + 1):
            # forming the list value by multiplying it by [1] 
            current_row = [1] * (row_number + 1)
            # here apllying our formula to iterate inside the list an change
            for column_index in range(1,row_number):
                current_row[column_index] = (previous_row[column_index - 1] + previous_row[column_index])

            previous_row = current_row

        return previous_row
