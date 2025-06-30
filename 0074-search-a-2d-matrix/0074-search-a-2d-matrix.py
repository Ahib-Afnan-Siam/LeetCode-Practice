class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get dimensions of the matrix
        m = len(matrix)
        if m == 0:
            return False  # Handle empty matrix case
        n = len(matrix[0])
        if n == 0:
            return False  # Handle empty rows case

        # Initialize the binary search pointers for the conceptual 1D array
        # 'left' is the index of the first element (0)
        # 'right' is the index of the last element (m*n - 1)
        left, right = 0, (m * n) - 1

        while left <= right:
            # Calculate the middle index of the conceptual 1D array
            # Using (right - left) // 2 helps prevent potential integer overflow
            mid = left + (right - left) // 2

            # Convert the 1D 'mid' index to 2D (row, col) coordinates
            mid_row = mid // n
            mid_col = mid % n

            # Get the value at the calculated 2D coordinates
            current_value = matrix[mid_row][mid_col]

            # Compare the current_value with the target
            if current_value == target:
                return True  # Target found
            elif current_value < target:
                # If the current value is less than the target,
                # the target must be in the right half of the conceptual array.
                left = mid + 1
            else:
                # If the current value is greater than the target,
                # the target must be in the left half of the conceptual array.
                right = mid - 1

        # If the loop finishes, the target was not found in the matrix
        return False