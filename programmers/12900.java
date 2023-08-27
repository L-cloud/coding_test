class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        return  dfs(dp,n);
    }
    public int dfs(int[] dp, int n){
        if(n <= 0) return 0;
        if(dp[n] != 0) return dp[n];
        dp[n] = (dfs(dp,n -1) + dfs(dp,n-2))%1000000007;
        return dp[n];
    }
}
