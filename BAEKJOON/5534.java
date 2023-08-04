import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        String s = br.readLine();
        int ans = 0;
        for(int i = 0; i<T;i++) {
        	String t = br.readLine();
        	for(int j = 1; j < t.length(); j ++) {
        		int tcnt = 0;
        		for(int k : start(s,t)) {
        			tcnt = 0;
        			for(int u =k; u < t.length(); u+=j) {
        				if (tcnt == s.length()) break;
        				if( s.charAt(tcnt) == t.charAt(u)) {
        					tcnt++;
        					continue;
        				}
        				break;
        			}
        			if (tcnt == s.length()) break;
        		}	
        		if (tcnt == s.length()) {
        			ans ++;
        			break;
        		}
        	}
        }
      System.out.println(ans);
    }
    
    public static List<Integer> start (String a, String b){
    	List<Integer> l = new LinkedList<>();
    	for(int i = 0; i < b.length(); i ++) {
    		if(b.charAt(i) == a.charAt(0)) {
    			l.add(i);
    		}
    	}
    	return l;
    }

}

