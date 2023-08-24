class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 1;
        while(match(a) != match(b)){
            a = a%2 == 0? a/2 : a/2 +1;
            b = b%2 == 0? b/2 : b/2 + 1;
            answer++;
        }
        return answer;
    }
    
    public int match(int a){
        return a%2 == 0? a -1 : a;
    }
}
