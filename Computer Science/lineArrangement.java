package com.SchoolWork.Assignment;


import java.util.Arrays;
import java.util.Scanner;

public class lineArrangement {
    public static void main(String args[]) {
        // read n
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        doublyLinkedList line = new doublyLinkedList();
        Node[] node_arr = new Node[n];
        line.add_first(node_arr);
        for (int i = 2; i < n + 1; i++) {
            int x = in.nextInt();
            int p = in.nextInt();
            line.insert(i, x, p, node_arr);
        }
        int[] value_arr = line.read(node_arr,n);
        int[] index_arr = new int[n];
        for (int index = 0; index < n; index++) {
            index_arr[value_arr[index]-1] = index;
        }
        int m = in.nextInt();
        for (int i = 0; i < m; i++) {
            int delete_num = in.nextInt();
            int index = index_arr[delete_num-1];
            value_arr[index] = -1;
        }
        for (int i = 0; i < n; i++) {
            if (value_arr[i] > 0){
                System.out.print(value_arr[i]+" ");
            }
        }

    }
}
class Node {
    public int data;
    public Node left;
    public Node right;

    public void displayNodeData() {
        System.out.println("{" + data + "}");
    }
}
class doublyLinkedList {
    public int head;
    public void add_first(Node[] node_arr) {
        Node newNode = new Node();
        newNode.data = 1;
        node_arr[0] = newNode;
        head = 1;
    }
    // read the whole list from the head
    public int[] read(Node[] node_arr, int n){
        Node head_node = node_arr[head-1];
        Node temp = head_node;
        int[] value_arr = new int[n];
        for (int i = 0; i < n-1; i++) {
            value_arr[i] = temp.data;
            temp = temp.right;
        }
        value_arr[n-1]=temp.data;
        return value_arr;
    }
    // insert a node according to x and p
    public void insert(int data, int previous, int p, Node[] node_arr) {
        Node target = node_arr[previous - 1];
        Node newNode = new Node();
        newNode.data = data;
        node_arr[data - 1] = newNode;
        if (p == 0) {
            newNode.right = target;
            if (target.left != null) {
                newNode.left = target.left;
                target.left.right = newNode;

            } else {
                head = data;
            }
            target.left = newNode;
        }
        if (p == 1) {
            newNode.left = target;
            if (target.right != null) {
                newNode.right = target.right;
                target.right.left = newNode;
            }
            target.right = newNode;
        }
    }
}



