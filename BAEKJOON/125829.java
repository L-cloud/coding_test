import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> hash = new HashMap<>();
        int i = 0;
        for (char c = 'a'; c<= 'z'; c++) hash.put(String.valueOf(c),++i);
        Long n = Long.valueOf(br.readLine());
        String abc = br.readLine();
        System.out.println(make(hash,abc) );
    }

    public static long make(HashMap<String,Integer> hash,String str){
        long ans = 0;
        for (int i = 0; i < str.length(); i ++){
            ans += hash.get(String.valueOf(str.charAt(i))) * p(i) % 1234567891;
            ans %= 1234567891;
        }
        return ans;
    }

    public static long p(int i){
        long t = 1;
        while (i > 0){
            t *= 31;
            t %= 1234567891;
            i--;
        }
        return t;
    }
}
