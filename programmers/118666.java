import java.util.*;
class Solution {
    public String solution(String[] survey, int[] choices) {
        HashMap<String,Integer> h = new HashMap<>();
        h.put("R",0);
        h.put("T",0);
        h.put("C",0);
        h.put("F",0);
        h.put("J",0);
        h.put("M",0);
        h.put("A",0);
        h.put("N",0);
        int index = 0;
        for(String str : survey){
            cal(h, str.substring(0,1),  str.substring(1,2), choices[index++]);
            }
    StringBuilder br = new StringBuilder();
    make(br,h);  
    return br.toString();    
    }
    public void cal(HashMap<String, Integer> h, String a, String b, int c)
    {
        
        if (c >4) { // a가 비동의 해야 점수 얻음 c가 4보다 크면 b가 점수 얻음
            h.put(b,h.get(b) +c -4);
        }
        else if (c <4) {
            int[] grade = {3,2,1};
            h.put(a,h.get(a) + grade[c-1]);
        }
    }
    
    public void make(StringBuilder br, HashMap<String, Integer> h){
        if(h.get("R") < h.get("T")) br.append("T");
        else br.append("R");
        if(h.get("C") < h.get("F")) br.append("F");
        else br.append("C");
        if(h.get("J") < h.get("M")) br.append("M");
        else br.append("J");
        if(h.get("A") < h.get("N")) br.append("N");
        else br.append("A");
    }
}
