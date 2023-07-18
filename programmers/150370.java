import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        String[] t = today.split("\\.");
        int i =0;
        HashMap<String, Integer> h = new HashMap<>();
        int[] today_int = {Integer.parseInt(t[0]),  Integer.parseInt(t[1]),  Integer.parseInt(t[2])};
        for (String term : terms){
            String[] t_term = term.split(" ");
            h.put(t_term[0],Integer.parseInt(t_term[1]));
        }
        int order = 1;
        List<Integer> answer = new ArrayList<>();
        for (String privacy : privacies){
            String[] p = privacy.split(" ");
            int[] date = get_date(p[0]);
            if (! cal(today_int, date, h.get(p[1]))) {
                answer.add(order);
            }
            order++;
        }
        int [] ans = answer.stream().mapToInt(Integer::intValue).toArray();
        return ans ;
    }
    
    public int[] get_date(String term){
        
        String[] t = term.split("\\.");
        return new int[] {Integer.parseInt(t[0]),Integer.parseInt(t[1]),Integer.parseInt(t[2])};
    }
    public boolean cal(int[] a, int[] b, int c){
        b[0] += c / 12;
        c %= 12;
        int d = (b[1] + c > 12)? 1 : 0;
        b[1] = (b[1] + c > 12)? b[1] + c- 12 : b[1] + c;
        b[0] += d;
        if (a[0] < b[0]) return true;
        else if (a[0] == b[0] && a[1] < b[1]) return true;
        else if (a[0] == b[0] && a[1] == b[1] && a[2] < b[2]) return true;
        return false;
    }
}
