from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # for row in range(9):
        #     seen=set()
        #     for j in range(9):
        #         if board[row][j]=='.':
        #             continue
        #         if board[row][j] in seen:
        #             return False
        #         seen.add(board[row][j])
        
        # for col in range(9):
        #     seen=set()
        #     for i in range(9):
        #         if board[i][col]=='.':
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])

        # for box in range(9):
        #     seen=set()
        #     for i in range(3):
        #         for j in range(3):
        #             row=(box//3)*3+i
        #             col=(box%3)*3+j
        #             if board[row][col]=='.':
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True


        # #single pass validation using hashset

        # row=defaultdict(set)
        # col=defaultdict(set)
        # square=defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c]=='.':
        #             continue
        #         if (board[r][c] in row[r]
        #             or board[r][c] in col[c]
        #             or board[r][c] in square[(r//3),(c//3)]):
        #             return False
        #         row[r].add(board[r][c])
        #         col[c].add(board[r][c])
        #         square[(r//3),(c//3)].add(board[r][c])
        # return True


        #using bitmasking

        rows=[0]*9
        cols=[0]*9
        boxes=[0]*9

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                val=int(board[r][c])-1

                if (1<<val) & rows[r]:
                    return False
                if (1<<val) & cols[c]:
                    return False
                if(1<<val) & boxes[(r//3)*3+(c//3)]:
                    return False
                
                rows[r]|=(1<<val)
                cols[c]|=(1<<val)
                boxes[(r//3)*3+(c//3)]|=(1<<val)
        return True

if __name__=='__main__':
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."]
             ,["6",".",".","1","9","5",".",".","."]
             ,[".","9","8",".",".",".",".","6","."]
             ,["8",".",".",".","6",".",".",".","3"]
             ,["4",".",".","8",".","3",".",".","1"]
             ,["7",".",".",".","2",".",".",".","6"]
             ,[".","6",".",".",".",".","2","8","."]
             ,[".",".",".","4","1","9",".",".","5"]
             ,[".",".",".",".","8",".",".","7","9"]]
    
    board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board))
    print(sol.isValidSudoku(board2))
    