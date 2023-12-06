#include<bits/stdc++.h>
using namespace std;

vector<vector<char>> board;
int choice;
int row,column;
char turn;
bool draw = false;
string s1,s2;

void display(){
    cout<<"----------\t----------\n\n";
    cout<<"\t\t     |     |     \n";
    cout<<"\t\t  "<<board[0][0]<<"  |  "<<board[0][1]<<"  |  "<<board[0][2]<<"\n";
    cout<<"\t\t_____|_____|_____\n";
    cout<<"\t\t     |     |     \n";
    cout<<"\t\t  "<<board[1][0]<<"  |  "<<board[1][1]<<"  |  "<<board[1][2]<<"\n";
    cout<<"\t\t_____|_____|_____\n";
    cout<<"\t\t     |     |     \n";
    cout<<"\t\t  "<<board[2][0]<<"  |  "<<board[2][1]<<"  |  "<<board[2][2]<<"\n";
    cout<<"\t\t     |     |     \n";
}

void instruction(){
    cout<<"----------\t----------\n\n";
    cout<<"\t\t      |      |      \n";
    cout<<"\t\t  00  |  01  |  02  \n";
    cout<<"\t\t______|______|______\n";
    cout<<"\t\t      |      |      \n";
    cout<<"\t\t  10  |  11  |  12  \n";
    cout<<"\t\t______|______|______\n";
    cout<<"\t\t      |      |      \n";
    cout<<"\t\t  20  |  21  |  22  \n";
    cout<<"\t\t      |      |      \n";
}

void player_turn(){
    if(turn == 'X')
        cout<<"\nPlayer of current turn: "<<s1<<"\n";
    else if(turn == 'O')
        cout<<"\nPlayer of current turn: "<<s2<<"\n";

    
    string row1,column1;
    while(1){
        cout<<"\nChoose a row number (0 to 2):\n";
        getline(cin,row1);
        if(row1[0]<'0' || row1[0]>'2' || row1.size()!=1){
            cout<<row1<<" is not a valid row.\n";
            continue;
        }
        
        cout<<"Choose a column number (0 to 2):\n";
        getline(cin,column1);
        if(column1[0]<'0' || column1[0]>'2' || column1.size()!=1){
            cout<<column1<<" is not a valid column.\n";
            continue;
        }
        break;
    }
    int row=row1[0]-'0';
    int column=column1[0]-'0';

    if(turn == 'X' && board[row][column] != 'X' && board[row][column] != 'O'){
        board[row][column] = 'X';
        turn = 'O';
    }else if(turn == 'O' && board[row][column] != 'X' && board[row][column] != 'O'){
        board[row][column] = 'O';
        turn = 'X';
    }else {
        cout<<"Box already filled!\nPlease choose another!!\n\n";
        player_turn();
        return;
    }
    
    display();
}

bool empty(){
    //for simple row and column
    for(int i=0; i<3; i++){
        int val1=(board[i][0] + board[i][1] + board[i][2]);//row
        int val2=(board[0][i] + board[1][i] + board[2][i]);//column
        if(val1== 264 || val2==264 || val1==237 || val2==237)
        	return false;
    }
    
    //for both diagoonals
    int val1=(board[0][0] + board[1][1] + board[2][2]);
    int val2=(board[0][2] + board[1][1] +  board[2][0]);
    if( val1==264 || val2==264 || val1==237 || val2==237 )
	    return false;
    
    //if any space empty
    for(int i=0; i<3; i++){
	    for(int j=0; j<3; j++){
		    if(board[i][j] != 'X' && board[i][j] != 'O')
			    return true;
		}
	}

    draw = true;
    return false;
}

bool YorN(){
    string ch="";
    while(ch!="Y" || ch!="N"){
        cout<<"\n\nWould you like to play again? (Y/N)"<<endl;
        getline(cin,ch);
        if(ch=="Y")
            return true;
        else if(ch=="N")
            return false;
        else
            cout<<ch<<" is not a valid answer\n";
    }
    return true;
}

int main()
{
    cout<<"-------------------------Instruction---------------------------\n\n";
    cout<<"Every Box is represented by a row and a column respectively as shown below!!\n";
    cout<<"Select the row number and column number accordingly!!\n";
    instruction();
    while(1){
        string s;
        s1="",s2="";
        while(s1==s2){
            cout<<"\nEnter the name of 'X' player:\n";
            getline(cin,s1);
            if(!(s1[0]>='a' && s1[0]<='z') && !(s1[0]>='A' && s1[0]<='Z')){
                cout<<"Frist character of name should start with an Alphabet!!\n";
                s1="";
                continue;
            }
            cout<<"\nEnter the name of 'O' player:\n";
            getline(cin,s2);
            if(!(s2[0]>='a' && s2[0]<='z') && !(s2[0]>='A' && s2[0]<='Z')){
                cout<<"Frist character of name should start with an Alphabet!!\n";
                s1=s2;
            }
            else if(s1==s2)
                cout<<"Both should have different name!!\n";
        }
        
        while(s!=s1 && s!=s2){
            cout<<"\nWho plays first, "<<s1<<" or "<<s2<<"?\n";
            getline(cin,s);
            if(s!=s1 && s!=s2)
                cout<<s<<" is not a registered player.\n";
        }
        if(s==s1)
            turn='X';
        else    turn='O';
        
        board={{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
        cout<<"\n"<<"    "<<s1<<": [X]  "<<s2<<": [O]\n\n";
        cout<<"Game board\n";
        display();
        while(empty()){
            player_turn();
            empty();
        }
        cout<<"\n\n\tGame is over:\n";
        if(turn == 'O' && draw == false)
            cout<<"\t"<<s1<<" wins!";
        else if(turn == 'X' && draw == false)
            cout<<"\t"<<s2<<" wins!";
        else
            cout<<"\t"<<"it is a tie!";
        if(YorN())  continue;
        else    break;
    }
    cout<<"Bye!\n";
    return 0;
}
