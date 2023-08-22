import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        quicksort(0,nm[0] -1,arr);
        System.out.println(arr[nm[0] - nm[1]]);
    }

    public static void quicksort(int start, int end, int[] arr){
        if(start >= end) return;
        int left = start;
        int right = end;
        while(left < right){
            while(left<right && arr[left] <= arr[start]) left++;
            while(left<=right && arr[start] <= arr[right]) right --;
            if(left < right) swap(left,right,arr);
        }
        swap(start,right,arr);
        quicksort(start,right-1,arr);
        quicksort(right+1,end,arr);
    }
    public static void swap(int i, int j, int[] arr){
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }
}
