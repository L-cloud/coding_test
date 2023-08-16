import java.io.*;
import java.util.*;
public class Main {
	static char[][] arr;
	static int[] nm;
	static int cnt;
	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		nm =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
 		arr = new char[nm[0]][nm[1]];
 		for(int i = 0; i < nm[0]; i ++) arr[i] = br.readLine().toCharArray();
 		for(int i = 0; i < nm[0]; i++) dfs(i,0);
 		System.out.println(cnt);
 		
 		
	}
	
	public static boolean dfs(int r, int c) {
		if(c == nm[1] - 1 ) {
			cnt ++;	
			return true;
		}
		if(0<=r-1 && c+1<nm[1] && arr[r-1][c+1] == '.') {
			arr[r-1][c+1] = '-';
			if(dfs(r-1,c+1)) return true;
		}
		if(c+1<nm[1] && arr[r][c+1] == '.'){
			arr[r][c+1] = '-';
			if(dfs(r,c+1)) return true;
		}
		if(c+1<nm[1] && r+1 <nm[0] && arr[r+1][c+1] == '.') {
			arr[r+1][c+1] = '-';
			if(dfs(r+1,c+1)) return true;
		}
		return false;
	}
	
	
}
