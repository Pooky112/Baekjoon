import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    private static void hanoiTower(int n, int moveFrom, int moveTo, int moveThrough){
        if (n == 1){
            System.out.println(moveFrom + " " + moveTo);
            return;
        }

        hanoiTower(n - 1, moveFrom, moveThrough, moveTo);
        System.out.println(moveFrom + " " + moveTo);
        hanoiTower(n - 1, moveThrough, moveTo, moveFrom);
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        //System.out.println((1L << N) - 1);
        System.out.println(BigInteger.TWO.pow(N).subtract(BigInteger.ONE));

        if (N <= 20) {
            hanoiTower(N, 1, 3, 2);
        }

        sc.close();
    }
}
