import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		HashMap<Integer, String> h = new HashMap<>();
		int[][] arr = new int[N][N];
		int t = Integer.parseInt(br.readLine());
		for(int i = 0; i < t; i ++) {
			String[] tt = br.readLine().split(" ");
			arr[Integer.parseInt(tt[0]) - 1][Integer.parseInt(tt[1]) - 1] = 1;
		}
		t = Integer.parseInt(br.readLine());
		for(int i = 0; i < t; i ++) {
			String[] tt = br.readLine().split(" ");
			h.put(Integer.parseInt(tt[0]), tt[1]);
		}
		System.out.println(sol(h,arr));
	}
		
	
	
	public static int sol(HashMap<Integer, String> h, int[][] arr ) {
		int[][] d = {{0,1}, {1,0},{0,-1},{-1,0}};
		List<int[]> snake = new ArrayList<>();
		arr[0][0] = 2;
		snake.add(new int[] {0,0});
		int direction = 0;
		int time = 0;
		while(true) {
			time ++;
			int[] next = {snake.get(0)[0] + d[direction][0],snake.get(0)[1] + d[direction][1] };
			if(!(0<= next[0] && next[0] < arr.length && next[1] < arr.length && next[1] >= 0)) return time;
			if(arr[next[0]][next[1]] == 2) return time;
			if (arr[next[0]][next[1]] == 1) {
				snake.add(0,next); // 사과 먹으면 그냥 몸 늘어감
			}
			else {
				arr[snake.get(snake.size() -1)[0]][snake.get(snake.size() -1)[1]] = 0; // 제일 끝 지워줌
				move(snake,next);
			}
			arr[next[0]][next[1]] = 2; // 머리 늘어감
			if (h.containsKey(time)) {
				direction = rotate(direction, h.get(time));
			}

		}
		
	}
	
	
	public static int rotate(int direction, String d) {
		if (d.equals("L")) {
			direction = direction - 1 > -1 ? direction - 1 : 3 ;
		}
		else {
			direction = direction + 1 < 4 ? direction + 1 : 0 ;
		}
		return direction;
	}
	
	public static void move(List<int[]> snake, int[] next) {
		for(int i = 0; i < snake.size(); i++) {
			int[] t = snake.get(i);
			snake.set(i, next);
			next = t;
		}
	}
}

