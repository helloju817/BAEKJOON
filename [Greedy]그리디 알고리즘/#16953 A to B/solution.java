import java.util.Scanner;
public class solution{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int count=1;
        int A =sc.nextInt();    //A
        int B =sc.nextInt();    //B
        
        while(A!=B) {
        	if(B<A) {
        		System.out.println(-1);
        		System.exit(0);
        	}
        	if(B%10==1){
        		B=B/10;
        	}
        	else if(B%2==0){
        		B=B/2;
        	}
        	else {
        		System.out.println(-1);
        		System.exit(0);
        	}
        count++;
       }
       System.out.println(count);
    }
}
 
