class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # the main formula is current_row[j] = previous_row[j-1] + previours_row[j]
        """
        there are two rules for pascals triangle
        all the front and alst values of the rows should be 1
        inbetween values should be sum of two numbers above it int he traingle
        """
        triangle = []

        for row_index in range(numRows):
            # for making first and last value as 1
            current_row = [1] * (row_index + 1) 

            # forming preview row with rest of the index apart from 0
            if row_index > 1:
                previous_row = triangle[row_index - 1]
                # using our main formula
                for column_index in range(1, row_index):
                    current_row[column_index] = (previous_row[column_index -1] + previous_row[column_index])
            triangle.append(current_row)  
        return triangle      

