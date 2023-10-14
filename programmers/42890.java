import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Arrays;
class Solution {
    public int solution(String[][] relation) {
       // 비트 연산 하면 됨!!
        HashSet<Integer> keys = new HashSet<>();
        int cnt = 0;
        for(int i = 1; i <= relation[0].length; i ++){
            cnt += sol(i,keys,relation);
        }
        return cnt;
    }
    
    public int sol(int size, HashSet<Integer> keys, String[][] relation){
        int[] arr = new int[size];
        List<int[]> k= new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int cnt = 0;
        dfs(relation[0].length,0,0,arr,k);
        for(int [] irr : k){
            int t = 1 << relation[0].length;
            for(int i : irr) t = t | (1 << i);
            if (!isv(t,keys)) continue;
            HashSet<String> hs = new HashSet<>();
            for(String[] s : relation){
                sb.setLength(0);
                for(int i : irr){
                    sb.append(s[i] + "-");
                }
                hs.add(sb.toString());
            }
            if(relation.length == hs.size()){
                cnt ++;
                keys.add(t);
            }
        }
        return cnt;
    }
    
    public void dfs(int size, int start,int index, int[] arr, List<int []> r){
        if (index == arr.length){
            r.add(arr.clone());
            return;
        }
        for(int i = start; i < size; i ++){
            arr[index] = i;
            dfs(size,i + 1, index + 1, arr, r);
        }
    }
    public boolean isv(int t, HashSet<Integer> keys){
      for(int key : keys){
            if ((key & t) == key || (key & t) == t) {// 하나라도 겹침
                return false;
            } 
        }
        return true;
    }
}
