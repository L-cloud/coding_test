import java.util.*;
import java.util.stream.Collectors;
class Solution {
    public long solution(String expression) {
        long[] arr = Arrays.stream(expression.replaceAll("[^0-9]", " ").split(" ")).mapToLong(Long::parseLong).toArray();
        char[] oper = expression.replaceAll("[0-9]", "").toCharArray();
        char[][] order = {{'+', '-', '*'}, {'+', '*', '-'}, {'*', '-', '+'}, {'*', '+', '-'}, {'-', '*', '+'}, {'-', '+', '*'}};
        long val = 0;
        for (int i = 0; i < 6; i++) {
            List<Long> tarr = Arrays.stream(arr).boxed().collect(Collectors.toList());
            List<Character> toper = new String(oper).chars() .mapToObj(c -> (char) c).collect(Collectors.toList());
            for (int j = 0; j < 3; j++) {
                int cnt = getNum(toper, order[i][j]); // 사실 한 번만 하면 되는 연산을 엄청 많이 하는거라 사실..
                for (int l = 0; l < cnt; l++) {
                    for (int k = 0; k < toper.size(); k++) {
                        if (toper.get(k) == order[i][j]) {
                            // 바로 계산함 계산하는 함수 만들어야 겠다.
                            long c = cul(tarr.get(k), tarr.get(k + 1), order[i][j]);
                            toper.remove(k);
                            tarr.remove(k);
                            tarr.remove(k);
                            tarr.add(k, c);
                            break;
                        }
                    }
                }
            }
            val = Math.max(val, Math.abs(tarr.get(0)));
            }

        return val;
    }
    public  int getNum(List<Character> l, char o) {
		int cnt =0;
		for(int i = 0; i < l.size(); i ++) {
			if (l.get(i) == o) cnt ++;
		}
		return cnt;
	}
	
	public  long cul(long a, long b, char c) {
		if(c == '+') return a + b;
		if (c == '-') return a - b;
		return a * b;
	}
    
}
