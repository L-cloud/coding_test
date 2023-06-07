class Solution {
    public int solution(int n) {
        int ans = 2;
        while (n % ans != 1) ans ++;
        return ans;
    }
}
