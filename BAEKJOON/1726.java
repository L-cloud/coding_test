import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
         int[][] arr = new int[nm[0]][nm[1]];
         for(int i = 0; i < nm[0]; i++) arr[i] =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
         int[][][] v = new int[nm[0]][nm[1]][4];
         PriorityQueue<int []> q = new PriorityQueue<>(Comparator.comparingInt(x -> x[0]));
         int[] dx = {-1,0,1,0};
         int[] dy = {0,1,0,-1};
         int[] st = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
         st[0] --; st[1]--; st[2]--;
         int[] ds =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
         for(int i = 0; i < nm[0]; i ++) {
        	 for(int j = 0; j < nm[1]; j ++) {
        		 Arrays.fill(v[i][j], 100000);
        	 }
         }
         v[st[0]][st[1]][st[2]] = 0;
         q.add(new int[] {0,st[0],st[1],match(st[2])});
         ds[2] = match(ds[2] -1);
         int cnt = 1000000;
         while(!q.isEmpty()) {
    		 int[] node = q.poll();
    		 if(node[1] == ds[0] -1 && node[2] == ds[1] -1 && node[3] == ds[2]) {
    			 cnt = Math.min(node[0], cnt);
    			 continue;
    		 }
    		 for(int i = 1; i <4; i ++) {
        		 if(check(node[1] + i*dx[node[3]], node[2] + i*dy[node[3]], arr)) {
        			 if(node[0] + 1 <v[node[1] + i*dx[node[3]]][node[2] + i*dy[node[3]]][node[3]]) {
            			 v[node[1] + i*dx[node[3]]][node[2] + i*dy[node[3]]][node[3]] = node[0] + 1;
            			 q.add(new int[] {node[0] + 1, node[1] + i*dx[node[3]],  node[2] + i*dy[node[3]], node[3]});
        			 }
        		 }
        		 else break;
    		 }

    		 if(node[0] + 1 < v[node[1]][node[2]][(node[3] + 1)%4]) {
    			 v[node[1]][node[2]][(node[3] + 1)%4] = node[0] + 1;
    			 q.add(new int[] {node[0] + 1, node[1], node[2], (node[3] + 1)%4});
    		 }
    		 if(node[0] + 2 < v[node[1]][node[2]][(node[3] + 2)%4]) {
    			 v[node[1]][node[2]][(node[3] + 2)%4] = node[0] + 2;
    			 q.add(new int[] {node[0] + 2, node[1], node[2], (node[3] + 2)%4});
    		 }
    		 if(node[0] + 1 < v[node[1]][node[2]][(node[3] + 3)%4]) {
    			 v[node[1]][node[2]][(node[3] + 3)%4] = node[0] + 1;
    			 q.add(new int[] {node[0] + 1, node[1], node[2], (node[3] + 3)%4});
    		 }
         }
         System.out.println(cnt);
    }
    
    public static boolean check(int x, int y, int[][]arr) {
    	return 0<= x && x < arr.length && 0<=y && y<arr[0].length && arr[x][y] == 0;
    }
    
    public static int match(int x) {
    	if (x == 0 ) return 1;
    	else if(x == 1) return 3;
    	else if (x == 3) return 0;
    	return 2;
    }
}

