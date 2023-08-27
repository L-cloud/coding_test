class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] arr = new int[rows][columns];
        for(int i = 0; i < rows; i ++){
            for(int j = 0; j < columns; j++){
                arr[i][j] = i *columns + j + 1; // 배열 초기화
            }
        }
        int[] answer = new int [queries.length];
        int index =0;
        for(int[] query : queries){
            answer[index++] = rotate(arr,query[0] -1 ,query[1] -1 , query[2] -1 , query[3] -1);
        }
        
    
        return answer;
    }
    
    
    public int rotate(int[][] arr, int x1, int y1, int x2, int y2){ // 입력 받을 때 1씩 빼서 오도록 하자!
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};
        int n = (x2-x1 + 1) * 2 + (y2-y1+ 1) * 2 - 4;
        int index = 0;
        int x = x1;
        int y = y1;
        int prev = arr[x1][y1];
        int min = prev;
        int next = 0;
        while( n > 0){
            int r = x + dx[index];
            int c = y + dy[index];
            if(x1<=r && r<=x2 && y1<=c && c<=y2 ){ // 범위 내라면
                next = arr[r][c];
                min = Math.min(min,next);
                arr[r][c] = prev;
                prev = next;
                x += dx[index];
                y += dy[index];
                n --;
                continue;
            }
            index ++; // 범위 벗어났으니 방향 전환
        }
        return min;
    }
}
