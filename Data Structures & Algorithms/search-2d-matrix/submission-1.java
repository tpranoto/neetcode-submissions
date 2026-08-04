class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
        for (int i= matrix.length-1;i>=0;i--){
            if (matrix[i][0]==target){
                return true;
            }

            if (matrix[i][0]<target){
                int left = 0;
                int right = matrix[i].length-1;

                while(left<=right){
                    int mid = (left+right)/2;

                    if (matrix[i][mid]>target){
                        right = mid-1;
                    }else if (matrix[i][mid]<target){
                        left = mid+1;
                    }else{
                        return true;
                    }
                }
            }
        }

        return false;
    }
}
