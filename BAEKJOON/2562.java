import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        for(int i = 0; i < 9; i ++){
            arr[i] = Integer.parseInt(br.readLine());
        }
        int index = 0;
        int max_value = 0;
        for(int i = 0; i < 9; i ++){
            if (max_value < arr[i]){
                index = i + 1;
                max_value = arr[i];
            }
        }
        System.out.println(max_value);
        System.out.println(index);

    }
}

