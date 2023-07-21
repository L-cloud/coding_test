import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
class Main
{
    public static void main(String args[]) throws Exception{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int T = Integer.parseInt(br.readLine());
    	
    	for(int k = 0; k <T; k++) {
    		int n  = Integer.parseInt(br.readLine());
    		HashMap<String, Integer> h = new HashMap<String,Integer>();
    		String[] str = br.readLine().split(" "); 
    		for(int i = 0; i <n;i++) {
    			int num = h.getOrDefault(str[i], 0);
    			h.put(str[i], num+1);
    		}
    		System.out.println(dfs(h,0,new String [3])); 
    		
    	}
    }
    
    public static int dfs(HashMap<String, Integer> h , int index, String[] str) {
    	if (index == 3) return cal(str);
    	int ans = 24;
    	for(String key : h.keySet()) {
    		if(h.get(key) > 0) {
    			h.put(key, h.get(key) -1);
    			str[index] = key;
    			ans = Math.min(ans,dfs(h,index+1,str));
    			h.put(key, h.get(key) + 1);
    		}
    	}
    	return ans;
    }
    
    public static int cal(String[] str) {
    	int s = 0;
    	for(int i = 0; i < 3; i ++) {
    		for(int j =i+1; j < 3; j ++) {
    			for(int k = 0; k < 4; k++) {
    				if(str[i].charAt(k) != str[j].charAt(k)) {
    					s++;
    				}
    			}
    		}
    	}
    	return s;
    }

}
