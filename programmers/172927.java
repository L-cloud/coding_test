import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
class Solution {
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        List<HashMap<String, Integer>> h = new ArrayList<>();
        for(int i = 0; i < 3; i++) h.add(new HashMap<>());
        h.get(0).put("diamond", 1); 
        h.get(0).put("iron", 1);
        h.get(0).put("stone", 1);
        h.get(1).put("diamond", 5); 
        h.get(1).put("iron", 1);
        h.get(1).put("stone", 1);
        h.get(2).put("diamond", 25); 
        h.get(2).put("iron", 5);
        h.get(2).put("stone", 1);
        return dfs(picks,minerals,h,0,0);
    }
    
    public int dfs(int[] picks, String[] minerals, List<HashMap<String, Integer>> h,int m_index, int ans){
        int res = 1250;
        if(minerals.length == m_index) return ans;
        for(int j = 0; j < 3; j++){
            if (picks[j] <= 0) continue;
            picks[j]--;
            int t = ans;
            for(int i = m_index; i < m_index + 5; i ++){
                if (minerals.length <= i) continue;
                t += h.get(j).get(minerals[i]);
            }
            if(m_index + 5 < minerals.length){ 
                res = Math.min(dfs(picks,minerals,h,m_index+5,t),res);
            }
            else{
                res = Math.min(res,t);
            }
            picks[j]++;
        }
        return (picks[0] == 0 && picks[1] == 0 && picks[2] ==0) ? ans : res;
    }
}
