import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int r = sc.nextInt(), c = sc.nextInt();
		String m[][] = new String[r][c];
		for(int i=0;i<r;i++){
		    for(int j=0;j<c;j++){
		        m[i][j]=sc.next();
		    }
		}
		for(int i=0;i<r;i++){ 
		    for(int j=0;j<c;j++){
		        if (m[i][j].equals("+"))
		            System.out.print(Integer.parseInt(m[i-1][j])+Integer.parseInt(m[i+1][j])+" ");
		        else if (m[i][j].equals("-"))
		            System.out.print(Math.abs(Integer.parseInt(m[i-1][j])-Integer.parseInt(m[i+1][j]))+" ");
		        else
		            System.out.print(m[i][j]+" ");
		    }
		System.out.println();
		}
	}
}
