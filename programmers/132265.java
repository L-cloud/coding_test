import java.util.*;
class Solution {
    public int solution(int[] topping) {
        HashMap<Integer,Integer> brother = new HashMap<>();
        HashMap<Integer,Integer> me = new HashMap<>();
        int answer = 0;
        for(int i : topping) me.put(i, me.getOrDefault(i,0) + 1); // 일단 다 채움
        for(int i: topping){
            brother.put(i, me.getOrDefault(i,0) + 1);
            if(me.containsKey(i)){
                int t = me.get(i);
                if(t == 1) me.remove(i);
                else me.put(i,t-1);
            }
            
            if(brother.size() == me.size()) answer++;
        }
        return answer;
    }
}
