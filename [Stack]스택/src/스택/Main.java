package 스택;

import java.util.Scanner;
public class Main {
	public static int[] stack;
	public static int size = 0;
 
	public static void main(String[] args) {
 
		Scanner sc = new Scanner(System.in);
		StringBuilder b = new StringBuilder();
		int N = sc.nextInt();
		stack = new int[N];
		
		for(int i = 0; i < N; i++) {
			String command = sc.next();
			
			switch (command) {
			case "push":	//정수 X를 스택에 넣는 연산이다.
				push(sc.nextInt());
				break;
			case "pop":		//스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
				b.append(pop()).append('\n');
				break;
			case "size":	//스택에 들어있는 정수의 개수를 출력한다.
				b.append(size).append('\n');
				break;
			case "empty":	//스택이 비어있으면 1, 아니면 0을 출력한다.
				b.append(empty()).append('\n');
				break;
			case "top":		//스택의 가장 위에 있는 정수를 출력한다
				b.append(top()).append('\n');
				break;
			}
		}
		System.out.println(b);
	}
	public static void push(int item) {
		stack[size] = item;
		size++;
	}
	public static int pop() {
		//정수가 없는 경우에는 -1을 출력한다.
		if(size > 0) {
			int ans = stack[size - 1];
			stack[size - 1] = 0;
			size--;
			return ans;
			
			}
		else {
			return -1;
		}
	}
	public static int empty() {
		if(size > 0) {
			return 0;}
		else {return 1;}
	}
	public static int top() {
		//정수가 없는 경우에는 -1을 출력한다.
		if(size >0 ) {
			return stack[size - 1];
		}
		else {
			return -1;
		}
	}
}