import java.util.*;
class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets, Comparator.comparingInt((int[] x) -> x[1])
                .thenComparingInt((int[] x) -> x[0]));
        // right가 작은 순으로 정렬
        int left,right;
        int answer = 1;
        right = targets[0][1];
        int m_r = targets[0][1];
        for (int[] t : targets){
             m_r = (t[1] < m_r) ? m_r : t[1];
            if (t[0] >= right) {
                answer++;
                right = m_r;
            }
        }
        return answer;
    }
}
