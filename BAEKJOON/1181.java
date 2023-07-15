import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer n = Integer.parseInt(br.readLine());
        Set<String> s = new HashSet<>();
        for (int i = 0; i<n; i++) s.add(br.readLine().toString());
        String[] arr = s.toArray(new String[s.size()]);
        Arrays.sort(arr, Comparator.comparing(String::length).thenComparing(Comparator.naturalOrder()));
        for(int i = 0; i <arr.length; i ++) System.out.println(arr[i]);
    }
}
