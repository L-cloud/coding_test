import java.io.*;
import java.util.Arrays;

public class Main {
    static int[] ncr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ncr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        divide(0,(int)Math.pow(2,ncr[0]), 0,(int)Math.pow(2,ncr[0]), 0);
    }
    public static int divide(int l_r, int r_r, int l_c, int r_c, int index){
        if(r_r - l_r == 2){
            if(ncr[1] == l_r && ncr[2] == l_c) {
                System.out.println(index);
                System.exit(0);
            }
            if(ncr[1] == l_r && ncr[2] == l_c+1) {
                System.out.println(index+1);
                System.exit(0);
            }
            if(ncr[1] == l_r+1 && ncr[2] == l_c) {
                System.out.println(index+2);
                System.exit(0);
            }
            if(ncr[1] == l_r+1 && ncr[2] == l_c+1) {
                System.out.println(index+3);
                System.exit(0);
            }
            return index+4;
        }

        if(l_r <= ncr[1] && ncr[1] < (l_r +r_r)/2 && l_c <= ncr[2] && ncr[2] < (l_c + r_c)/2)divide(l_r,(l_r +r_r)/2,l_c,(l_c + r_c)/2,index);
        else index += ((l_r +r_r)/2 - l_r) * ((l_r +r_r)/2 - l_r);
        if(l_r <= ncr[1] && ncr[1] < (l_r +r_r)/2 && (l_c + r_c)/2 <= ncr[2] && ncr[2] < r_c) divide(l_r,(l_r +r_r)/2,(l_c + r_c)/2,r_c,index);
        else index += ((l_r +r_r)/2 - l_r) * ((l_r +r_r)/2 - l_r);
        if((l_r +r_r)/2 <=ncr[1] && ncr[1] <r_r && l_c <=ncr[2] && ncr[2] <(l_c + r_c)/2 ) divide((l_r +r_r)/2, r_r, l_c,(l_c + r_c)/2, index);
        else index += ((l_r +r_r)/2 - l_r) * ((l_r +r_r)/2 - l_r);
        if((l_r +r_r)/2 <=ncr[1] && ncr[1] <r_r && (l_c + r_c)/2 <=ncr[2] && ncr[2] < r_c ) divide((l_r +r_r)/2, r_r,(l_c + r_c)/2,r_c, index);
        else index += ((l_r +r_r)/2 - l_r) * ((l_r +r_r)/2 - l_r);
        return index;
    }
}


