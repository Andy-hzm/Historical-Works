package com.SchoolWork.Assignment;

import java.util.Arrays;
import java.util.Scanner;

public class twoSum {
    public static void main(String Args[]){
        // Input size and target
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int target = in.nextInt();
        // Input array
        int[] data = new int[n];
        for(int i=0;i<n;i++){
            data[i]=in.nextInt();
        }
        // Two Sum Algorithm
        int[] arr = data.clone();
        int[] target_number = two_sum(arr, target);
        int count = 0;
        if (target_number[0] != target_number[1]){
            for (int i = 0; i < data.length; i++) {
                if (data[i] == target_number[0]){
                    System.out.print(i+1);
                    count++;
                    System.out.print(" ");
                }
                if (data[i] == target_number[1]){
                    System.out.print(i+1);
                    count++;
                    System.out.print(" ");
                }
                if (count == 2){
                    break;
                }
            }
        }
        if (target_number[0] == target_number[1]){
            for (int i = 0; i < data.length; i++) {
                if (data[i] == target_number[0]){
                    System.out.print(i+1);
                    count++;
                    System.out.print(" ");
                }
                if (count == 2){
                    break;
                }
            }
        }
    }
    public static int[] two_sum(int arr[], int target){
        int n = arr.length;
        int[] sorted_arr;
        sorted_arr = quick_sort(arr,0,n-1);
        int[] result = new int[2];
        for (int f = 0; f < n; f++) {
            int s = binary_search(sorted_arr, target-arr[f], f+1, n-1);
            if (s != -1){
                result[0] = arr[f];
                result[1] = arr[s];
                break;
            }
        }
        return result;
    }
    public static int[] quick_sort(int arr[], int left, int right){
        if (left >= right){
            return arr;
        }
        int pivot = left;
        int pivotNewPosition = partition(arr, left, right, pivot);
        quick_sort(arr, left, pivotNewPosition-1);
        quick_sort(arr, pivotNewPosition+1, right);
        return arr;
    }
    public static int partition(int[] arr, int left, int right, int pivot) {
        //record the pivot data
        int pivotVal = arr[pivot];
        //swap the pivot data and the last data
        swap(arr, right, pivot);
        //record the next position to put data smaller than pivotVal
        int nextsmallpos = left;
        for (int j = left; j <=right-1 ; j++) {
            if (arr[j] < pivotVal){
                swap(arr, nextsmallpos++, j);
            }
        }
        swap(arr, nextsmallpos,right);
        return nextsmallpos;
    }
    public static void swap(int[] arr, int first, int second) {
        int i_f = arr[first];
        int i_s = arr[second];
        arr[second] = i_f;
        arr[first] = i_s;
    }
    public static int binary_search(int arr[], int target, int low, int high) {
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (arr[mid] == target){
                return mid;
            }
            if (arr[mid] < target){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return -1;
    }
}
