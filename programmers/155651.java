/*
최소한의 객실 이용해서 손님
퇴실 시간을 기준으로 10분간 청소 해야함.
필요한 최소 객실의 수

-> 어떻게 방을 조정할 것인가... 
일단 시간대를 편하게 하기 위해 String -> Int 배열로 변경해준다.
*/
import java.util.*;
class Solution {
    public int solution(String[][] book_time) {
        int[][] arr = new int[book_time.length][2];
        for(int i= 0; i < arr.length; i ++) arr[i] = change(book_time[i]);
        Arrays.sort(arr,Comparator.comparing((int[] x) -> x[0]).thenComparing(x -> x[1]));
        PriorityQueue<Integer> q = new PriorityQueue<>();
        int answer = 0;
        for(int i = 0; i< arr.length; i ++){
            int [] node = arr[i];
            while(!q.isEmpty() && q.peek() <= node[0]) q.remove();
            q.add(node[1]);
            answer = Math.max(answer, q.size());
        }
        return answer;
    }
    
    public int[] change(String[] str){
        int[] r = new int[2];
        for(int i = 0; i < 2; i ++){
            String[] s = str[i].split(":");
            r[i] = Integer.parseInt(s[0])*60 + Integer.parseInt(s[1]);
        }
        r[1] += 10;
        return r;
    }
}
