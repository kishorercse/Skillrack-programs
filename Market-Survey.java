/*
Market Research firm is carrying out a survey regarding popular brands. The person who has the best pulse of the survey population will be rewarded by the firm. 
The survey comprises of N questions was taken by M participants, not at the same time but one after the other. Clearly, there is no correct answer since it is a 
survey of brands. Each question can have only four options (1,2,3,4). Most expected answers to different questions is used as a template to measure brand popularity. 
Think of this as a default answer sheet where the question paper is the Survey. '0' represents no answer to a question. Thus it means that the participant has skipped 
answering that question. 

Right Answer:
For a particular question, the highly chosen option till that point of time is treated as the correct answer. If multiple options
have the same count, then out of those options the one which was chosen recently is treated as the right answer. Score of a participant: One point will be awarded for 
each right answer. No negative points for wrong answers. 

Instant Result: 
This is shared to the participant instantly after completion of his/her exam. (this is equal to
number of right answers) 

Final Result: 
Only the final top scorer(TOPPER) is announced along with his score. 

Note: 
At the end of all M participants completing the exam, the final right answers gets decided.
Based on these answers score of each candidate gets recalculated and the one with highest score is the TOPPER!!!
If more than one participant gets the top score then the one among them who attempted the exam first, is treated as TOPPER.

Boundary Condition(s):
1 <= N, M <= 1000 

Input Format: 
The first line contains N. 
The second line contains M. 
The third line contains N integers representing the default answers. (There are no 0 in the default answers) 
The next M lines, each contains N integers representing the response of a participant. 

Output Format: 
The first M lines, each contains an integer representing the instant result of a articipant. 
The (M+1)st line contains the TOPPERs id and his/her score. (assume ids start with 1) 

Example Input/Output 1:
Input: 
10 
2 
1 4 4 1 2 2 3 1 2 1 
1 3 4 4 2 1 3 2 4 2 
4 3 2 2 4 2 3 2 4 1 

Output 
4 
4 
1 7 

Explanation: 
Number of questions = 10 
Number of participants = 2 
Default answers: 1 4 4 1 2 2 3 1 2 1 (Latest Key is same as Default answers) 
First participant's answers: 1 3 4 4 2 1 3 2 4 2 
Right answers: 4 (Instant result of the first participant) 
Latest Key: 1 3 4 4 2 1 3 2 4 2 
Second participant's answers: 4 3 2 2 4 2 3 2 4 1
Right answers : 4 (Instant result of the second Participant) 
Latest Key : 1 3 4 2 2 2 3 2 4 1 
Final key : 1 3 4 2 2 2 3 2 4 1 (Final Key is same as Latest Key at the end of all participants completing the exam)
Right answers of the participant 1 = Right answers of the participant 2 = 7.
So the topper is the first participant with score 7. 

Example Input/Output 2: 
Input: 
9 
5 
2 1 4 4 1 2 1 3 1 
1 3 1 1 4 1 4 3 2 
2 1 4 1 3 0 2 3 3 
3 4 2 2 0 2 2 0 4 
3 2 2 4 4 4 4 4 4 
4 0 3 2 2 1 2 2 3 

Output: 
1 
2 
1 
1 
0 
2 4
*/
import java.util.*;
public class Hello {

    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n=sc.nextInt(),m=sc.nextInt(), def[]=new int[n], student[][]=new int[m][n], key[][]=new int[n][4];
		for(int i=0;i<n;i++){
		    def[i]=sc.nextInt();
		    key[i][def[i]-1]+=1;
		}
		for(int i=0;i<m;i++){
		    int score=0;
		    for(int j=0;j<n;j++){
    		    student[i][j]=sc.nextInt();
    		    int t=student[i][j]-1;
    		    if (t>=0){
    		        key[j][t]+=1;
        		    if (student[i][j]==def[j]){
        		        score+=1;
        		    }
        		    else{
        		        if (i==0 || ( t>=0 && key[j][t]>=key[j][(t+1)%4] && key[j][t]>=key[j][(t+2)%4] && key[j][t]>=key[j][(t+3)%4] )){
        		            def[j]=student[i][j];
        		        }
        		    }
    		    }
		    }
		    System.out.println(score);
		}
		int maxScore=0, id=-1;
		for(int i=0;i<m;i++){
		    int score=0;
		    for(int j=0;j<n;j++){
		        if (student[i][j]==def[j])
		            score+=1;
		    }
		    if(score>maxScore){
		        maxScore=score;
		        id=i;
		    }
		}
		System.out.print((id+1)+" "+maxScore);
	}
}
