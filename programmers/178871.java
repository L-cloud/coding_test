import java.util.HashMap;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<Integer,String> rankNum = new HashMap<>();
        HashMap<String,Integer> rankName = new HashMap<>();
        for(int i = 0; i < players.length; i++){
            rankNum.put(i,players[i]);
            rankName.put(players[i],i);
        }
        for(String call : callings){
            int rank = rankName.get(call);
            String t =  rankNum.get(rank-1);
            rankNum.put(rank-1,call);
            rankName.put(call,rank-1);
            rankNum.put(rank,t);
            rankName.put(t,rank);
        }
        String[] answer = new String[players.length];
        for(int i = 0; i < answer.length; i++){
            answer[i] = rankNum.get(i);
        }
        return answer;
    }
}
