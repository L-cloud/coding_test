
import java.io.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true){
            String input = br.readLine();
            if (input.equals("0")) break;
            String ans = check(input) ? "yes" : "no";
            System.out.println(ans);

        }
    }

    public static boolean check(String s){
        int left, right;
        left = 0;
        right = s.length() -1;
        while (left <= right){
            if (s.charAt(left++) != s.charAt(right--)) return false;
        }
        return true;
    }

}
