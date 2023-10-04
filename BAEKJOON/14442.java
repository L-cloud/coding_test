import java.util.*;
import java.io.*;
public class Main {
	static int[] NMK;
	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		NMK = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		int[][] arr = new int[NMK[0]][NMK[1]];
		for(int i = 0; i < NMK[0]; i ++) {
			String t = br.readLine();
			for(int j = 0; j< NMK[1]; j++) {
				arr[i][j] = t.charAt(j) - '0';
			}
		}
		System.out.println(sol(arr));
	}
	
	
	public static boolean check(int[][] v, int x, int y , int k) {
		return v[x][y] < k;
	}
	
	public static int sol(int[][] arr) {
		int[] dx = {0,1,0,-1};
		int[] dy = {1,0,-1,0};
		int[][] v = new int[NMK[0]][NMK[1]];
		Deque<int []> q = new ArrayDeque<>();
		q.add(new int [] {0,0,NMK[2] + 1});
		v[0][0] = NMK[2];
		int cnt = 1;
		while(!q.isEmpty()) {
			int size = q.size();
			for(int t = 0; t < size; t++) {
				int[] node = q.poll();
				if(node[0] == NMK[0] -1 && node[1] == NMK[1]-1) return cnt;
				for(int i = 0; i < 4; i ++) {
					int x = node[0] + dx[i];
					int y = node[1] + dy[i];
					if(0<=x && x < NMK[0] && 0<= y && y <NMK[1]) {
						if(arr[x][y] == 1 && check(v,x,y,node[2] -1)) {
							v[x][y] = node[2] -1;
							q.addLast(new int[] {x,y,node[2] - 1});
						}
						if(arr[x][y] == 0 && check(v,x,y,node[2])) {
							v[x][y] = node[2];
							q.addLast(new int[] {x,y,node[2]});
						}
					}
				}
			}
			cnt++;
		}
		return -1;
	}
}

