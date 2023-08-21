import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력
		int N = Integer.parseInt(br.readLine()); // 입력
		Deque<int []> q = new LinkedList<>(); // 큐 생성
		int s = 0; // 업무 점수
		for(int i = 1; i < N + 1; i ++) {
			int[] node = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray(); // 입력 받음
			if(node.length > 1) q.addFirst(node); // 0이 아니라면 제일 최상단에 넣음
			if(!q.isEmpty()  && --q.peek()[2] <= 0) s += q.remove()[1];  // 업무 순서대로 처리 하고 다 했으면	점수 획득
		}
		System.out.println(s); // 출력
	}

}
