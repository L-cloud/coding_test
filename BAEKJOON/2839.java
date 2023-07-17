import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	// 그냥  dp로 풀어버리자
    	int[] matrix = new int [N+1];
    	for(int i = 0;i<N+1; i ++) {
    		matrix[i] = N;
    	}
    	int index = 1;
    	for (int i = 5; i < N+1; i +=5) {
    		matrix[i] = index ++;
    	}
    	for (int i = 3; i<N+1; i +=3) {
    		matrix[i] = (i/3 < matrix[i]) ? i/3 : matrix[i]; 
    	}
    	for (int i = 8; i < N+1; i++) {
    			matrix[i] = (matrix[i-3] + 1 < matrix[i]) ? matrix[i-3] + 1 : matrix[i];
    	}
    	System.out.println((matrix[N] == N) ? -1 : matrix[N]);
    }

}
