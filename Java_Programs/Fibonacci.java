import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N (>=1): ");
        if (!sc.hasNextInt()) { System.err.println("Invalid input"); sc.close(); System.exit(1); }
        int n = sc.nextInt();
        if (n < 1) { System.err.println("N must be >= 1"); sc.close(); System.exit(1); }
        long a = 0, b = 1;
        System.out.print("Fibonacci:");
        for (int i = 0; i < n; i++) {
            System.out.print(" " + a);
            long t = a + b; a = b; b = t;
        }
        System.out.println();
        sc.close();
    }
}
