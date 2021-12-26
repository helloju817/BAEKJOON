import java.util.Scanner;
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int count=0;
        int N =sc.nextInt();    //레벨
        int arr[]=new int[101];   //레벨 수 만큼 배열 생성
        
        for (int i=1;i<N+1;i++)
        {
            arr[i] = sc.nextInt();  //레벨 점수 값 입력 받아 배열에 저장
        }
        
        int score=arr[N];             
        for(int i=N-1;i>0;i--){     
            while(arr[i]>=score){   //점수 감소 조건
                arr[i]=arr[i]-1;
                count++;
            }
            score=arr[i];
        }
        System.out.println(count);
    }
}
