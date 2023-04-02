class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowCheck = {i: [] for i in range(len(board))}
        colCheck = {j: [] for j in range(len(board[0]))}
        squareCheck = {
            (i//3,j//3): []
            for i in range(len(board))
            for j in range(len(board[0]))
        }

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j]=='.':
                    continue
                
                elif board[i][j] in rowCheck[i] or board[i][j] in colCheck[j] or board[i][j] in squareCheck[(i//3,j//3)]:
                    return False
                else:
                    rowCheck[i].append(board[i][j])
                    colCheck[j].append(board[i][j])
                    squareCheck[(i//3,j//3)].append(board[i][j])
        
        return True
        
 """
 Time complexity: O(N^2), N = Length of board
 Space complexity: O(3*N^2) = O(N^2) since each digit is tracked in 3 ways - rows, columns, squares
 """
