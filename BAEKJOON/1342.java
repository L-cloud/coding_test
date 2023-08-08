import java.io.*;
import java.util.*;

public class Main {
	static HashMap<Character, Integer> v;
	static int N;
	static int len; 
	public static void main(String[] args) throws IOException{
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 char[] input = br.readLine().toCharArray();
		 v = new HashMap<>();
		 for(int i  = 0; i < input.length; i ++) {
			 int var = v.getOrDefault(input[i], 0);
			 v.put(input[i], var + 1);
		 }
		 Character[] arr = new Character[v.size()];
		 len = input.length;
		 int index = 0 ;
		 for(Character v : v.keySet()) {
			 arr[index ++] = v;
		 }
		 Arrays.sort(arr, Comparator.comparing(x -> -v.get(x)));
		 dfs('0', 0);
		 System.out.println(N);
		 
	}
	
	public static void dfs(char prev, int cnt) {
		if(cnt == len) {
			N++;
			return;
		}
		for(char k : v.keySet()) {
			if (k != prev && v.get(k) != 0) {
				v.put(k, v.get(k) -1);
				dfs(k,cnt + 1);
				v.put(k, v.get(k) + 1);
			}
		}

	}
}

