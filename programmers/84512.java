class Solution {
    static int cnt = 0;
    static String[] arr = {"A", "E", "I", "O", "U"};
    public int solution(String word) {
        return dfs("", word, 0);
    }
    
    public int dfs(String a, String ans,int index){
        if(a.equals(ans)) return cnt;
        if(index == 5) return -1;
        for(int i = 0; i < 5; i ++){
            cnt ++;
            int t = dfs(a+arr[i],ans,index+1);
            if(t > 0) return t;
        }
        return -1;
    }
}
