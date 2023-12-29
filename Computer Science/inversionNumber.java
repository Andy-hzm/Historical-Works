package com.SchoolWork.Assignment;
import java.util.Scanner;

public class inversionNumber {

    public static long count_inverse = 0;
    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] data = new int[n];
        for(int i=0;i<n;i++){
            data[i]=in.nextInt();
        }
        int[] tmpArray = new int[data.length];
        mergeSort(data, tmpArray, 0, data.length - 1);
        System.out.println(count_inverse);
    }
    public static void mergeSort(int[] a, int[] tmpArray, int left, int right) {
        if (left < right) {
            int center = (left + right) / 2;
            mergeSort(a, tmpArray, left, center);
            mergeSort(a, tmpArray, center + 1, right);
            merge(a, tmpArray, left, center + 1, right);
        }}
    public static void merge(int[] a, int[] tmpArray, int leftPos, int rightPos, int rightEnd){
        int leftEnd = rightPos-1, tmpPos = leftPos;
        int numElements = rightEnd - leftPos + 1;
        while (leftPos <= leftEnd && rightPos <= rightEnd){
            if (a[leftPos] <= a[rightPos]) {
                tmpArray[tmpPos++] = a[leftPos++];
            }
            else {
                count_inverse += (leftEnd-leftPos+1);
                tmpArray[tmpPos++] = a[rightPos++];
            }
        }

        while (leftPos <= leftEnd) {
            tmpArray[tmpPos++] = a[leftPos++];
        }
        while (rightPos <= rightEnd) {
            tmpArray[tmpPos++] = a[rightPos++];
        }
        for (int i = 0; i < numElements; i++, rightEnd--) {
            a[rightEnd] = tmpArray[rightEnd];
        }
    }
}
