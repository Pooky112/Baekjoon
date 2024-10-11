import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void quickSort(int[] arr, int low, int high){
        if (low >= high){
            return;
        }

        int pivot = low + (high - low) / 2;
        int pivotValue = arr[pivot];

        int left = low;
        int right = high;
        while (left <= right){
            while (arr[left] < pivotValue){
                left++;
            }
            while (arr[right] > pivotValue){
                right--;
            }

            if (left <= right){
                int temp = arr[right];
                arr[right] = arr[left];
                arr[left] = temp;
                left++;
                right--;
            }
        }

        quickSort(arr, low, right);
        quickSort(arr, left, high);

    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] numList = new int[N];
        for (int i = 0; i < N; i++){
            numList[i] = sc.nextInt();
        }
//        Arrays.sort(numList);
        quickSort(numList, 0, N - 1);

        for (int num: numList){
            System.out.println(num);
        }
    }
}
