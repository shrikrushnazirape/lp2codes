#include<bits/stdc++.h>
using namespace std;

void printBoard(vector<vector<int>> v){
    for(int i=0; i<v.size(); i++){
        for(int j=0; j<v[i].size(); j++){
            cout<<v[i][j]<<" ";

        }
        cout<<"\n";
    }
}

bool isSafe(int row, int col, vector<vector<int>>board, int n) {
        // check upper diagonal
        int duprow = row;
        int dupcol = col; 
        
        while(row >= 0 && col >= 0) {
            if(board[row][col] == 1) return false;
            row--;
            col--;
        }
        
        
        col = dupcol; 
        row = duprow;
        while(col>=0) {
            if(board[row][col] == 1) return false;
            col--; 
        }
    
        row = duprow;
        col = dupcol; 
        while(row<n && col>=0) {
            if(board[row][col] == 1) return false;
            row++;
            col--; 
        }
        
        return true; 
    }

void solve(int col, vector<vector<int>> &board, vector<vector<int>> &ans, int n){

    if(col == n){
        ans = board;
        return;
    }
    for(int row=0; row<n ; row++){
        if(isSafe(row, col, board, n)){
  

            board[row][col] = 1;
            solve(col+1, board, ans, n);
            board[row][col] = 0;
        }
    }
}

int main(){
    vector<vector<int>>ans;
    vector<vector<int>>board;
    int n;
    cout<<"Enter the size of board : ";
    cin>>n;
    
    for(int i=0; i<n; i++){
        vector<int>test;
        for(int i=0; i<n; i++)test.push_back(0);
        board.push_back(test);
    }
    cout<<"\n\nAnswer for the given n queen problem : \n";
    solve(0, board, ans, n);
    printBoard(ans);
    return 0;
}