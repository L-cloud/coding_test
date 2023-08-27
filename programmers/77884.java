/*
기본 로직
1. 그냥 모든 수의 약수를 체크한다.
체크 시간 복잡도는 O(N)
*/
class Solution {
    public int solution(int left, int right) {
        int answer = 0;
        for(int i = left; i <= right; i ++){
            if(i > 1 && check(i)) answer += i;
            else answer -= i;
        }
        return answer;
    }
    
    public boolean check(int n){
        int cnt = 2; // 1과 자기 자신 1인 경우는 예외임
        for(int i = 2; i<=n/2; i ++){
            if (n % i  == 0) cnt ++;
        }
        
        return cnt % 2 == 0? true : false; // 짝수면 true;
    }
}
