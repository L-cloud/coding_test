import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        int left = 1;
        int right = 1;
        int s = 0;
        while( right <= n ){
            while(s < n) s += right++;
            while(n < s) s -= left++;
            if(s == n) {
                answer++;
                s -= left++;
            }
        }
        return answer;
    }
}
