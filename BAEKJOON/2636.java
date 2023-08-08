import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
 	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		
		String[] input = br.readLine().split(" ");
		char[][] m = new char[Integer.parseInt(input[0])][Integer.parseInt(input[1])];
		for(int k = 0; k < Integer.parseInt(input[0]); k++) {
			m[k] = br.readLine().replaceAll(" ", "").toCharArray();
		}
		int cnt = 0;
		int sol = 0;
		int prev = 0;
		Queue<int []> q = new LinkedList<>();
		while(true) {
			air(m);
			for(int i = 0; i < m.length; i ++ ) {
				for(int j = 0; j < m[0].length; j++) {
					if(m[i][j] == '1' ) {
						cnt ++;
						if(check(i,j,m)) {
							q.add(new int[] {i,j});
						}
					}
				}
			}
			if(cnt == 0) break;
			sol ++;
			prev = cnt;
			cnt = 0;
			while (!q.isEmpty()) {
				int[] node = q.remove();
				m[node[0]][node[1]] = '2';
			}
		}
			System.out.println(sol);
			System.out.println(prev);
 	}
		
 	public static boolean check(int r, int c, char[][] m) {
 		for(int i = 0; i < 4; i ++) {
 			int x = r + dx[i];
 			int y = c + dy[i];
 			if(0<=x && x< m.length && 0<=y  && y < m[0].length && m[x][y] == '2') return true;
 		}
 		return false; // 녹는거 아님
 	}
 	
 	public static void air(char [][] m) {
 		Queue<int []> q = new LinkedList<>();
 		boolean[][] v = new boolean[m.length][m[0].length]; 
 		q.add(new int[] {0,0});
 		m[0][0] = '2';
 		v[0][0]= true;
 		while(!q.isEmpty()) {
 			int[] node = q.remove();
 			for(int i = 0; i < 4; i ++) {
 	 			int x = node[0] + dx[i];
 	 			int y = node[1] + dy[i];
 	 			if(0<=x && x< m.length && 0<=y  && y < m[0].length && !v[x][y] &&(m[x][y] == '0' || m[x][y] == '2' )) {
 	 				m[x][y] = '2';
 	 				q.add(new int[] {x,y});
 	 				v[x][y]=true;
 	 			}
 	 		}
 		}
 	}
 	
}


