import java.util.Deque;
import java.util.LinkedList;
class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int[] dx = new int[] {0,1,0,-1};
        int[] dy = new int[] {1,0,-1,0};
        boolean [][] v = new boolean[m][n];
        for (int i = 0; i < m; i ++){
            for (int j = 0; j < n; j ++){
                if (!v[i][j] && picture[i][j] != 0) {
                    v[i][j] = true;
                    int k = picture[i][j];
                    int num = 0;
                    numberOfArea ++;
                    Deque<int []> deque = new LinkedList<>();
                    deque.add(new int[]{i, j});
                    while ( 0 < deque.size()){
                    for (int q =0; q < deque.size(); q++){
                        int [] node = deque.removeLast();
                        num++;
                        for (int z = 0; z<4; z ++){
                            int x = dx[z] + node[0];
                            int y = dy[z] + node[1];
                            if (0<= x && x < m && 0<= y && y < n && !v[x][y] && picture[x][y] == k){
                                deque.addFirst(new int[]{x, y});
                                v[x][y] = true;
                            } 
                        }
                        
                    }
                  }
                maxSizeOfOneArea = (maxSizeOfOneArea > num) ? maxSizeOfOneArea : num;                
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}
