import java.io.*;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException {

//        Scanner scanner = new Scanner(System.in);
//
//        int a = scanner.nextInt();
//        int b = scanner.nextInt();
//        scanner.close();
//
//        System.out.println(a + b);
//        System.out.println(a - b);
//        System.out.println(a * b);
//        System.out.println(a / b);
//        System.out.println(a % b);

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    String input = br.readLine();
    StringTokenizer st = new StringTokenizer(input);
    int A = Integer.parseInt(st.nextToken());
    int B = Integer.parseInt(st.nextToken());

    System.out.println(A + B);
    System.out.println(A - B);
    System.out.println(A * B);
    System.out.println(A / B);
    System.out.println(A % B);

//    bw.write((A + B) + "\n");
//    bw.write((A - B) + "\n");
//    bw.write((A * B) + "\n");
//    bw.write((A / B) + "\n");
//    bw.write((A % B) + "\n");

//    bw.flush();
//    bw.close();
    }

}
