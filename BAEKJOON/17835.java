import java.util.*;
import java.io.*;
public class Main {

	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] NMK = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		// 그럼 처음에 면접장까지 거리해서 그냥 다 초기화 한 다음에 면접장 돌면서.. 그 다음 이제 가장 작은 녀석들 부터 해서 돌면 되는거 아님?
		long[] distance = new long[NMK[0]];
		Arrays.fill(distance, Long.MAX_VALUE);
		HashMap<Integer, HashMap<Integer, Integer>> h = new HashMap<>();
		for(int i = 0; i < NMK[0]; i ++) h.put(i, new HashMap<>());
		for(int i = 0; i < NMK[1]; i++) {
			int[] uvc = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			h.get(uvc[1] -1).put(uvc[0] -1, Math.min(uvc[2], h.get(uvc[1] -1).getOrDefault(uvc[0] -1, Integer.MAX_VALUE)));
		}
		int[] t =  Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		PriorityQueue<long []> pq = new PriorityQueue<>(Comparator.comparing(x -> x[0]));
		for(int i : t) {
			pq.add(new long[] {0,i-1});
			distance[i-1] = 0;
		}
		while(!pq.isEmpty()) {
			long[] node = pq.poll();
			if(distance[(int) node[1]] < node[0]) continue;
			for(int key : h.get((int)node[1]).keySet()) {
				if(h.get((int)node[1]).get(key) + node[0] < distance[key]) {
					distance[key] = h.get((int)node[1]).get(key) + node[0];
					pq.add(new long[] {distance[key], key});
				}
			}
		}
		long[] sol = {0,0};
		for(int i = 0; i < NMK[0]; i++ ) {
			if(sol[1] < distance[i]) {
				sol[1] = distance[i];
				sol[0] = i;
			}
		}
		System.out.println(sol[0] + 1);
		System.out.println(sol[1]);
	}
	
	
}

