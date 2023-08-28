import java.util.*;
class Solution {
    public int[][] solution(int n) {
        int[][] answer = {};
        List<int[]> l = new LinkedList<>();
        dfs(n,1,3,2,l);
        answer = new int[l.size()][2];
        int index = 0;
        for(int[] node : l) answer[index++] = node;
        return answer;
    }
    
    public void dfs(int n, int from, int to, int via, List<int[]> l){
        // 원래는 3,1,3,2
        // 2의 관점 2, 1,2,3 1에서 2로 3를 거쳐서
        // 3을 1에서 3으로 이동
        // (1,2)를 3에서 3으로 이동 1을 거쳐서
        // 2가 되면 2에서 3으로 1을 거쳐서 
        if(n<=0) return;
        dfs(n-1,from, via, to,l);
        move(l,from,to);
        dfs(n-1,via,to,from,l);
    }
    
    public void move(List<int[]> l, int from,int to){
        l.add(new int[] {from, to});
    }
}
