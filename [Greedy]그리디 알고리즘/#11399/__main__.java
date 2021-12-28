import java.util.*;
public class __main__{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        int arr[]=new int[N];
        for (int i=0; i<N;i++)
        {
            arr[i] = sc.nextInt();
           
        }
        Arrays.sort(arr);
        int answer=0;
        int curr=0;
        for ( int j=0;j<N;j++) {
        	answer+=curr+arr[j];
        	curr+=arr[j];
        }

        System.out.println(answer);
    }
}