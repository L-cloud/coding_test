import java.util.*;
import java.io.*;
public class Main {
	static int [] NM;
	static int[][] m;
	static int[][] tempt;
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
  	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		NM = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		m = new int[NM[0]][NM[1]];
		for(int i = 0; i <NM[0]; i++) m[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		tempt = new int[NM[0]][NM[1]];
		int year = 0;
		while(island() == 1) {
			year ++;
			for(int i = 0; i <NM[0]; i ++) {
				for(int j = 0; j <NM[1]; j ++) {
					if(m[i][j] != 0) {
						tempt[i][j] = getnum(i,j);
					}
				}
			}
			for(int i = 0; i < NM[0]; i ++) {
				for(int j = 0; j<NM[1]; j ++) {
					m[i][j] -= tempt[i][j];
					if(m[i][j] < 0) m[i][j] = 0;
				}
			}
		}	
		System.out.println(island() == 0 ? 0 : year);
  	}
  	
  	public static int getnum(int r, int c) {
  		int cnt = 0;
  		for(int i = 0; i <4; i ++) {
  			int x = r + dx[i];
  			int y = c  + dy[i];
  			if(check(x,y)  && m[x][y] == 0) cnt ++;
  		}
  		return cnt;
  	}
	
	
	public static int island() {
		int cnt = 0;
		Queue<int[]> q = new LinkedList<>();
		boolean[][] v = new boolean[NM[0]][NM[1]];
		for(int i = 0; i < NM[0] ; i ++) {
			for(int j = 0; j<NM[1]; j ++) {
				if(m[i][j] != 0 && !v[i][j]) {
					cnt ++;
					q.add(new int[] {i,j});
					v[i][j] = true;
					while(!q.isEmpty()) {
						int[] node = q.remove();
						for(int k = 0; k <4; k++) {
							int x = node[0] + dx[k];
							int y = node[1] + dy[k];
							if(check(x,y)  && m[x][y] != 0 && !v[x][y]) {
								q.add(new int[] {x,y});
								v[x][y] = true;
							}
						}
					}
				}
			}
		}
		return cnt;
	}
	
	public static boolean check(int x, int y) {
		return 0<=x && x<NM[0] && 0<= y && y<NM[1];
	}
	
}

