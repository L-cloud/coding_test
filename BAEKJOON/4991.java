import java.util.*;
import java.io.*;

public class Main {
    static int[] dx  = {-1,0,1,0};
    static int[] dy = {0,-1,0,1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] start = new int[2];
        while(true) {
            int[] nm = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            if(nm[0] == 0 && nm[1] == 0) break;
            char[][] arr = new char[nm[1]][];
            for(int i = 0 ; i < nm[1] ; i ++) arr[i] = br.readLine().replace(" ", "").toCharArray();
            int size = 1;
            for(int i = 0; i < nm[1]; i++) {
                for (int j = 0; j < nm[0]; j++) {
                    if (arr[i][j] == '*') {
                        arr[i][j] = (size + "").charAt(0);
                        size++;
                    }
                    if (arr[i][j] == 'o') {
                        start[0] = i;
                        start[1] = j;
                    }
                }
            }
            if (size!=0) System.out.println(logic(arr,start, --size));
            else System.out.println(0);
        }
    }

    public static int logic(char[][] arr,  int[] start, int k) {
        Deque<int []> q = new ArrayDeque<>();
        arr[start[0]][start[1]] = '.';
        HashSet<Integer>[][] v = new HashSet[arr.length][arr[0].length];
        for(int i = 0; i < arr.length; i ++){
            for(int j = 0; j < arr[1].length; j ++) v[i][j] = new HashSet<>();
        }
        v[start[0]][start[1]].add(0);
        q.add(new int [] {start[0], start[1], 1 }); // x,y, 방문 노드
        int turn = 0;
        while (!q.isEmpty()){
            turn++;
            int size = q.size();
            for(int i = 0 ; i < size; i ++){
                int[] node = q.poll();
                for(int j = 0; j < 4; j++){
                    int x = dx[j] + node[0];
                    int y = dy[j] + node[1];
                    if(0<=x && x< arr.length && 0<= y  && y<arr[0].length && arr[x][y] != 'x' && !v[x][y].contains(node[2])){
                        v[x][y].add(node[2]);
                        if(arr[x][y] != '.'){
                            int t = Character.digit(arr[x][y],10);
                            if ((1 << t | node[2]) == (1 << (k+1)) - 1) return turn; // 모두 방문
                            q.addLast(new int[]{x, y, 1 << t | node[2]});
                            v[x][y].add(1 << t | node[2]);
                            continue;
                        }
                        q.addLast(new int[] {x,y, node[2]});

                    }
                }
            }
        }

        return -1;
    }

}
