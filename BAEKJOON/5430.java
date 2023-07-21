import java.io.BufferedReader;
import java.util.Deque;
import java.util.LinkedList;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
class Main
{
    public static void main(String args[]) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for(int l =0; l < T; l++) {
			String cmd = br.readLine();
			int len = Integer.parseInt(br.readLine());
			Deque<Integer> dq = new LinkedList<>();
			String s_arr = br.readLine();
			Pattern p = Pattern.compile("(100|[1-9][0-9]?)");
			Matcher m = p.matcher(s_arr);
			boolean flag = true;
			int r = 0; // 이거 홀수냐 짝수냐에 따라 앞에서 뺄지 뒤에서 뺄지 결정 ㄱ
			while(m.find()) {
				dq.addLast(Integer.parseInt(m.group()));
			}
			for(int i = 0; i <cmd.length(); i++) {
				if(cmd.charAt(i) == 'R') {
					r = (r+1) % 2;
				}
				else { // 빼야함
					if( 0 < dq.size()) {
						if (r % 2 == 0) { // 짝수는 현재 순서로
							dq.removeFirst();
						}
						else {
							dq.removeLast();
						}
					}
					else {
						System.out.println("error");
						flag = false;
						break;
					}
				}
			}
			if(flag) {
				StringBuilder sr = new StringBuilder();
				sr.append("[");
				int size = dq.size();
				for(int i = 0; i<size; i++) {
					if(r % 2 == 0) { // 역순 아님
						sr.append(String.valueOf(dq.removeFirst()));
					}
					else sr.append(String.valueOf(dq.removeLast()));
					if(i + 1 != size) sr.append(",");
				}
				sr.append("]");
				System.out.println(sr.toString());
			}
			
		}
    }
    
}
