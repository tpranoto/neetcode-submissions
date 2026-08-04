class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl,rowr=0,len(matrix)-1

        selected_r = 0
        while rowl<=rowr:
            mid = (rowl+rowr) //2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                rowl = mid+1
                selected_r = mid
            else:
                rowr = mid-1

        coll,colr = 0,len(matrix[0])-1
        while coll<=colr:
            mid = (coll+colr) //2

            if matrix[selected_r][mid] == target:
                return True
            elif matrix[selected_r][mid] < target:
                coll = mid+1
            else:
                colr=mid-1

        return False