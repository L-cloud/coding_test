package com.test;

import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " "); // 일단 한 줄 다 읽고 한 글자씩
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        M = (N-M >= M) ? M : N-M;
        int i = 1;
        int j = 1;
        for (int l=1;l<M+1;l++){
            i *= N--;
        }
        for (int l = 1; l <M+1; l++){
            j *= l;
        }
        System.out.println(i/j);


    }
}
