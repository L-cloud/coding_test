import java.util.Arrays;
import java.util.Collections;

class Solution {
    public String solution(String s) {
        String[] w = s.split("");
        Arrays.sort(w, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < w.length; i++) {
          sb.append(w[i]);
        }
        return sb.toString();
    }
}
