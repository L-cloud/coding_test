class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1) return new int [] {-1};
        int[] answer = new int[arr.length -1];
        int min_val = (int)Math.pow(2,31) -1;
        for (int a : arr) min_val = (min_val < a) ? min_val : a;
        int index = 0;
        for (int i = 0; i < arr.length; i ++){
            if (arr[i] != min_val){
                answer[index++] = arr[i];
            }
        }
        return answer;
    }
}
