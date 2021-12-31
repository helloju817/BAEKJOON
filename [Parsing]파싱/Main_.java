package 스택;

import java.util.*;
public class Main_ {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String input=sc.nextLine();
        int sum=0;
        String arr[] = input.split(",");
        for(int i=0; i<arr.length;i++){
            sum+=Integer.parseInt(arr[i]);
                
            }
        System.out.print(sum);
    }
}