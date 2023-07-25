import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	Integer N = Integer.parseInt(br.readLine());
    	int [] m = new int[N];
    	System.out.println(dfs(0,m));
    }
    
    public static int dfs(int index, int[] m) {
    	int cnt = 0;
    	if (index == m.length) return 1;
    	for(int i=0;i<m.length;i++) {
    		if (!row(index,i,m)) continue;
    		if(!dia1(index,i,m)) continue;
    		if(!dia2(index,i,m)) continue;
    		m[index] = i;
    		cnt += dfs(index+1,m);
    	}
    	return cnt;
    }
    
    public static boolean row(int index,int t ,int[] m) { 	// 가로 확인
    	for(int i = 0; i < index; i++) { 
    		if (m[i] == t) return false;
    	}
    	return true;
    }
    public static boolean dia1(int index, int t, int[] m) { // 대각선 왼쪽 위
    	int i = index -1;
    	int j = t -1;
    	while(0<=i && 0<=j) {
    		if(m[i --] == j --) return false;
    	}
    	return true;
    }
    public static boolean dia2(int index, int t, int[] m) { // 대각선 왼쪽 아래
    	int i = index -1;
    	int j = t+1;
    	while(0<=i && j < m.length) {
    		if(m[i--] == j++) return false;
    	}
    	return true;
    }
}
