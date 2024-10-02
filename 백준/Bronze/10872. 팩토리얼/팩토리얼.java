import java.util.Scanner;

class Main {
    private static int factorial(int n){
        if (n == 0) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        int result = factorial(N);
        
        System.out.println(result);
    }
}
