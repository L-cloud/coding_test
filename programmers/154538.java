import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        int ans = -1;
        HashSet<Integer> s = new HashSet<>();
        Deque<Integer> q = new ArrayDeque<>();
        q.add(x);
        while(!q.isEmpty()){
            ans ++;
            int size = q.size();
            for(int i = 0; i < size; i ++){
                int node = q.poll();
                if(node == y) return ans;
                if(node+n <= y && !s.contains(node + n)) add(node+n, s, q);
                if(node*2 <= y && !s.contains(node*2)) add(node*2, s, q);
                if(node*3 <= y && !s.contains(node*3)) add(node*3, s, q);
            }
        }
        return -1;
    }
    
    public void add(int x, HashSet<Integer> s, Deque<Integer> q ){
        if(!s.contains(x)){
              s.add(x);
              q.addLast(x);
        }
    }
}
