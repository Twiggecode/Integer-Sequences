public class InsertionSort {
    public static void insertionSort(int[] num){
        int n = num.length;
        for(int i = 1; i < n; i++){
            int pivot = num[i];
            int j = i - 1;
            while(j >= 0 && num[j] > pivot){
                num[j + 1] = num[j];
                j--;
            }
            num[j + 1] = pivot;
        }
    }
}
