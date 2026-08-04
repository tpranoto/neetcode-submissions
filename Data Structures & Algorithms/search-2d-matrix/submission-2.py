class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l_m,r_m = 0, len(matrix)-1
        l_n,r_n = 0, len(matrix[0])-1
        
        selected_row = -1
        while l_m <= r_m:
            mid_m = (l_m+r_m) //2
            if target < matrix[mid_m][l_n]:
                r_m = mid_m -1
            elif target > matrix[mid_m][r_n]:
                l_m = mid_m +1
            else:
                selected_row = mid_m
                break
        
        if selected_row == -1:
            return False
        
        while l_n <= r_n:
            mid_n = (l_n + r_n) //2
            if target > matrix[selected_row][mid_n]:
                l_n = mid_n + 1
            elif target < matrix[selected_row][mid_n]:
                r_n = mid_n - 1
            else:
                return True

        return False