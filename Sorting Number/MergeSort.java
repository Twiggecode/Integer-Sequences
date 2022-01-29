public class MergeSort {
    public static void mergeSort(int[] num, int n){
        if(n < 2){
            return;
        }
        int mid = n / 2;
        int[] l = new int[mid];
        int[] r = new int[n - mid];
        for(int i = 0; i < mid; i++){
            l[i] = num[i];
        }
        for(int i = mid; i < n; i++){
            r[i - mid] = num[i];
        }
        mergeSort(l, mid);
        mergeSort(r, n - mid);

        merge(num, l, r, mid, n - mid);
    }
    public static void merge(int[] num, int[] l, int[] r, int left, int right){
        int i = 0, j = 0, k = 0;
        while(i < left && j < right){
            if(l[i] <= r[j]){
                num[k++] = l[i++];
            }else{
                num[k++] = r[j++];
            }
        }
        while(i < left){
            num[k++] = l[i++];
        }
        while(j < right){
            num[k++] = r[j++];
        }
    }
}