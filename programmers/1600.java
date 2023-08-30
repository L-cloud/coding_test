import java.io.*;
import java.util.*;
public class Main {
	static int[] nm;
	static int[][] arr;
	static int[][] v;
	public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int k = Integer.parseInt(br.readLine());
      nm =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
      arr = new int[nm[1]][nm[0]];
      for(int i = 0; i < nm[1]; i ++) arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
      v = new int[nm[1]][nm[0]];
      for(int i = 0; i < nm[1]; i ++) Arrays.fill(v[i], -1);
      int[] dx = {0,1,0,-1};
      int[] dy = {1,0,-1,0,1};
      int[] hx = {-2, -1, 1, 2, 2, 1, -1, -2};
      int[] hy = {1,   2, 2 ,1, -1 ,-2 ,-2,-1};
      Deque<int []> q = new ArrayDeque<>();
      q.add(new int [] {k,0,0});
      int cnt = -1;
      while(!q.isEmpty()) {
    	  cnt ++;
    	  int size = q.size();
    	  for(int i = 0; i < size; i ++) {
    		  int[] node = q.poll();
    		  if(node[1] == nm[1] -1 && node[2] == nm[0] -1) {
    			  System.out.println(cnt);
    			  System.exit(0);
    		  }
    		  check(q,dx,dy,node,0);
    		  if(node[0] == 0) continue;
    		  check(q,hx,hy,node,1);
    	  }
      }
      System.out.println(-1);
	}
	
	public static void check( Deque<int []> q, int[] dx, int[] dy, int[] node, int flag) {
		for(int j = 0 ; j < dx.length; j ++) {
			  int x = node[1] + dx[j];
			  int y = node[2] + dy[j];
			  if(0<=x && x < nm[1] && 0<= y && y < nm[0] && arr[x][y] == 0 &&  v[x][y] < node[0] - flag) {
				  q.addLast(new int[] {node[0] - flag, x, y});
				  v[x][y] = node[0] - flag;
			  }
		  }
	}
	
}
