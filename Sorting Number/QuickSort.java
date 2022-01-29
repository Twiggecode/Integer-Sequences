public class QuickSort {
    public static void quickSort(int[] num, int n){
        quickSortRecursive(num, 0, n - 1);
    }

    public static void quickSortRecursive(int[] num, int l, int r){
        if(l >= r) return;

        int div = partition(num, l, r);
        quickSortRecursive(num, l, div - 1);
        quickSortRecursive(num, div + 1, r);
    }

    public static int partition(int[] num, int l, int r){
        int pivot = num[r];
        int index = l;
        for(int i = l; i < r; i++){
            if(num[i] > pivot){
                int temp = num[index];
                num[index] = num[i];
                num[i] = temp;
                index++;
            }
        }
        int temp = num[index];
        num[index] = num[r];
        num[r] = temp;
        return index;
    }
}
