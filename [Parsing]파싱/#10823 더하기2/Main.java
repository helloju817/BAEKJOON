
import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String line="";
		while(sc.hasNextLine()) {
			String line1 = sc.nextLine();
			if(line1.equals("")) break;
			line += line1;
		}
		//System.out.println(line);
		//문자열이 한 종류의 구분자로 연결되어 있을 경우, StringTokenizer 클래스를 사용하면 쉽게 문자열을 분리할 수 있다.
		StringTokenizer st = new StringTokenizer(line,","); 
				int sum=0;
				while(st.hasMoreTokens()) {
					sum+=Integer.parseInt(st.nextToken());
				}
				System.out.println(sum);
	}

}