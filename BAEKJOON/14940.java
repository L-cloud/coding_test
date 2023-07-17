import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;
class Main
{
    public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        Queue<int[]> q = new LinkedList<>();
        boolean[][] visit = new boolean[N][M];
		int [][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] == 2) {
                	q.offer(new int []{i,j,0});
                	visit[i][j] = true;
                	arr[i][j] = 0;
                }
            }
        }
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
       
        while (!q.isEmpty()) {
        	for(int i =0; i<q.size(); i ++) {
        		int[] node = q.poll();
        		for (int j = 0; j < 4; j++) {
        			int x = dx[j] + node[0];
        			int y = dy[j] + node[1];
        			if(0<=x && x < N && 0<= y && y <M && !visit[x][y] && arr[x][y] == 1) {
        				visit[x][y] = true;
        				arr[x][y] = node[2] + 1;
        				q.offer(new int[] {x,y,arr[x][y]});
        			}
        		}
        		
        	}
        }
        for(int i = 0; i <N; i++) {
        	for(int j = 0; j<M; j++) {
        		if (!visit[i][j] && arr[i][j] == 1) arr[i][j] = -1;
        		System.out.print(arr[i][j] + " ");
        	}
        	System.out.println();
        }

    }
}
