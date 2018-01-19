
import java.util.Scanner;

public class HelloJava{
	
	public static void main(String[] args){
		
		Scanner sc = new Scanner(System.in);
		System.out.print("input: ");
		String s = sc.nextLine();  
		
		System.out.println("hello "+s);
	}
}