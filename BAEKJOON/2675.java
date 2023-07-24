import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i=0; i<T;i++){
            StringTokenizer tr = new StringTokenizer(br.readLine());
            StringBuilder sb = new StringBuilder();
            int r = Integer.parseInt(tr.nextToken());
            String str = tr.nextToken();
            for(int j = 0 ; j <str.length(); j++){
                for(int k = 0; k<r; k++){
                    sb.append(Character.toString(str.charAt(j)));
                }
            }
            System.out.println(sb.toString());
            sb.setLength(0);
        }

    }
}

