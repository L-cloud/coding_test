class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String st = "";
        for (int s = 0; s < my_string.length(); s++){
            if (Character.isDigit(my_string.charAt(s))){
                st = st.concat(Character.toString(my_string.charAt(s)));
            }
            else{
                if (!st.equals("")){
                    answer += Integer.parseInt(st);
                    st = "";
                }
            }
            
        }
         if (!st.equals("")) answer += Integer.parseInt(st);
        
    return answer;
    }
}
