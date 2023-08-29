import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i ++){
            System.out.println(nCr(Arrays.stream(br.readLine().split(" ")).mapToLong(Long::parseLong).toArray()));
        }
    }


    public static long nCr(long[] arr){
        long n = arr[1];
        long c = arr[0] < arr[1]  - arr[0] ? arr[0] : arr[1] - arr[0];
        long s = 1;
        for(int i = 0; i <c;  i++){
            s *= n;
            n--;
        }
        for(int i = 2; i <= c; i ++){
            s /= i;
        }
        return s;
    }
}
