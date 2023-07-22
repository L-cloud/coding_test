package com.test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer T = Integer.parseInt(br.readLine());
        int[] arr = new int[T];
        int avg = 0;
        HashMap<Integer, Integer> h= new HashMap<>();
        for(int i = 0; i<T; i++){
            arr[i] = Integer.parseInt(br.readLine());
            int v = h.getOrDefault(arr[i],0);
            h.put(arr[i], v + 1);
            avg += arr[i];
        }
        List<Integer> sortedList = new ArrayList<>(h.values());
        Collections.sort(sortedList);
        Arrays.sort(arr);
        List<Integer> l = new ArrayList<>();
        for (Integer k : h.keySet()){
            if (h.get(k) == sortedList.get(sortedList.size()-1)) l.add(k);
        }
        Collections.sort(l);

        int c = (l.size() > 1) ? l.get(1) : l.get(0);
        System.out.println(Math.round(avg/(float)T));
        System.out.println(arr[T/2]);
        System.out.println(c);
        System.out.println(arr[T-1] - arr[0]);
        // 최빈값 중 두 번째로 작은 값

    }
}

