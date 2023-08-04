import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<String> hs = new HashSet<>();
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i<T;i++) {
        	hs.add(br.readLine());
        }
        while (true) {
            int max_v = 0;
            String max_s = "";
        	for(String s : hs) {
        		Pattern p = Pattern.compile("^" + s);
        		int t_v= 0;
        		String t_s = s;
        		for(String s2 : hs) {
        			if (p.matcher(s2).find()) t_v++;
        		}
        		if(max_v <t_v) {
        			max_v = t_v;
        			max_s = t_s;
        		}
        	}
        	if(max_v == 1) break;
        	hs.remove(max_s);
        }
        System.out.println(hs.size());
    }
    
}

