package com.SchoolWork.Assignment;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SBT {
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        // read n
        int n = in.nextInt();
        // read weight in node i
        int[] weightList = new int[n+1];
        for (int i = 1; i <= n; i++) {
            weightList[i] = in.nextInt();
        }
                               // read child [left,right,left,right...]
        int[] childList = new int[2*n+1];
        for (int i = 1; i <= 2*n; i++) {
            childList[i] = in.nextInt();
        }
        // Main body
        TreeNode[] treeArray = new TreeNode[n+1];
        TreeNode root = new TreeNode();
        root.index = 1;
        root.weight = weightList[1];
        buildTree(weightList,root,childList[1],childList[2],childList,treeArray);
        markTree(root);
        int m = maxSymTree(root,n);
        System.out.println(m);
    }
    public static int markTree(TreeNode root){
        if (root.lChild == null & root.rChild == null){
            root.treeSize = 1;
        }else if (root.lChild != null & root.rChild == null){
            root.treeSize = markTree(root.lChild)+1;
        }else if (root.lChild == null){
            root.treeSize = markTree(root.rChild)+1;
        }else{
            root.treeSize = markTree(root.lChild)+markTree(root.rChild)+1;
        }
        return root.treeSize;
    }



    public static void buildTree(int[] weightList,TreeNode p, int lIndex, int rIndex, int[] childList, TreeNode[] treeArray) {
        TreeNode l = new TreeNode();
        TreeNode r = new TreeNode();
        if (lIndex != -1){
            l.weight = weightList[lIndex];
            l.parent = p;
            p.lChild = l;
            l.index = lIndex;
            treeArray[lIndex] = l;
            buildTree(weightList,l,childList[2*lIndex-1],childList[2*lIndex],childList,treeArray);
        }
        if (rIndex != -1){
            r.weight = weightList[rIndex];
            r.parent = p;
            p.rChild = r;
            r.index = rIndex;
            treeArray[rIndex] = r;
            buildTree(weightList,r,childList[2*rIndex-1],childList[2*rIndex],childList,treeArray);
        }
    }
    public static boolean checkSymmetric(TreeNode l, TreeNode r) {
        if (l.weight == r.weight & l.treeSize == r.treeSize) {
            boolean outside = true;
            boolean inside = true;
            // Check Outside (l.lChild and r.rChild)
            if (l.lChild == null) {
                outside = (r.rChild == null);
            } else {
                if (r.rChild == null) {
                    outside = false;
                } else {
                    outside = checkSymmetric(l.lChild, r.rChild);
                }
            }
            // Check Inside
            if (l.rChild == null) {
                inside = (r.lChild == null);
            } else {
                if (r.lChild == null) {
                    inside = false;
                } else {
                    inside = (checkSymmetric(l.rChild, r.lChild));
                }
            }
            return (inside & outside);
        } else {
            return false;
        }
    }
    public static int maxSymTree(TreeNode root, int n){
        int[] color = new int[n+1];
        int maxT = 1;
        Queue<TreeNode> Q = new LinkedList<TreeNode>();
        Q.offer(root);
        color[1] = 1;
        while (!Q.isEmpty()){
            TreeNode v = Q.poll();
            if (v.lChild != null){
                if (color[v.lChild.index] == 0){
                    Q.offer(v.lChild);
                    color[v.lChild.index] = 1;
                }
                color[v.index] = 2;
            }
            if (v.rChild != null){
                if (color[v.rChild.index] == 0){
                    Q.offer(v.rChild);
                    color[v.rChild.index] = 1;
                }
            }
            color[v.index] = 2;
            if ((v.lChild != null & v.rChild != null) && checkSymmetric(v.lChild, v.rChild)){
                int size = v.treeSize;
                if (size > maxT){
                    maxT = size;
                }
            }
        }
        return maxT;
    }
}
class TreeNode{
    TreeNode parent;
    TreeNode lChild;
    TreeNode rChild;
    int weight;
    int treeSize;
    int index;
}
