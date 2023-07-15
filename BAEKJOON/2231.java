import java.io.*;
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        int ans = 0;
        while (make(ans++) != n && ans <= n){}
        ans = n == make(ans-1) ? ans -1 : 0;
        System.out.println(ans);
    }

    public static int make(int num){
        String str = String.valueOf(num);
        for (int i = 0; i < str.length(); i ++){
            num += Character.getNumericValue(str.charAt(i));
        }
        return num;
    }
}
