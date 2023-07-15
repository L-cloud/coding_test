import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];
        for (int i = 0; i <N;i++){
            String[] input = br.readLine().split(" ");
            arr[i][0] = Integer.parseInt(input[0]);
            arr[i][1] = Integer.parseInt(input[1]);
        }
        Integer[] rank = new Integer [N];
        Arrays.fill(rank, 1);
        int a,b;
        for (int i = 0; i < N; i++){
            a = arr[i][0];
            b = arr[i][1];
            for (int j = 0; j < N; j++){
                if (a < arr[j][0] && b < arr[j][1]) rank[i]++;
            }
        }
        for (Integer k : rank) System.out.print(k + " ");
    }
}
