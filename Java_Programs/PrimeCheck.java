import java.util.Scanner;

public class PrimeCheck {
    public static boolean isPrime(long n) {
        if (n < 2) return false;
        if (n % 2 == 0) return n == 2;
        for (long i = 3; i * i <= n; i += 2) if (n % i == 0) return false;
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        if (!sc.hasNextLong()) { System.err.println("Invalid input"); sc.close(); System.exit(1); }
        long n = sc.nextLong();
        System.out.println(n + (isPrime(n) ? " is prime" : " is not prime"));
        sc.close();
    }
}
