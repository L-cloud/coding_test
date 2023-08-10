import java.util.*;
import java.io.*;
public class Main {
	static HashSet<Character> s;
	static String[] arr;
	static char[] sc;
	static int[] NM;
 	static int ans;
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		NM = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		if(NM[1] < 5) {
			System.out.println(0);
			System.exit(0);
		}
		s = new HashSet<>();
		arr = new String[NM[0]];
		for(int i = 0; i<NM[0]; i ++) {
			arr[i] = br.readLine().replaceAll("[antic]","");
			for(int j = 0; j < arr[i].length(); j ++) s.add(arr[i].charAt(j));
		}
		sc = new char[s.size()];
		int index =0 ;
		for(char c : s) sc[index++] = c; 

		dfs(new HashSet<Character>(), 0);
		System.out.println(ans);
		
		
	}
	
	public static void dfs(HashSet<Character> sb,int index) {
		if(sb.size() == Math.min(NM[1] - 5, sc.length)) {
			int cnt = 0;
			for(String s : arr) {
				boolean flag = true;
				for(int i = 0; i < s.length(); i ++) {
					if(!sb.contains(s.charAt(i))) {
						flag = false;
						break;
					}
				}
				if(flag) cnt ++;
			}
			ans = Math.max(cnt, ans);
			return;
		}
		for(int i = index; i <sc.length; i++) {
			sb.add(sc[i]);
			dfs(sb,i+1);
			sb.remove(sc[i]);
		}
	}

}

