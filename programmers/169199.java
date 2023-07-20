import java.util.*;
class Solution {
    public int solution(String[] board) {
        int [] dx = {0,1,0,-1};
        int [] dy = {1,0,-1,0};
        int[][] v = new int[board.length][board[0].length()];
        int answer = 0;
        Queue<int []> q = new LinkedList<>();
        q.add(find_start(board));
        System.out.println(q.peek()[0]+ " " + q.peek()[1]);
        v[q.peek()[0]][q.peek()[1]] = 1;
        while (!q.isEmpty()){
            answer ++;
            int size = q.size();
            for(int i = 0; i <size;i++){
                int[] node = q.poll();
                for(int k = 0; k < 4; k++){
                    int x = node[0];
                    int y = node[1];
                    while(0<=x + dx[k] && x + dx[k] <v.length && 0<= y + dy[k] && y + dy[k] < v[0].length && board[x + dx[k]].charAt(y + dy[k]) != 'D')
                    { // 끝까지 움직임
                        x += dx[k];
                        y += dy[k];
                    }
                    if (v[x][y] == 1) continue; // 이미 방문
                    if(board[x].charAt(y) == 'G') return answer;
                    v[x][y] = 1;
                    q.add(new int[] {x,y});
                }
            
            }
            
        }
        return -1;
    }
    
    public int[] find_start(String[] board){
        for (int i =0; i<board.length; i++){
            for(int j = 0; j < board[0].length(); j ++){
                if(board[i].charAt(j) == 'R') {
                    return new int[] {i,j};
                }
            }
        }
        return new int[] {};
    }
}

