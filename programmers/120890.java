class Solution {
    public int solution(int[] array, int n) {
        int min_abs = 1000;
        int m_v = array[0];
        for (int a : array){
            if (Math.abs(a-n) <= min_abs){
                if ((Math.abs(a-n) == min_abs)) m_v = (m_v < a) ? m_v : a;
                else m_v = a;
                min_abs = Math.abs(a-n);
            }
        }
        return m_v;
    }
}
