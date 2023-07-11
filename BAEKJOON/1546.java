import java.io.*;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String [] a = br.readLine().split(" ");
        Float[] arr = new Float[N];
        for (int i =0; i< N; i++) arr[i] = Float.parseFloat(a[i]);
        Arrays.sort(arr);
        float avg = 0;
        for (int i = 0; i < N; i++) {
            arr[i] = arr[i] / arr[arr.length-1] * 100;
            avg += arr[i];
        }
        System.out.println(avg/N);
    }
}
