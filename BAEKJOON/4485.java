import java.util.*;
import java.io.*;
public class Main {
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int cnt = 0;
		while(true) {
			cnt ++;
			int n = Integer.parseInt(br.readLine());
			if(n == 0) break;		
			int[][] arr = new int[n][n];
			for(int i = 0; i < n; i ++) arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			int[][] dp = new int[n][n];
			for(int i = 0; i < n ; i ++) Arrays.fill(dp[i], 100000);
			PriorityQueue<int []> q = new PriorityQueue<>(Comparator.comparing(x -> x[0]));
			q.add(new int[] {arr[0][0],0,0});
			while(!q.isEmpty()) {
				int [] node = q.poll();
				for(int i = 0 ; i < 4; i ++) {
					int x = node[1] + dx[i];
					int y = node[2] + dy[i];
					if(0<= x && x <n && 0<= y && y < n && node[0] + arr[x][y] < dp[x][y]) {
						dp[x][y] = node[0] + arr[x][y];
						q.add(new int[] {dp[x][y], x, y});
					}
				}
			}
			System.out.println("Problem "+ cnt + ": " +dp[n-1][n-1]);
		}
	}

}
