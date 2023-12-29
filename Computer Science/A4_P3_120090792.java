package com.SchoolWork.Assignment;
import java.util.*;
public class A4_P3_120090792 {
    // Build 2-dimension arrays to store the vertices' distances => cols: known, d, p
    public static int[][] disArray;
    public static int INF = 10000000;

    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        // Read N and R
        int n = in.nextInt();
        int r = in.nextInt();
        // Build 3-dimension arrays of LinkedList to store the graph structure
        PriorityQueue<Integer>[][] graph = new PriorityQueue[n+1][n+1];
        int maxDis = 0;
        for (int i = 1; i <= r; i++) {
            int a = in.nextInt();
            int b = in.nextInt();
            int d = in.nextInt();
            if (d >= maxDis){
                maxDis = d;
            }
            if (graph[a][b]==null){
                graph[a][b] = new PriorityQueue<Integer>();
            }
            if (graph[b][a]==null){
                graph[b][a] = new PriorityQueue<Integer>();
            }
            graph[a][b].add(d);
            graph[b][a].add(d);
        }
        // Find the second shortest path
        Dijkstra2(graph,1,n);
        System.out.println(disArray[n][2]);
    }

    public static void Dijkstra2(PriorityQueue<Integer>[][] graph, int source, int n){
        // Read Graph and record maximum distance
        initializeSingleSource(source, n);
        // Priority Queue for shortest
        PriorityQueue<Integer> tempQ1 = new PriorityQueue<Integer>(new CustomComparator1());
        // Priority Queue for 2nd shortest
        PriorityQueue<Integer> tempQ2 = new PriorityQueue<Integer>(new CustomComparator2());
        for (int i = 1; i <= n; i++) {
            tempQ1.add(i);
            tempQ2.add(i);
        }
        // Find shortest path
        int u1 = 1;
        int count = 0;
        while (!tempQ1.isEmpty()){
            count += 1;
            u1 = tempQ1.poll();
            for (int i = 1; i <= n; i++) {
                if (graph[u1][i] != null){
                    // Find if shorter adjacent path exists
                    relax1(graph[u1][i], u1, i, tempQ1, n, count);
                }
            }
        }
        // Find Second shortest path
        int u2 = 1;
        count = 0;
        while (!tempQ2.isEmpty()){
            count += 1;
            u2 = tempQ2.poll();
            for (int i = 1; i <= n; i++) {
                if (graph[u2][i] != null){
                    // Find if shorter adjacent path exists
                    relax2(graph[u2][i], u2, i, tempQ2, n, count);
                }
            }
        }
    }


    public static void initializeSingleSource(int s, int n){
        disArray = new int[n+1][3]; // Distance1, p1, Distance2, p2
        for (int v = 1; v <= n; v++) {
            if (v != s){
                disArray[v][1] = INF; // initialize distance1 to infinity
                disArray[v][2] = INF; // initialize distance2 to infinity
            } else {
                disArray[v][1] = 0;
                disArray[v][2] = 0;
            }
        }
    }
    static class CustomComparator1 implements Comparator<Integer> {
        // Compare Distance
        @Override
        public int compare(Integer node1, Integer node2) {
            Integer d1 = disArray[node1][1];
            Integer d2 = disArray[node2][1];
            if (d1 - d2 < 0) {
                return -1;
            }
            else if (d1 - d2 > 0) {
                return 1;
            }
            else {
                return 0;
            }
        }
    }
    static class CustomComparator2 implements Comparator<Integer> {
        // Compare Distance
        @Override
        public int compare(Integer node1, Integer node2) {
            Integer d1 = disArray[node1][2];
            Integer d2 = disArray[node2][2];
            if (d1 - d2 < 0) {
                return -1;
            }
            else if (d1 - d2 > 0) {
                return 1;
            }
            else {
                return 0;
            }
        }
    }
    public static void relax1(PriorityQueue<Integer> adjacentList, int u, int v, PriorityQueue tempQ,int n, int itr){
        // catch element polled from adjacentList
        Stack<Integer> copy = new Stack();
        while (!adjacentList.isEmpty()){
            int w = adjacentList.poll();
            copy.push(w);
            if (disArray[v][1] > disArray[u][1] + w) {
                if (itr != n){
                    tempQ.remove(v);
                    disArray[v][1] = disArray[u][1] + w;
                    tempQ.add(v);// Update Priority Queue
                } else {
                    disArray[v][1] = disArray[u][1] + w;
                }
            }
        }
        while (!copy.isEmpty()){
            adjacentList.add(copy.pop());
        }

    }
    public static void relax2(PriorityQueue<Integer> adjacentList, int u, int v, PriorityQueue<Integer> tempQ,int n, int itr){
        // catch element polled from adjacentList
        Stack<Integer> copy = new Stack();
        while (!adjacentList.isEmpty()){
            int w = (int) adjacentList.poll();
            copy.push(w);
            if (disArray[v][1] < disArray[u][1] + w && disArray[u][1] + w< disArray[v][2] ){
                if (itr != n){
                    tempQ.remove(v);
                    disArray[v][2] = disArray[u][1] + w;
                    tempQ.add(v);
                } else {
                    disArray[v][2] = disArray[u][1] + w;
                }
            } else if (disArray[v][1] < disArray[u][2] + w && disArray[u][2] + w< disArray[v][2]){
                if (disArray[u][1] + 3*w > disArray[u][2] + w){
                    if (itr != n){
                        tempQ.remove(v);
                        disArray[v][2] = disArray[u][2] + w;
                        tempQ.add(v);
                    } else {
                        disArray[v][2] = disArray[u][2] + w;
                    }
                } else {
                    if (itr != n){
                        tempQ.remove(v);
                        disArray[v][2] = disArray[u][1] + 3*w;
                        tempQ.add(v);
                    } else {
                        disArray[v][2] = disArray[u][1] + 3*w;
                    }
                }
            } else if (disArray[v][1] < disArray[u][1] + 3*w && disArray[u][1] + 3*w< disArray[v][2]){
                if (itr != n){
                    tempQ.remove(v);
                    disArray[v][2] = disArray[u][1] + 3*w;
                    tempQ.add(v);
                } else {
                    disArray[v][2] = disArray[u][1] + 3*w;
                }
            }
        }
        while (!copy.isEmpty()){
            adjacentList.add(copy.pop());
        }
    }
    public static void printgraph(PriorityQueue[][] graph){
        for (int i = 0; i < graph.length; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                if (graph[i][j] != null){
                    System.out.print(graph[i][j].peek()+" ");
                } else{
                    System.out.print(0+" ");
                }
            }
            System.out.println("");
        }
    }
}
