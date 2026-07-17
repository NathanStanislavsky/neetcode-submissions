class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1

        while row_l <= row_r:
            row_m = row_l + (row_r - row_l) // 2

            if matrix[row_m][0] <= target <= matrix[row_m][-1]:
                col_l, col_r = 0, len(matrix[0]) - 1

                while col_l <= col_r:
                    col_m = col_l + (col_r - col_l) // 2

                    if matrix[row_m][col_m] == target:
                        return True
                    elif matrix[row_m][col_m] < target:
                        col_l = col_m + 1
                    else:
                        col_r = col_m - 1

                return False
            elif matrix[row_m][0] > target:
                row_r = row_m - 1
            else:
                row_l = row_m + 1

        return False