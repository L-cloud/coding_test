import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        PriorityQueue<int []> pq = new PriorityQueue<>(Comparator.comparing(x -> x[0]));
        int[] ans = new int[numbers.length];
        Arrays.fill(ans, -1);
        int index = 0;
        for(int i : numbers){
            while(!pq.isEmpty() && pq.peek()[0] <i){
                int[] node = pq.remove();
                ans[node[1]] = i;
            }
            pq.add(new int [] {i,index++});
        }
        return ans;
    }
}
