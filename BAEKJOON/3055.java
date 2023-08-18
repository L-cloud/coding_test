import java.io.*;
import java.util.*;
public class Main {
	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
 		char[][] arr = new char[nm[0]][nm[1]];
 		for(int i = 0; i < nm[0]; i ++) arr[i] = br.readLine().toCharArray();
 		Deque<int []> mq = new LinkedList<>();
 		Deque<int []> wq = new LinkedList<>();
 		for(int i = 0; i <nm[0]; i++) {
 			for(int j = 0; j < nm[1]; j ++) {
 				if(arr[i][j] == '*') wq.add(new int [] {i,j});
 				if(arr[i][j] == 'S') mq.add(new int [] {i,j});
 			}
 		}
 		int[] dx = {0,1,0,-1};
 		int[] dy = {1,0,-1,0};
 		int cnt = -1;
 		while(!mq.isEmpty()) {
 			cnt ++;
 			int size = mq.size();
 			for(int i = 0; i <size; i ++) {
 				int[] node = mq.poll();
 				if(arr[node[0]][node[1]] != 'S') continue;
 				for(int j = 0; j < 4; j ++) {
 					int x = node[0] + dx[j];
 					int y = node[1] + dy[j];
 					if(0<=x && 0<=y && x < nm[0] && y < nm[1]) {
 						if(arr[x][y] == '.') {
 	 						mq.addLast(new int [] {x,y});
 	 						arr[x][y] = 'S';
 						}
 	 					if(arr[x][y] == 'D') {
 	 						System.out.println(cnt + 1);
 	 						System.exit(0);

 					    }
 					}
 				}
 			}
 			size = wq.size();
 			for(int i =0; i < size; i ++) {
 				int[] node = wq.poll();
 				for(int j = 0; j < 4; j ++) {
 					int x = node[0] + dx[j];
 					int y = node[1] + dy[j];
 					if(0<=x && 0<=y && x < nm[0] && y < nm[1] && arr[x][y] != 'X' && arr[x][y] != 'D' && arr[x][y] != '*') {
 						wq.addLast(new int [] {x,y});
 						arr[x][y] = '*';
 					}
 				}
 			}
 		}
 		System.out.println("KAKTUS");
 		
	}
	
}









