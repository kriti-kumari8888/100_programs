public class SwapDemo {
    public static void swap(int[] pair) {
        int t = pair[0]; pair[0] = pair[1]; pair[1] = t;
    }

    public static void main(String[] args) {
        int[] pair = {10, 20};
        System.out.println("Before: x=" + pair[0] + " y=" + pair[1]);
        swap(pair);
        System.out.println("After:  x=" + pair[0] + " y=" + pair[1]);
    }
}
