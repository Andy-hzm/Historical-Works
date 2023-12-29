package com.SchoolWork.Assignment;

import java.util.*;

public class A4_P4_120090792 {
    public static double[][] graph;
    public static double[][] cor;
    public static double[] primArray;
    public static int n;
    public static int c;
    public static double maxDis;
    public static double INF = 10000000;

    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        // read n and c
        n = in.nextInt();
        c = in.nextInt();
        // read coordinate
        cor = new double[n+1][3];
        for (int i = 1; i <= n; i++) {
            double x = in.nextInt();
            cor[i][1] = x;
            double y = in.nextInt();
            cor[i][2] = y;
        }
        // store the graph
        graph = new double[n+1][n+1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                // ith point
                double xi = cor[i][1];
                double yi = cor[i][2];
                // jth point
                double xj = cor[j][1];
                double yj = cor[j][2];
                // Calculate distance and record maximum distance
                double dis = Math.pow(xi-xj,2) + Math.pow(yi-yj,2);
                if (dis < c) {
                    dis = INF;
                }
                // store the available edges
                graph[i][j] = dis;
                graph[j][i] = dis;
            }
        }
        // prim algorithm
        System.out.println((int) primAlgorithm(1));

    }
    public static double primAlgorithm(int root){
        // Exclude no answer
        for (int i = 1; i <= n; i++) {
            boolean flag = false;
            for (int j = 1; j <= n; j++) {
                if (graph[i][j]!=INF){
                    flag = true;
                    break;
                }
            }
            if (!flag){
                return -1;
            }
        }
        // Look for answer
        double total_weight = 0;
        // build min-heap for travelling
        PriorityQueue<Integer> Q = new PriorityQueue(new primDistanceComparator());
        // prepare array to store key
        primArray = new double[n+1];
        for (int u = 1; u <= n; u++) {
            primArray[u] = INF;
            Q.add(u);
        }
        // update root key
        Q.remove(root);
        primArray[root] = 0;
        Q.add(root);
        // update the following
        boolean[] leftover = new boolean[n+1];
        for (int i = 1; i <= n; i++) {
            leftover[i] = true;
        }
        while (true) {
            int u = Q.poll();
            leftover[u] = false;
            if (Q.isEmpty()) {
                break;
            }
            for (int v = 1; v <= n; v++) {
                if (graph[u][v] != 0) {
                    // reach adjacent point
                    if (leftover[v] && graph[u][v] < primArray[v]) {
                        Q.remove(v);
                        primArray[v] = graph[u][v];
                        Q.add(v);
                        // Record min weight of the new added
                    }
                }
            }
            double min = INF;
            for (int i = 1; i <= n; i++) {
                if (leftover[i] && primArray[i] < min){
                    min = primArray[i];
                }
            }
            total_weight += min;
        }
        return total_weight;
    }

    static class primDistanceComparator implements Comparator<Integer> {
        // Compare Distance
        @Override
        public int compare(Integer n1, Integer n2) {
            double d1 = primArray[n1];
            double d2 = primArray[n2];
            if (d1 > d2){
                return 1;
            } else if (d1 < d2){
                return -1;
            } else {
                return 0;
            }
        }
    }
    public static void printGraph(){
        for (int i = 0; i < graph.length; i++) {
            System.out.println(Arrays.toString(graph[i]));
        }
    }
}
