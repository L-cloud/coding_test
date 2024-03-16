import java.util.HashMap;
import java.util.ArrayList;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] r = new int[] {0,0}; 
        HashMap <Integer, ArrayList<Integer>> h = new HashMap<>();
        for (int i =0; i < nums.length; i ++){
            ArrayList<Integer> arr = h.containsKey(nums[i]) ? h.get(nums[i]) : new ArrayList<Integer> ();
            arr.add(i);
            h.put(nums[i], arr);
        }

        for(int num : nums){
            if (h.containsKey(target - num)){
                if (target-num == num){
                   if(h.get(num).size() >= 2){
                    r[0]  = h.get(num).get(0);
                    r[1] = h.get(num).get(1);
                    return r;
                    }
                }
                else{
                    r[0] = h.get(num).get(0);
                    r[1] = h.get(target-num).get(0);
                    return r;
                }
            }
        }
        return r;
    }
}
