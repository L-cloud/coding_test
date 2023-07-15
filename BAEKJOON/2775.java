import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int k,n;
        for (int i = 0; i< T; i ++){
            k = Integer.parseInt(br.readLine());
            n = Integer.parseInt(br.readLine());
            System.out.println(solve(k,n));
        }
    }

    public static int solve(int k, int n){
        int [][] apart = new int[k+1][n];
        for (int i = 0; i < n; i++) apart[0][i] = i+1;
        for (int i = 1; i < k+1; i++){
            for (int j = 0; j < n; j++){
                if (j == 0) apart[i][j] = apart[i-1][j];
                else apart[i][j] = apart[i-1][j] + apart[i][j-1];
            }
        }
        return apart[k][n-1];
    }

}
