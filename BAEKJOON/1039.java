import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] arr = br.readLine().split(" ");
		Deque<Integer> q = new ArrayDeque<>();
		HashSet<Integer> s = new HashSet<>();
		int k = Integer.parseInt(arr[1]);
		q.add(Integer.parseInt(arr[0]));
		while (k-- > 0) {
			s.clear();
			int size = q.size();
			for(int i = 0; i <size; i++) {
				make(q.poll(), q, s, k);
			}
			if (s.size() == 0) {
				System.out.println(-1);
				System.exit(0);
			}
		}
		int sol = 0;
		for(int i : s) sol = Math.max(sol, i);
		System.out.println(sol);
	}
	
	public static void make(int n,Deque<Integer> q, HashSet<Integer> h,int k) {
		char[] arr = String.valueOf(n).toCharArray();
		for(int i = 0; i < arr.length-1; i++) {
			for(int j = i + 1; j < arr.length; j ++) {
				char t = arr[j];
				arr[j] = arr[i];
				arr[i] = t;
				if(arr[0] != '0') {
					int l = Integer.parseInt(String.valueOf(arr));
                    if (!h.contains(l)){
                        h.add(l);
					    q.addLast(l);   
                    }
				}
				arr[i] = arr[j];
				arr[j] = t;
			}
		}
	}

}
