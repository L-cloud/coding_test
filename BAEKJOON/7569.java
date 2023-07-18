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
		int N,M,H;
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		Queue<int []> q = new LinkedList<>();
		int[][][] tomato = new int[H][N][M];
		int s = N*M*H;
		for(int i = 0; i <H; i++) { // 초기화
			for(int j = 0; j < N; j ++) {
				String[] tempt = br.readLine().split(" ");
				for(int k = 0; k<tempt.length; k++) {
					tomato[i][j][k] = Integer.parseInt(tempt[k]);
					if (tomato[i][j][k] == 1) {
						q.offer(new int[] {i,j,k});
						s--;
					}
					else if (tomato[i][j][k] == -1) s--;
				}
			}
		}
		int ans = 0;
		int [] node  = new int [3];
		int[] dh = {1,0,0,0,0,-1};
		int[] dx = {0,0,1,0,-1,0};
		int[] dy = {0,1,0,-1,0,0};
		while (!q.isEmpty() && s > 0) {
			ans++;
			int size = q.size();
			for (int i = 0; i < size; i++) {
				node = q.poll();
				for(int j = 0; j <6; j ++) {
					int h = dh[j] + node[0];
					int x = dx[j] + node[1];
					int y = dy[j] + node[2];
					if (0<=h && h<H && 0<=x && x<N && 0<=y && y<M && tomato[h][x][y] == 0) {
						tomato[h][x][y] = 1;
						s--;
						q.offer(new int[] {h,x,y});
					}
				}
			}
		}
	  ans = (s == 0) ? ans : -1;
	  System.out.println(ans);
    }
}
