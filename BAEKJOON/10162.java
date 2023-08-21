import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 입력
		int T = Integer.parseInt(br.readLine()); // 입력
		Deque<int []> q = new LinkedList<>(); // 큐 생성
		q.add(new int [] {0,0,0,0}); // 현재 시간 합, A, B, C 버튼 갯수
		HashSet<Integer> h = new HashSet<>(); // 중복 방지
		while(!q.isEmpty()) { // Q 빌때 까지
			int size = q.size(); // 큐 갯수 만큼 돈다
			for(int i = 0; i < size;i ++) {
				int[] node = q.poll();
				if(node[0] == T) { // T랑 같으면 최소값임 출력 이후 종료
					System.out.println(node[1] + " " + node[2] + " " + node[3]);
					System.exit(0);
				}
				
				if(node[0] + 300 <= T && !h.contains(node[0] + 300)) { // a버튼 누를 수 있음
					q.addLast(new int[] {node[0] + 300 , node[1] + 1, node[2], node[3]}); 
					h.add(node[0] + 300);
				}
				if(node[0] + 60 <=T && !h.contains(node[0] + 60)) { // b버튼 누를 수 있음
					q.addLast(new int[] {node[0] + 60, node[1], node[2] + 1, node[3] });
					h.add(node[0] + 60);
				}
				
				if(node[0] + 10 <=T && !h.contains(node[0] + 10)) { // c버튼 누를 수 있음
					q.addLast(new int[] {node[0] + 10, node[1], node[2], node[3] + 1 });
					h.add(node[0] + 10);
				}
			}
				
		}
		System.out.println(-1); // q가 비었다는 뜻임 그럼 조작 못 하니 out 사실 10으로 안 나누어 떨어지면 다 되는거라 위에서 예외 처리 해도 됨
		
	}

}

