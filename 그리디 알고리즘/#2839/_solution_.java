import java.util.Scanner;
public class _solution_{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int N=scan.nextInt();
        int a,b;
        a=N/5;
        while(a>=0){
            if((N-a*5)%3==0){
                b=(N-a*5)/3+a;
            System.out.println(b);
            return;
        }
            a--;
        }
        //정확하게 만들 수 없는 경우 ㅣ -1 
        if((N-a*5)/3!=0)
        System.out.println("-1");
        return;
    }
}
