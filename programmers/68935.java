/*
3진 법으로 만든다  7이라고 해보자
7 % 3 == 1
2
21 이렇게 되어야함 deque에서 addFirst인데
그냥 List에서 add만 한 뒤 
이를 앞에서부터 12 10진수로 바꿔주면 됨 근데 뒤에서 해야하는구나
그냥 21 
1200 이렇게 만든다음 즉 addFirst한 다음 그냥 for문으로 앞에서부터 3의 n승을 더해주면 된다!
*/
import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        Deque<Integer> q = new ArrayDeque<>();
        while(n >0){
            q.addFirst(n%3);
            n /=3;
        }
        int index = 0;
        while(!q.isEmpty()){
            answer += q.poll() * Math.pow(3,index++);
        }
        return answer;
    }
}
