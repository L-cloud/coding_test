import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
 	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		int N = Integer.parseInt(br.readLine());
 		for(int T = 0; T< N; T ++){
 			String[] input = br.readLine().split(" ");
 			int[][] m = new int[Integer.parseInt(input[0])][Integer.parseInt(input[1])];
 			for(int k = 0; k < Integer.parseInt(input[2]); k++) {
 				String[] in = br.readLine().split(" ");
 				m[Integer.parseInt(in[0])][Integer.parseInt(in[1])] = 1;
 			}
 			int cnt = 0;
 			for(int i = 0;i<m.length; i ++) {
 				for(int j = 0; j < m[0].length; j++) {
 					if(m[i][j] == 1) {
 						cnt ++;
 						m[i][j] = 0;
 						check(i,j,m);
 					}
 				}
 			}
 			System.out.println(cnt);
 			
 			
 		}
	}
 	public static void check(int r, int c, int[][] m) {
 		Queue<int []> q = new LinkedList<>();
 		q.add(new int[] {r,c});
 		while(!q.isEmpty()) {
 			int [] node = q.remove();
 			for(int i = 0; i<4;i ++) {
 				int x = node[0] + dx[i];
 				int y = node[1] + dy[i];
 				if(0<= x && x < m.length && 0<= y && y < m[0].length && m[x][y] == 1) {
 					m[x][y] = 0;
 					q.add(new int[] {x,y});
 				}
 			}
 		}
 	}
 	
}


