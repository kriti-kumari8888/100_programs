import java.util.Scanner;

public class Factorial {
    public static long factorial(int n) {
        long r = 1;
        for (int i = 2; i <= n; i++) r *= i;
        return r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a non-negative integer: ");
        if (!sc.hasNextInt()) { System.err.println("Invalid input"); sc.close(); System.exit(1); }
        int n = sc.nextInt();
        if (n < 0) { System.err.println("Negative number not allowed"); sc.close(); System.exit(1); }
        System.out.println(n + "! = " + factorial(n));
        sc.close();
    }
}
