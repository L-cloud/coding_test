import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer T = Integer.parseInt(br.readLine());
        for(int i =0; i <T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
            Deque<Integer[]> dq = new ArrayDeque<>();
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j <N; j++){
                Integer a = Integer.parseInt(st.nextToken());
                dq.add(new Integer[] {a,j});
                pq.add(a);
            }
            int index =0;
            while (true){
                if (dq.peek()[0] == pq.peek()){
                    if(dq.peek()[1] == M){
                        System.out.println(++index);
                        break;
                    }
                    index++;
                    dq.pollFirst();
                    pq.poll();
                }
                else{
                    dq.add(dq.pollFirst());
                }
            }




        }
    }
}
