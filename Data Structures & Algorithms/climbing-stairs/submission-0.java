class Solution {
    public int climbStairs(int n) {
        return dfs(n,0);
    }

    private int dfs(int target, int currentTotal){
        if (currentTotal == target){
            return 1;
        }

        if (currentTotal > target){
            return 0;
        }

        return dfs(target,currentTotal+1) + dfs(target, currentTotal+2);
    }
}
