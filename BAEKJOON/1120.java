import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 String[] input = br.readLine().split(" ");
		 String big = input[0].length() >= input[1].length() ? input[0] : input[1];
		 String small = big.equals(input[0]) ? input[1] : input[0];
		 int min = small.length();
		 for(int i = 0; i < big.length() - small.length() + 1; i++) {
			 int t = 0;
			 for(int j = 0; j < small.length(); j ++) {
				if(big.charAt(j+i) != small.charAt(j)) t ++;
			 }
			 min = Math.min(t, min);
		 }
		 System.out.println(min);

	}

}

