class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        R = len(board)
        C = len(board[0])
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if self.matchAround(board, r, c, word[1:], [(r, c)]):
                        return True
                    else:
                        continue
                else:
                    continue
        return False


    def matchAround(self, board, row, column, word, path):
        R = len(board)
        C = len(board[0])
        if word == "":
            return True
        # (row, column)左侧是否有 = char 的
        if column - 1 >= 0 and board[row][column - 1] == word[0] and (row, column - 1) not in path:
            tempPath = [c for c in path]
            tempPath.append((row, column - 1))
            if self.matchAround(board, row, column - 1, word[1:], tempPath):
                return True
        # (row, column)右侧是否有 = char 的
        if column + 1 < C and board[row][column + 1] == word[0] and (row, column + 1) not in path:
            tempPath = [c for c in path]
            tempPath.append((row, column + 1))
            if self.matchAround(board, row, column + 1, word[1:], tempPath):
                return True
        # (row, column)上方是否有 = char 的
        if row - 1 >= 0 and board[row - 1][column] == word[0] and (row - 1, column) not in path:
            tempPath = [c for c in path]
            tempPath.append((row - 1, column))
            if self.matchAround(board, row - 1, column, word[1:], tempPath):
                return True
        # (row, column)下方是否有 = char 的
        if row + 1 < R and board[row + 1][column] == word[0] and (row + 1, column) not in path:
            tempPath = [c for c in path]
            tempPath.append((row + 1, column))
            if self.matchAround(board, row + 1, column, word[1:], tempPath):
                return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
# ["A","B","C","E"]
# ["S","F","E","S"]
# ["A","D","E","E"]