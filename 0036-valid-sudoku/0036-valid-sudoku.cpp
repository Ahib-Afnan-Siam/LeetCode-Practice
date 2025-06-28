class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<bool>> rowSeen(9, vector<bool>(9, false));
        vector<vector<bool>> colSeen(9, vector<bool>(9, false));
        vector<vector<bool>> boxSeen(9, vector<bool>(9, false));
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                
                int num = c - '1';
                if (rowSeen[i][num]) {
                    return false;
                }
                rowSeen[i][num] = true;
                
                if (colSeen[j][num]) {
                    return false;
                }
                colSeen[j][num] = true;
                
                int box_index = (i / 3) * 3 + (j / 3);
                if (boxSeen[box_index][num]) {
                    return false;
                }
                boxSeen[box_index][num] = true;
            }
        }
        
        return true;
    }
};