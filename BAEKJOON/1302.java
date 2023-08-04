import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        HashMap<String, Integer> h = new HashMap<>();
        for(int i = 0; i < t; i ++){
            String a = br.readLine();
            int c = h.getOrDefault(a,0);
            h.put(a,c+1);
        }
        String[] a = h.keySet().toArray(new String[0]);
        Arrays.sort(a, Comparator.comparing((String x) -> h.get(x)).thenComparing(Comparator.reverseOrder()));
        System.out.println(a[a.length -1]);
    }
}
