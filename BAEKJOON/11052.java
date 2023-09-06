import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input= br.readLine().split(" ");
        int[] arr = new int[n + 1];
        for (int i = 0; i < n; i++) arr[i + 1] = Integer.parseInt(input[i]);
        int[] dp = Arrays.stream(arr, 0, n + 1).toArray();
        for(int i = 1; i <= n; i ++){
            for(int j = 1; j < i; j ++){
                dp[i] = Math.max(dp[i], dp[i-j] + arr[j]);
            }
        }
        System.out.println(dp[n]);
    }
}

