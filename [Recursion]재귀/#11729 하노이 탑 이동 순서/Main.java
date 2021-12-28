
import java.util.Scanner;
public class Main{
	static StringBuilder sb = new StringBuilder();
    public static void main(String[] args){
    	//StringBuilder를 이용하면 메모리 사용량을 줄일 수 있다.
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        sb.append(((int)Math.pow(2,N)-1)+"\n");
        move(N, 1,3,2);
        System.out.println(sb.toString());
    }
    private static void move(int N, int start, int end, int middle) {
    	if(N==1) {
    		sb.append(start+" "+ end+"\n");
    		return;
    	}
    	
    	move(N-1, start, middle, end);
    	move(1, start, end, middle);
    	move(N-1,middle, end, start);
    		
    }
}