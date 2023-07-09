import java.util.*;
import java.io.*;

public class Triangle {
    static boolean check(String[] arr){
        int a = (int)Math.pow(Integer.parseInt(arr[0]), 2);
        int b = (int)Math.pow(Integer.parseInt(arr[1]), 2);
        int c = (int)Math.pow(Integer.parseInt(arr[2]), 2);
        if (a + b == c) return true;
        else if (a + c  == b) return true;
        else if (b + c == a) return true;
        return false;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] st = {"0", "0", "0"};
        while (true) {
            String[] arr = br.readLine().split(" ");
            if (Arrays.equals(st, arr)) break;
            if (check(arr)) bw.write("right");
            else bw.write("wrong");
            bw.newLine();
            bw.flush();
        }
    }
}


