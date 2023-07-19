import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.PriorityQueue;
import java.util.Arrays;
import java.util.Comparator;
class Main
{
    public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] mat = new int [101];
        for(int i = 1; i < 101; i++) mat[i] = i;
        for (int i =0; i< N; i++) {
        	st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            mat[a] = b;
        }
        for(int i = 0; i<M; i ++) {
        	st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            mat[a] = b;
        }
        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(x -> x[0])); 
        int [] v = new int[101];
        Arrays.fill(v, 100);
        q.offer(new int []{0,1});
        while(true) {
        	int [] node = q.poll();
        	if (node[1] == 100) {
        		System.out.println(node[0]);
        		break;
        	}
        	for(int i = 1; i<7;i++) {
        		if (node[1] + i < 101) {
        		int x = mat[node[1] + i];
        		if(node[0] + 1 < v[x]) {
        			v[x] = node[0] + 1;
        			q.offer(new int[] {node[0] +1 ,x});
        		}
    		}
        	}
        }
        
        

    }
}
