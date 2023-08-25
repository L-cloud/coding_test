import java.util.*;
class Solution {
    public int solution(int[] elements) {
        HashSet<Integer> s = new HashSet<>();
        s.add(Arrays.stream(elements).sum());
        for(int i = 1; i<elements.length - 1;i++){
            for(int k = 0; k < elements.length; k ++){
              int t = 0;
              for(int j = 0; j < i; j ++){
                    int index = (k + j) % elements.length;
                    t += elements[index];
                  } 
               s.add(t);
            }
            
        }
        return s.size();
    }
    
}
