import java.util.Scanner;

public class TestScanner {
  public static void main(String args[]) {
    Scanner sc = new Scanner (System.in);
    System.out.println("Please enter a number: ");
    double num = sc.nextDouble();
    System.out.println("Please enter another number: ");
    num += sc.nextInt();
    
    double avg = num/2;
    System.out.println("Average: " + avg);
    
    sc.close();
  }
  
}