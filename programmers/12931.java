import java.util.*;

public class Solution {
    public int solution(int n) {
        String s=String.valueOf(n);
        int ans = 0;
        for (char ch : s.toCharArray()) {
            ans += Character.getNumericValue(ch);
        }
        return ans;
    }
}
