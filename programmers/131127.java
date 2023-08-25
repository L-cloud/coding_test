import java.util.*;
class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        HashMap<String,Integer> h = new HashMap<>();
        int index = 0;
        int sum = Arrays.stream(number).sum();
        for(String w : want) h.put(w,index++);
        for(int i = 0; i < 10; i ++){
            if(h.containsKey(discount[i])){
                if(number[h.get(discount[i])] > 0)sum--;
                number[h.get(discount[i])]--;
            }
        }
        int s = sum == 0? 1 : 0;
        int left = 0;
        int right = 10;
        while(right < discount.length){
            if(h.containsKey(discount[left])){
                 number[h.get(discount[left])]++;
                 if(number[h.get(discount[left])] > 0) sum++;
                
            }
            if(h.containsKey(discount[right])){
                if(number[h.get(discount[right])] > 0) sum--;
                number[h.get(discount[right])]--;
                
            }
            if(sum == 0) s++;
            left++;
            right++;
        }
        return s;
    }
}
