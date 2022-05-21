import java.util.Scanner;
public class Main {
    public static void main(String args[]) {
    Scanner s=new Scanner(System.in);
    int X=s.nextInt();
    int Y=s.nextInt();
    int X1=0,y1=0,sum=0,sum1=0;
    if(X/1000!=0){
        X1=(X/1000)+((X%1000)/100)*10+((X%100)/10)*100+(X%10)*1000;
    }
    else if(X/100!=0){
        X1=(X/100)+((X%100)/10)*10+(X%10)*100;
    }
    else if(X/10!=0){
        X1=(X/10)+(X%10)*10;
    }
    else{
        X1=X;
    }
    if(Y/1000!=0){
        y1=(Y/1000)+((Y%1000)/100)*10+((Y%100)/10)*100+(Y%10)*1000;
    }
    else if(Y/100!=0){
        y1=(Y/100)+((Y%100)/10)*10+(Y%10)*100;
    }
    else if(Y/10!=0){
        y1=(Y/10)+(Y%10)*10;
    }
    else{
        y1=Y;
    }
    sum=X1+y1;
    if(sum/1000!=0){
        sum1=(sum/1000)+((sum%1000)/100)*10+((sum%100)/10)*100+(sum%10)*1000;
    }
    else if(sum/100!=0){
        sum1=(sum/100)+((sum%100)/10)*10+(sum%10)*100;
    }
    else if(sum/10!=0){
        sum1=(sum/10)+(sum%10)*10;
    }
    else{
        sum1=sum;
    }
    System.out.println(sum1);
    }
}
