package com.SchoolWork.Assignment;

import java.util.LinkedList;
import java.util.Scanner;

public class A4_P2_120090792 {
    public static void main(String args[]){
        // Read the number of datasets
        Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        // prepare output storage
        LinkedList[] output = new LinkedList[T];
        // Main body
        for (int i = 0; i < T; i++) {
            // Main Body of each dataset
            int n = in.nextInt();
            int[] raw = new int[n+1];
            // record input
            int min = 2^31-1;
            int max = -2^31+1;
            for (int j = 1; j <= n; j++) {
                int num = in.nextInt();
                if (num > max){
                    max = num;
                }
                if (num < min){
                    min = num;
                }
                raw[j] = num;
            }
            if (max == min){
                output[i] = new LinkedList<Integer>();
                output[i].addLast(min);
            }else{
                // prepare hashing function
                int range = 70001;
                LinkedList<Integer>[] hash = new LinkedList[range];
                // hashing
                for (int j = 1; j <= n; j++) {
                    int num = raw[j]-min;
                    int f = num % range;
                    if (hash[f] == null){
                        hash[f] = new LinkedList();
                    }
                    int index = hash[f].indexOf(num);
                    if (index == -1){
                        if (output[i] == null){
                            output[i] = new LinkedList<Integer>();
                        }
                        output[i].addLast(num+min);
                        hash[f].add(num);
                    }
                }
            }
        }
        // Output
        for (int i = 0; i < T; i++) {
            while (!output[i].isEmpty()){
                int element = (int) output[i].pollFirst();
                System.out.print(element+" ");
            }
            System.out.println("");
        }
    }

}
