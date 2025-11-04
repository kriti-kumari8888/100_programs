import java.util.Scanner;

public class Palindrome {
    public static boolean isPalindrome(String s) {
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) return false;
            i++; j--;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String line = sc.nextLine();
        String trimmed = line.replaceAll("\\s+", ""); // remove spaces
        if (isPalindrome(trimmed)) System.out.println("The string \"" + line + "\" is a palindrome");
        else System.out.println("The string \"" + line + "\" is not a palindrome");
        sc.close();
    }
}
