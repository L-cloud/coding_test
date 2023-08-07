import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static Deque<int []> q = new LinkedList<>();
	static HashMap<Integer,Integer> total_v = new HashMap<>();
	static int[] NM;
	static String[] m;
	static int[] dx = {0,1,0,-1};
	static int[] dy = {1,0,-1,0};
 	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		NM = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		m = new String[NM[0]];
		for(int i = 0; i < NM[0]; i++) m[i] = br.readLine();
		HashSet<Integer> v = new HashSet<>();
		v.add(0);
		System.out.println(dfs(0,0,v));
	}
	
	
	public static int range(int x, int y) {
		return Integer.parseInt(String.valueOf(m[x].charAt(y)));
	}
	
	public static HashSet<Integer> dcp(HashSet<Integer> v){
		HashSet<Integer> r = new HashSet<>();
		for(int i : v) {
			r.add(i);
		}
		return r;
	}
	
	public static int dfs(int x, int y, HashSet<Integer> v) {
		int cnt = 0;
		for(int k = 0; k< 4; k++) {
			int r = dx[k] * range(x,y) + x;
			int c = dy[k] * range(x,y) + y;
			if(0<= r && r< NM[0] && 0<= c && c <NM[1] && m[r].charAt(c) != 'H') {
				if(v.contains(r*NM[1] + c)) return -1;
				if(total_v.containsKey(r*NM[1] + c)) {
					cnt = Math.max(cnt, total_v.get(r*NM[1] + c) + 1);
					continue;
				}
				HashSet<Integer> t_v = dcp(v);
				t_v.add(r*NM[1] + c);
				int t = dfs(r,c,t_v);
				if (t == -1) return -1;
				cnt = Math.max(cnt, t);
			}
			
		}
		total_v.put(x*NM[1] + y, cnt);
		return cnt + 1;
	}
	
	

}

