class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def recurse(i, r, c):
            if word[i] != board[r][c]:
                return False

            if word[i] == board[r][c] and i == len(word) - 1:
                return True

            tmp = board[r][c]
            board[r][c] = "#"
                
            for dr, dc in directions:
                new_row = r + dr
                new_col = c + dc

                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and recurse(i + 1, new_row, new_col):
                    return True
            
            board[r][c] = tmp
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if recurse(0, r, c):
                    return True
        
        return False

