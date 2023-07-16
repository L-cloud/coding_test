import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input =br.readLine().split(" ");
        int ans = 32;
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);
        String[] a = new String[8];
        String[] b = new String[8];
        String[] m = new String[N];
        for (int i = 0; i<8; i++){
            if (i % 2 == 0) {
                a[i] = "WBWBWBWB";
                b[i] = "BWBWBWBW";
            }
            else{
                b[i] = "WBWBWBWB";
                a[i] = "BWBWBWBW";
            }
        }
        int t1,t2;
        for (int i = 0; i < N; i ++) m[i] = br.readLine();
        for (int i =0; i < N -7; i++){
            for (int j = 0; j< M-7; j++){
                t1 = compare(a,m,i,j);
                t2 = compare(b,m,i,j);
                ans = (ans < t1) ? ans : t1;
                ans = (ans < t2) ? ans : t2;
            }
        }
        System.out.println(ans);
    }


    public static int compare(String[] a, String[] b, int r, int c){
        int ans = 0;
        for (int i = 0; i < 8; i++){
            for (int j = 0; j< 8; j++){
                if (a[i].charAt(j) != b[i+r].charAt(j+c)) ans ++;
            }
        }
        return ans;
    }
}
