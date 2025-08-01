from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(numRows):
            # Start the row with 1
            row = [1]
            if triangle:
                last_row = triangle[-1]
                # Add the sum of pairs from the previous row
                for i in range(1, len(last_row)):
                    row.append(last_row[i - 1] + last_row[i])
                # End the row with 1
                row.append(1)
            triangle.append(row)

        return triangle
