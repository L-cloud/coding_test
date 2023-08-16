import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	int [] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
    	long[][] dp = new long[N][21];
    	dp[0][arr[0]] = 1;
    	for(int i = 1; i < N-1; i++) {
    		for(int j  = 0 ; j <21; j ++) {
    			if(dp[i-1][j] == 0) continue;
    			if(j + arr[i] <= 20) dp[i][j + arr[i]] += dp[i-1][j];
    			if(0<=j - arr[i]) dp[i][j - arr[i]] += dp[i-1][j]; 
    		}
    	}
    	System.out.println(dp[N-2][arr[arr.length -1]]);
    }
}
