import java.io.*;
import java.util.*;
public class Main {
	static HashSet<Character>[][] v;
	public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int[] nm =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
	  char[][] arr = new char[nm[0]][];
	  for(int i = 0; i < nm[0]; i ++) arr[i] = br.readLine().toCharArray();
	  // 이미 방문 한 것을 어떻게 처리 할 것인가? 그냥 키를 가지고 있는지만 체크하면 되는거 아님?
	  v = new HashSet[nm[0]][nm[1]];
	  for(int i = 0; i < nm[0]; i ++) {
		  for(int j = 0; j < nm[1]; j ++) v[i][j] = new HashSet<Character>();
	  }
	  int[] dx = {0,1,0,-1};
	  int[] dy = {1,0,-1,0};
//	  Character.isUpperCase
//	  Character.isLowerCase
	  Deque<u> q = new ArrayDeque<>();
	  int[] l = location(arr);
	  HashSet<Character> t =  new HashSet<>();
	  t.add('0');
	  q.addFirst(new u(l[0], l[1], t));
	  int cnt = -1;
	  while (!q.isEmpty()) {
		  cnt ++;
		  int size = q.size();
		  for(int i =0 ; i < size; i ++) {
			  u node = q.poll();
			  if(arr[node.x][node.y] == '1') {
				  System.out.println(cnt);
				  System.exit(0);
			  }
			  for(int j = 0 ; j < 4; j ++) {
				  int x = node.x + dx[j];
				  int y = node.y + dy[j];
				  if(0<=x && x<nm[0] && 0<= y && y<nm[1] && arr[x][y] != '#') {
					  /*
					   * 여기서 어떻게 해아하는가
					   * 무엇부터 체크? 일단 방문 한 번 해봄.. 방문 가능한지 check하기 전에 대문자면 키가 있어야하는거임
					   */
					  if(Character.isUpperCase(arr[x][y])) {
						  if(!node.key.contains(Character.toLowerCase(arr[x][y]))) continue; // 키가 없음 
						  if(isv(node.key,x,y)) continue; // 키는 있는데 이미 방문함
						  // 키 있는데 방문 안 함
						  u new_node = new u(x,y,makeset(node.key));
						  q.addLast(new_node);
						  v[x][y] = makeset(node.key);
						  continue;
					  }
					  // 여기는 갈 수 있음! 그런데 그럼 방문 했는지 체크하자
					  if(isv(node.key,x,y)) continue; // 이미 방문 함
					  if(Character.isLowerCase(arr[x][y])){ // 키임 그리고 방문 안함
						  HashSet<Character> k = makeset(node.key);
						  k.add(arr[x][y]);
						  v[x][y] = makeset(k);
						  q.add(new u (x,y, k));
						  continue;
					  } 
					  // 그냥 가는 곳임
					  u new_node = new u(x,y,makeset(node.key));
					  q.addLast(new_node);
					  v[x][y] = makeset(node.key);
				  }
			  }
		  }
	  }
	  System.out.println(-1);
	}
	
	public static int[] location(char[][] arr) {
		for(int i = 0; i< arr.length; i ++) {
			for(int j = 0 ; j < arr[0].length; j ++) {
				if(arr[i][j] == '0') return new int[] {i,j};
			}
		}
		return null;
	}
	
	public static boolean isv(HashSet<Character> s, int x, int y) {
		// 체크 해야하는 경우 s에 있는 애들이 모두 v에 포함 되어야함!
		int size = s.size();
		for(Character c : s) {
			if (v[x][y].contains(c)) size --;
		}
		return size == 0? true : false; // true라면 이미 방문함
	}
	
	public static HashSet<Character> makeset(HashSet<Character> s){
		HashSet<Character> r = new HashSet<>();
		for(Character c : s) {
			r.add(c);
		}
		return r;
	}
	
	static class u {
		public int x;
		public int y;
		public HashSet<Character> key;
		public u(int x, int y, HashSet<Character> key) {
			this.x = x;
			this.y = y;
			this.key = key;
		}
		
	}
	
	
}
