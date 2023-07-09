import java.util.*;
import java.io.*;

public class BeeHouse {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer token = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(token.nextToken()) - 1;
        int cnt = 1;
        while (m > 0) {
            m -= 6 * cnt++;
        }
        System.out.println(cnt);
    }
}
