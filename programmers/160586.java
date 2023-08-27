import java.util.*;
class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        HashMap<Character, Integer> h = new HashMap<>();
        for(char i = 'A'; i <= 'Z'; i++) h.put(i,10000);
        int [] answer = new int[targets.length];
        for(String key : keymap){
            for(int i = 0; i < key.length(); i++) h.put(key.charAt(i), Math.min(h.get(key.charAt(i)), i + 1));
        }
        for(int j = 0; j <targets.length; j ++){
            int cnt = 0;
            for(int i =0; i < targets[j].length(); i ++){
                if(h.get(targets[j].charAt(i)) == 10000){
                    cnt = -1;
                    break;
                }
                cnt += h.get(targets[j].charAt(i));
            }
            answer[j] = cnt;
        }
        return answer;
    
    }

    
    
}
