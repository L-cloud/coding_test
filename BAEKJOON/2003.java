import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException{
    	// arr이 자연수임!
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int N = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(st.nextToken());
    	st = new StringTokenizer(br.readLine());
    	int[] arr = new int[N];
    	for(int i = 0; i <N; i++) {
    		arr[i] = Integer.parseInt(st.nextToken());
    	}
    	int s = 0;
    	int left = 0;
    	int cnt =0;
    	for(int i = 0; i <N; i++) {
    		s += arr[i];
    		if (s==M) cnt ++;
    		while (s > M) {
    			s -= arr[left ++];
    			if(s == M) cnt++;
    		}
    	}
    	System.out.println(cnt);
    }

}
