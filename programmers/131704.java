import java.util.*;
class Solution {
    public int solution(int[] order) {
        Integer index = 1; 
        int answer = 0;
        LinkedList<Integer> s = new LinkedList<>();
        for(int o :order){
            if (o == index){
                // 현재 순서가 같음
                answer ++;
                index ++;
                continue;
            }
            if(s.size() > 0 && s.peek()==o ){
                // stack에 쌓여있는게 같음
                s.pop();
                answer++;
                continue;
            }
            if (index < o){
                // 현재 쌓은 것 보다 더 작음
                while(index< o){
                    s.push(index++);
                   // System.out.println(s.peek());
                }
                answer ++;
                index++;
            }
            else break; // stack 에 2 3 4 5 이렇게 쌓여있는데 4 순서오면 방법x
        }
        return answer;
    }
}
