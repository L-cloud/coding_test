import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
 	static int[] m;
 	static int[][] arr = new int[6][3];
 	static boolean[][] v;
 	static int[] index;
	public static void main (String[] args) throws IOException {
 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 		StringBuilder sb = new StringBuilder();
 		for(int i = 0; i <4;i++) {
 			m = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
 			v = new boolean[6][6];
 			for(int j = 0; j<6; j++) {
 				for(int k = 0; k<3; k++) arr[j][k] = m[j*3+k];
 			}
 			index = new int[] {0,0,0,0,0,1,1,1,1,2,2,2,3,3,4};
 			if (sum()) sb.append(dfs(0) + " ");
 			else sb.append(0 + " ");
 		}
 		System.out.println(sb);
 	}
	
	public static int dfs(int n) {
		if(n == 15) return 1;	
			int i = index[n];
			boolean flag = false; 
			for(int j = i + 1; j < 6; j ++) {
				if(v[i][j])continue;
				// 각 국가들이랑 싸우는 거임 그래서 이겼는지 졌는지 기록하고 넘김
				if(arr[i][0] > 0 && arr[j][2] > 0) {
					v[i][j] = true;
					arr[i][0] --;
					arr[j][2] --;
					if(dfs(n+1) == 1) return 1;
					arr[i][0] ++;
					arr[j][2] ++;
					v[i][j] = false;
					flag = true;
				}
				if(arr[i][1]>0 && arr[j][1] >0) {
					v[i][j] = true;
					arr[i][1] --;
					arr[j][1] --;
					if(dfs(n+1) == 1) return 1;
					arr[i][1] ++;
					arr[j][1] ++;
					v[i][j] = false;
					flag = true;
				}
				if(arr[i][2]>0 && arr[j][0] >0) {
					v[i][j] = true;
					arr[i][2] --;
					arr[j][0] --;
					if(dfs(n+1) == 1) return 1;
					arr[i][2] ++;
					arr[j][0] ++;
					v[i][j] = false;
					flag = true;
				}
			}
			if(!flag) return 0; // 경기를 해야하는 녀석인데 못 함
		return 0;
	}
	
	public static boolean sum() {
		for(int i = 0; i <6; i++) {
			int c = 0;
			for(int j = 0; j < 3; j ++) c += arr[i][j];
			if(c!= 5) return false;
		}
		return true;
	}
}


