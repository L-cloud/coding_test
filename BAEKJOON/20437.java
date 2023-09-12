import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashMap<Character, Deque<Integer>> h2 = new HashMap<>();
		for(char i = 'a'; i <= 'z'; i++) h2.put(i, new ArrayDeque<>());
		int t = Integer.parseInt(br.readLine());
		for(int q=0;q<t;q++) {
			char[] arr = br.readLine().toCharArray();
			int k = Integer.parseInt(br.readLine());
			for(char i = 'a'; i <='z'; i ++) {h2.put(i, new ArrayDeque<>());}
			int max_cnt = -1;
			int min_cnt = 10001;
			for(int i = 0 ; i < arr.length; i++) {
				h2.get(arr[i]).add(i);
				if (h2.get(arr[i]).size() == k) {
					// 3번, 4번 로직
					max_cnt = Math.max(max_cnt, h2.get(arr[i]).getLast() - h2.get(arr[i]).getFirst() + 1);
					min_cnt = Math.min(min_cnt,  h2.get(arr[i]).getLast() - h2.get(arr[i]).getFirst() + 1);
					h2.get(arr[i]).poll();
				}
				
			}
			if(max_cnt == -1) System.out.println(-1);
			else System.out.println(min_cnt+" "+max_cnt);
			
		}
		
	}
}
