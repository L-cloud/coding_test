import java.io.*;
import java.util.*;
public class Main {
	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		StringBuilder sb = new StringBuilder();
 		int T = Integer.parseInt(br.readLine());
 		for(int t = 0; t <T; t ++) {
 			int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
 			int tempt = nm[0];
 			nm[0] = nm[1];
 			nm[1] = tempt;
 			char[][] arr = new char[nm[0]][nm[1]];
 			for(int i= 0; i <nm[0]; i ++) arr[i] = br.readLine().toCharArray();
 			int[] dx = {0,1,0,-1};
 			int[] dy = {1,0,-1,0};
 			Deque<int []> sq = new LinkedList<>();
 			Deque<int[]> fq = new LinkedList<>();
 			boolean[][] v = new boolean[nm[0]][nm[1]];
 			for(int i = 0; i <nm[0]; i ++) {
 				for(int j = 0; j<nm[1]; j++) {
 					if(arr[i][j] == '*') fq.add(new int[] {i,j});
 					if(arr[i][j] == '@') {
 						sq.add(new int[] {i,j});
 					}
 				}
 			}
 			int cnt = 0;
 			HashSet<Integer> h ;
 			a : while(true) {
 				cnt ++;
 				h  = new HashSet<>();
 				int size = sq.size();
 				for(int i = 0; i < size; i ++) {
 					int[] node = sq.poll();
 					for(int j = 0; j < 4; j ++) {
 						int x = node[0] + dx[j];
 						int y = node[1] + dy[j];
 						if(x < 0 || x >= nm[0] || y < 0 || y>=nm[1]) {
 							sb.append(cnt + "\n");
 							break a;
 						}
 						if(arr[x][y] == '.' && !v[x][y]) {
 							v[x][y] = true;
 							sq.addLast(new int[] {x,y});
 							h.add(x*nm[1] + y);
 						}
 					} 
 				}
 				size = fq.size();
 				for(int i = 0; i < size; i ++) {
 					int [] node = fq.poll();
 					for(int j = 0 ; j <4; j ++) {
 						int x = node[0] + dx[j];
 						int y = node[1] + dy[j];
 						if(0<= x && 0<=y && x<nm[0] && y<nm[1] && (arr[x][y] == '.' || arr[x][y] == '@')) {
 							fq.addLast(new int [] {x,y});
 							if(h.contains(x*nm[1] + y)) {
 								h.remove(x*nm[1] + y);
 							}
 							arr[x][y] = '*';
 						}
 					}
 				}
 				if(h.size() == 0) {
 					sb.append("IMPOSSIBLE" + "\n");
 					break;
 				}
 			}
 		}
 		System.out.println(sb);
	}
	
}


