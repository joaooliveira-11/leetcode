class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def backtrack(row, col, idx):
            if idx == len(word):
                return True

            if (row, col) in visited:
                return False
            
            if not (0 <= row < rows) or not (0 <= col < cols):
                return False

            if board[row][col] != word[idx]:
                return False

            visited.add((row, col))
            
            found = backtrack(row+1, col, idx+1) or backtrack(row-1, col, idx+1) or backtrack(row, col+1, idx+1) or backtrack(row, col-1, idx+1)

            visited.remove((row, col))

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False
        


    
