import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input =br.readLine().split(" ");
        double a = Integer.parseInt(input[0]);
        double b = Integer.parseInt(input[1]);
        double c = Integer.parseInt(input[2]);
        double d = Math.ceil(c / (a-b));
        double e = (a-b) *d; // d일 후 거리
        while (c <= e){
            d--;
            e = (a-b) * (d-1) + a;
        }
        System.out.println((int)d+1);
    }
}
