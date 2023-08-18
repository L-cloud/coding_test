import java.io.*;
import java.util.*;
public class Main {
	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
 		char[][] arr = new char[nm[0]][nm[1]];
 		for(int i = 0; i < nm[0]; i ++) arr[i] = br.readLine().toCharArray();
 		boolean[][][] v= new boolean[2][nm[0]][nm[1]];
 		Deque<int []> q = new ArrayDeque<>();
 		q.add(new int [] {1,0,0}); // 벽 부숨? 몇 번 움직임? 
 		v[0][0][0] = true;
 		v[1][0][0] = true;
 		int cnt = 0;
 		int[] dx = {0,1,0,-1};
 		int[] dy = {1,0,-1,0};
 		while(!q.isEmpty()) {
 			cnt ++;
 			int size = q.size();
 			for(int i = 0; i < size; i ++) {
 				int[] node = q.poll();
 				if(node[1] == nm[0] -1 && node[2] == nm[1] -1) {
 					System.out.println(cnt);
 					System.exit(0);
 				}
 				for(int j = 0; j <4; j ++) {
 					int x = node[1] + dx[j];
 					int y = node[2] + dy[j];
 					if(0<=x && 0<= y && x <nm[0] && y <nm[1] && !v[node[0]][x][y]) {
 						if(arr[x][y] == '1' && node[0] > 0) {
 							q.addLast(new int [] {0,x,y});
 							v[0][x][y] = true;
 						}
 						if(arr[x][y] == '0' && !v[node[0]][x][y]) {
 							q.addLast(new int[] {node[0], x, y});
 							v[node[0]][x][y] = true;
 						}
 					}
 				}
 			}
 			
 		}
 		System.out.println(-1);
	}
}

