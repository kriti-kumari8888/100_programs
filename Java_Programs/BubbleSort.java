public class BubbleSort {
    public static void bubbleSort(int[] a) {
        int n = a.length;
        for (int i = 0; i < n - 1; i++)
            for (int j = 0; j < n - 1 - i; j++)
                if (a[j] > a[j+1]) {
                    int t = a[j]; a[j] = a[j+1]; a[j+1] = t;
                }
    }

    public static void main(String[] args) {
        int[] a = {64, 34, 25, 12, 22, 11, 90};
        System.out.print("Before:"); for (int v : a) System.out.print(" " + v);
        System.out.println();
        bubbleSort(a);
        System.out.print("After:"); for (int v : a) System.out.print(" " + v);
        System.out.println();
    }
}
