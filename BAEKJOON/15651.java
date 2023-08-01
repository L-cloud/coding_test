import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static StringBuilder sbb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        sbb = new StringBuilder();
        nCr(n,0,new int[r]);
        System.out.println(sbb.toString());
    }

    public static void nCr(int N, int index, int[] sb){
        if (sb.length == index){
            for(int i = 0; i<sb.length; i ++) sbb.append(sb[i] + " ");
            sbb.append("\n");
            return;
        }
        for(int i = 1; i <N+1; i++){
            sb[index] = i;
            nCr(N,index+1,sb);
        }
    }
}
