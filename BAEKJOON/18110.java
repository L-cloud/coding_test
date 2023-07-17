import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	int[] m = new int[N];
    	for(int i = 0; i<N;i++) m[i] = Integer.parseInt(br.readLine());
    	Arrays.sort(m);
    	int t = (int)Math.round( N * (3.0f/20.0f));
    	int cnt = 0;
    	for (int i = t; i < N - t; i++) cnt += m[i];
    	System.out.println((int) Math.round(cnt /(float)(N - 2*t)));
    }

}
