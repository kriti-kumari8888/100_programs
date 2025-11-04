import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter expression (e.g. 2.5 + 3): ");
        double a, b; String op;
        if (!sc.hasNextDouble()) { System.err.println("Invalid input"); sc.close(); System.exit(1); }
        a = sc.nextDouble();
        if (!sc.hasNext()) { System.err.println("Invalid input"); sc.close(); System.exit(1); }
        op = sc.next();
        if (!sc.hasNextDouble()) { System.err.println("Invalid input"); sc.close(); System.exit(1); }
        b = sc.nextDouble();
        sc.close();
        double r = 0; boolean ok = true;
        switch (op) {
            case "+": r = a + b; break;
            case "-": r = a - b; break;
            case "*": r = a * b; break;
            case "/": if (b == 0) { System.err.println("Division by zero"); System.exit(1); } r = a / b; break;
            default: ok = false;
        }
        if (!ok) { System.err.println("Unsupported operator: " + op); System.exit(1); }
        System.out.println("Result: " + r);
    }
}
